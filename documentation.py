import subprocess
import re
from pathlib import Path

# File paths
onefile_path = Path("onefile.py")
doc_path = Path("documentation.md")

# 1. Run onefile.py
subprocess.run(["python3", str(onefile_path)], check=True)

# 2. Generate documentation with pydoc-markdown
with open(doc_path, "w") as f:
    subprocess.run(["pydoc-markdown", "-I", str(Path.cwd())], stdout=f, check=True)

# 3. Read the content of markdown file
with open(doc_path, "r") as f:
    content = f.read()

# 4. Remove everything before "# quadratic-invaders"
main_index = content.find("# quadratic-invaders")
if main_index != -1:
    content = content[main_index:]

# 5. Remove all <a ...></a> tags
content = re.sub(r'<a[^>]*>.*?</a>', '', content, flags=re.DOTALL)

# 6. Remove all unnecessary lines
content = content.rstrip('\n')
content = re.sub(r'\n\s*\n', '\n\n', content)

# 7. Write the final result
with open(doc_path, "w") as f:
    f.write(content)

print("Documentation updated successfully!")