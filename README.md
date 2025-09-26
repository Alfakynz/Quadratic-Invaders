# Window Kill

Python, [Pyxel](https://github.com/kitao/pyxel)

## Game

#### Méthodes

- Augmenter ennemis en fonction du temps (dégat, vitesse, bouclier, PV, vitesse de tir)

#### Interface

- Taille fenêtre (`x: int, y: int`)
- Compteur de points (temps resté en vie) (`points: int`)

## Presonnage

#### Méthodes

- Se déplacer
- Recevoir dégats

#### Interface

- Couleur (`r: int, g: int, b: int`)
- Forme (`shape: str`)
- PV (`hp: int`)
- Dégats (`damage: int`)
- Vitesse (`speed: int`)
- Bouclier (`shield: int`)
- Vitesse de tir (`speed_shoot: int`)

## Main Character

#### Méthodes

- Tirer

#### Interface

- XP (`xp: int`)

## Ennemis (Personnage)

#### Méthodes

- Se déplacer vers le perso (pythagore)
- Collision
- Attaquer

#### Interface

- XP (`xp: int`)

## Tir

#### Méthodes

- Avancer
- Collision
- Attaquer

#### Interface

- Couleur (`r: int, g: int, b: int`)
- Forme (`shape: str`)
- Dégat (`damage: int`)
- Vitesse (`speed: int`)

## Formes

#### Interface

- Couleur (`r: int, g: int, b: int`)

## Upgrade

#### Méthodes

- Augmenter PV
- Augmenter attaque
- Ajouter une compétence
- Ajouter bouclier
- Ajouter vitesse
- Vérifier nombre XP joueur
