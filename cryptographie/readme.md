# Utilisation du script `main.py`

Ce script permet d'effectuer des opérations de chiffrement et de déchiffrement sur un fichier en utilisant différentes méthodes telles que ROTN, Offset, AES, ASCII, et Substitution. Voici comment utiliser le script et les différents arguments acceptés :

## Prérequis

Avant d'utiliser ce script, assurez-vous d'avoir installé toutes les dépendances requises en exécutant la commande suivante dans votre terminal :

```
pip install -r requirements.txt
```

## Arguments acceptés

1. `-f` ou `--function`: Nom de la fonction à appeler.
   - Valeurs possibles : "ROTN", "Offset", "AES", "ASCII", "Substitution".

2. `-m` ou `--method`: Méthode à utiliser ("crypt" pour chiffrer, "decrypt" pour déchiffrer).
   - Valeurs possibles : "crypt", "decrypt".

3. `-u` ou `--input`: Nom du fichier d'entrée.
   - Exemple de valeur : "input.txt".

4. `-o` ou `--output`: Nom du fichier de sortie.
   - Exemple de valeur : "output.txt".

5. `-k` ou `--key`: Clé de chiffrement/déchiffrement.
   - Exemple de valeur : "7" (pour ROTN), "3" (pour Offset), clé AES en bytes, etc.

6. `-a` ou `--alphabet`: Alphabet personnalisé pour la substitution.
   - Exemple de valeur : "azertyuiopqsdfghjklmwxcvbn".

## Exemples d'utilisation

1. Chiffrer avec ROTN :
   ```
   python main.py -f ROTN -m crypt -u input.txt -o output.txt -k key -a your_alphabet
   ```

2. Déchiffrer avec ROTN :
   ```
   python main.py -f ROTN -m decrypt -u input.txt -o output.txt -k key -a your_alphabet
   ```

3. Chiffrer avec Offset :
   ```
   python main.py -f Offset -m crypt -u input.txt -o output.txt -k key
   ```

4. Déchiffrer avec Offset :
   ```
   python main.py -f Offset -m decrypt -u input.txt -o output.txt -k key
   ```

5. Chiffrer avec AES :
   ```
   python main.py -f AES -m crypt -u input.txt -o output.txt -k key
   ```

6. Déchiffrer avec AES :
   ```
   python main.py -f AES -m decrypt -u input.txt -o output.txt -k key
   ```

7. Chiffrer avec ASCII :
   ```
   python main.py -f ASCII -m crypt -u input.txt -o output.txt -k key
   ```

8. Déchiffrer avec ASCII :
   ```
   python main.py -f ASCII -m decrypt -u input.txt -o output.txt -k key
   ```

9. Chiffrer avec Substitution :
   ```
   python main.py -f Substitution -m crypt -u input.txt -o output.txt -k key
   ```

10. Déchiffrer avec Substitution :
    ```
    python main.py -f Substitution -m decrypt -u input.txt -o output.txt -k key
    ```