import ast
import os
import sys
import re

FOLDER = "src"
OUTPUT_FILE = "quadratic-invaders.py"

def merge_python_files(src_folder):
    """
    Merge all Python files in src_folder into a single output.
    Handles imports deduplication, removal of internal imports,
    and class ordering by dependencies.

    Made by ChatGPT with few tweaks
    """
    # 1. Retrieve all .py files
    py_files = []
    for root, dirs, files in os.walk(src_folder):
        for name in files:
            if name.endswith('.py'):
                py_files.append(os.path.join(root, name))
    py_files.sort()  # Sort for a deterministic order

    # names of internal modules (.py files)
    internal_modules = {os.path.splitext(os.path.basename(p))[0] for p in py_files}

    all_imports = set()   # Set to deduplicate external imports
    classes = {}          # Dictionary class -> {code, deps}
    other_code_lines = [] # Lines of code that are not imports and not classes

    # 2. Process each file: collect imports and class definitions
    for filepath in py_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read().rstrip('\n')
        try:
            tree = ast.parse(code, filepath)
        except SyntaxError as e:
            print(f"SyntaxError in {filepath}: {e}", file=sys.stderr)
            continue
        code_lines = code.splitlines()
        class_lines = set()

        for node in tree.body:
            # External imports -> keep, internal imports -> ignore
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name not in internal_modules:  # keep only if external module
                        all_imports.add(code_lines[node.lineno - 1].strip())

            elif isinstance(node, ast.ImportFrom):
                module = node.module.split('.')[0] if node.module else ""
                if module not in internal_modules:  # keep only if external module
                    all_imports.add(code_lines[node.lineno - 1].strip())

            elif isinstance(node, ast.ClassDef):
                # Extract the class block safely (handle nodes without end_lineno)
                start = node.lineno - 1
                end = getattr(node, "end_lineno", None)
                if end is None:
                    # Try to infer end by taking the max end_lineno/lineno of child nodes
                    child_lines = []
                    for child in ast.walk(node):
                        ln = getattr(child, "end_lineno", None) or getattr(child, "lineno", None)
                        if isinstance(ln, int):
                            child_lines.append(ln)
                    if child_lines:
                        end = max(child_lines)
                    else:
                        # Fallback: assume class is a single-line definition
                        end = start + 1
                # Ensure end is an int and within bounds for slicing
                if not isinstance(end, int):
                    end = start + 1
                end = min(end, len(code_lines))
                class_block = "\n".join(code_lines[start:end])
                classes[node.name] = {"code": class_block, "deps": set()}
                class_lines.update(range(start, end))

        # Collect the rest of the code (functions, main script, etc.)
        for i, line in enumerate(code_lines):
            stripped = line.strip()
            if stripped.startswith('import ') or stripped.startswith('from '):
                continue  # skip all imports
            if i in class_lines:
                continue  # skip class lines
            other_code_lines.append(line)

        other_code_lines.append('')  # separation between files

    # 3. Sort external imports
    sorted_imports = sorted(all_imports)

    # 4. Detect dependencies between classes via ast.walk
    class_names = set(classes.keys())
    for cls, info in classes.items():
        try:
            class_tree = ast.parse(info["code"])
        except SyntaxError:
            continue
        for node in ast.walk(class_tree):
            # Inheritance
            if isinstance(node, ast.ClassDef):
                for base in node.bases:
                    if isinstance(base, ast.Name) and base.id in class_names:
                        info["deps"].add(base.id)
            # Direct references to other classes
            elif isinstance(node, ast.Name):
                if node.id in class_names and node.id != cls:
                    info["deps"].add(node.id)

    # 5. Topological sorting of classes
    sorted_classes = []
    deps = {cls: set(info["deps"]) for cls, info in classes.items()}

    while deps:
        acyclic = False
        for cls, dset in list(deps.items()):
            dset.discard(cls)
            if not dset:
                acyclic = True
                sorted_classes.append(cls)
                del deps[cls]
                for other in list(deps):
                    deps[other].discard(cls)
        if not acyclic:  # cycle → append the rest as-is
            sorted_classes.extend(deps.keys())
            break

    # 6. Build the final code
    output = []

    # External imports
    if sorted_imports:
        output.extend(sorted_imports)
        output.append("")

    # Ordered classes
    for cls in sorted_classes:
        output.append(classes[cls]["code"])
        output.append("")

    # Other lines of code
    if other_code_lines:
        output.extend(other_code_lines)

    return "\n".join(output)

def write(filename, content):
    """
    Write the file and remove unnecessary blank lines. 

    Made by ChatGPT with few tweaks
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    with open(filename) as f_input:
        data = f_input.read().rstrip('\n')
        data = re.sub(r'\n\s*\n', '\n\n', data)
    with open(filename, 'w') as f_output:
        f_output.write(data)


if __name__ == "__main__":
    merged = merge_python_files(FOLDER)
    write(OUTPUT_FILE, merged)