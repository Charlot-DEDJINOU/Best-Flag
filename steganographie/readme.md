# Utilisation du script Python pour la stéganographie d'images

Ce script Python permet de cacher et extraire des données dans/from des images en utilisant la stéganographie. Il offre les fonctionnalités suivantes :

- Cacher une image dans une autre image (`hide_image`)
- Extraire une image cachée d'une image hôte (`extract_hidden_image`)
- Cacher du texte dans une image (`hide_text`)
- Extraire du texte d'une image cachée (`extract_text`)

## Prérequis

Avant d'utiliser ce script, assurez-vous d'avoir installé toutes les dépendances requises en exécutant la commande suivante dans votre terminal :

```
pip install -r requirements.txt
```

## Utilisation

1. Ouvrez un terminal ou une invite de commandes.
2. Accédez au répertoire où se trouve le script Python (`main.py`).

### Options disponibles

- `-a`, `--action` : Action à effectuer. Choix disponibles : `hide_image`, `extract_hidden_image`, `hide_text`, `extract_text`.
- `-t`, `--text` : Chemin vers le fichier texte à cacher (utilisé avec l'action `hide_text`).
- `-h`, `--image_to_image` : Chemin vers l'image à cacher (utilisé avec l'action `hide_image`).
- `-H`, `--host_image` : Chemin vers l'image hôte dans laquelle cacher l'image ou extraire le texte.
- `-o`, `--output` : Chemin vers le fichier de sortie pour enregistrer l'image cachée ou le texte extrait.

### Exemples d'utilisation

- Cacher une image dans une autre image :
  ```
  python main.py -a hide_image -sh path/to/image_to_hide.jpg -th path/to/host_image.jpg -o path/to/output_image.png
  ```

- Extraire une image cachée d'une image hôte :
  ```
  python main.py -a extract_hidden_image -th path/to/host_image_with_hidden_image.png -o path/to/extracted_image.jpg
  ```

- Cacher du texte dans une image :
  ```
  python main.py -a hide_text -t path/to/text_to_hide.txt -th path/to/host_image.jpg -o path/to/output_image.png
  ```

- Extraire du texte d'une image cachée :
  ```
  python main.py -a extract_text -th path/to/host_image_with_hidden_text.png -o path/to/extracted_text.txt
  ```

...et ainsi de suite pour d'autres actions disponibles.

## Contributions

Les contributions sont les bienvenues ! N'hésitez pas à soumettre des problèmes, des suggestions ou des demandes de fonctionnalités.

## Auteur

- [Charlot DEDJINOU](https://charlot-dedjinou.vercel.app) - Développeur principal