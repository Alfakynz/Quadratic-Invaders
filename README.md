# Quadratic Invaders

Python, [Pyxel](https://github.com/kitao/pyxel)

## Documentation

Use `pydoc-markdown` to make the documentation

```sh
pip install pydoc-markdown
```

Then, run

```python
python3 documentation.py
```

To create a pdf, use the [Markdown PDF](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf) extension

## Game

#### Méthodes

- Augmenter ennemis en fonction du temps (dégat, vitesse, bouclier, PV, vitesse de tir)
- Game Over
- Collision

#### Interface

- Taille fenêtre (`x: int, y: int`)
- Compteur de points (temps resté en vie) (`points: int`)

## Personnage

#### Méthodes

- Recevoir dégats

#### Interface

- Couleur (`color: int`)
- PV (`hp: int`)
- Dégats (`damage: int`)
- Vitesse (`speed: int`)
- Bouclier (`shield: int`)
- Vitesse de tir (`fire_rate: int`)
- XP (`xp: int`)

## Joueur (Personnage)

#### Méthodes

- Se déplacer
- Tirer
- Ajout XP

## Balles (Joueur)

#### Méthodes

- Se déplacer
- Avancer
- Collision
- Attaquer

#### Interface

- Couleur (`color: int`)
- Dégat (`damage: int`)
- Vitesse (`speed: int`)
- Angle (`angle: float`)

## Ennemis (Personnage)

#### Méthodes

- Se déplacer vers le perso (pythagore)
- Collision
- Attaquer

## Formes

#### Interface

- Couleur (`color: int`)

## Upgrade

#### Méthodes

- Augmenter PV
- Augmenter attaque
- Augmenter bouclier
- Augmenter vitesse
- Augmenter vitesse de tir
- Augmenter prix (après achat)
- Vérifier nombre XP joueur

#### Interface

- Prix PV (`price_hp: int`)
- Prix attaque (`price_damage: int`)
- Prix bouclier (`price_shield: int`)
- Prix vitesse (`price_speed: int`)
- Prix vitesse de tir (`price_speed_shoot: int`)
- Prix compétences (`price_skills: int`)

## Skill

#### Interface

- Name (`name: str`)
- Description (`description: str`)
- Price (`price: int`)
- Amoount (`amount: int`)

## Si on a le temps

- Types d'ennemis
- Fenêtre qui bouge
- Compétences
- Boss
