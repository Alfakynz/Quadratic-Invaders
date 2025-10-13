# Window Kill

Python, [Pyxel](https://github.com/kitao/pyxel)

## Game

#### Méthodes

- Augmenter ennemis en fonction du temps (dégat, vitesse, bouclier, PV, vitesse de tir)
- Game Over
- Collision

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
- XP (`xp: int`)

## Main Character (Personnage)

#### Méthodes

- Tirer
- Ajout XP

## Tir (Main Character)

#### Méthodes

- Avancer
- Collision
- Attaquer

#### Interface

- Couleur (`r: int, g: int, b: int`)
- Forme (`shape: str`)
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

- Couleur (`r: int, g: int, b: int`)

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

## Si on a le temps

- Types d'ennemis
- Fenêtre qui bouge
- Compétences
- Boss
