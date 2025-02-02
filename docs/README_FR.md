![Static Badge](https://img.shields.io/badge/python-%233776ab?logo=python&logoColor=white) ![Static Badge](https://img.shields.io/badge/MIT%20License-grey) ![Static Badge](https://img.shields.io/badge/bitcoin-%23ff9900?logo=bitcoin&logoColor=white)

# Mnemonic Shield

Ce projet propose une façon **innovante d'améliorer la sécurité du stockage d'une phrase mémonique BIP39 en la transformant en un sigil**, un symbole cryptographique unique.<br>La phrase mémonique est sécurisée en étant encodée dans une valeur combinée à l'aide d'un algorithme, et le résultat est représenté visuellement sous forme de sigil. **Cela ajoute une couche supplémentaire de sécurité**, car la phrase mémonique n'est pas stockée en texte brut, mais sous forme d'image.

Le sigil **peut être stocké sous différents formats**, tels que des images imprimées, une peinture ou d'autres supports créatifs, **ce qui rend extrêmement difficile pour les attaquants de reconnaître ou d'accéder à la phrase mémonique sous-jacente**.En cas de perte ou de compromission du sigil, **la phrase mémonique peut toujours être récupérée en décodant la valeur encodée, offrant ainsi une méthode discrète et sécurisée pour sauvegarder des informations sensibles**.

## Table de Matières

- [Table de Matières](#table-de-matieres)
- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Sécurité et Éthique](sécurité-et-éthique)
- [Comparaison](#comparaison)
- [Benchmarks](#benchmarks)
- [Roadmap](#roadmap)
- [Arborescence](#arborescence)
- [Contributions](#contributions)
- [Soutenir le Projet](#soutenir-le-projet)
- [License](#license)
- [Auteur](#Auteur)

## Fonctionnalités

- 🌀 **Transformation de Phrase Mnémonique en Sigil**<br>_Convertit une phrase mnémonique en un sigil unique à l'aide de transformations mathématiques._

- 🔒 **Encodage Sécurisé avec un Algorithme**<br>_La phrase mnémonique est d'abord convertie en indices numériques à partir d'une liste de mots BIP39. Ces indices sont ensuite encodés en une valeur combinée à l'aide de l'algorithme base2048._

- 🖼️ **Visualisation sous forme d'Image**<br>_Le sigil est généré sous forme d'image vectorielle, affichant un design unique basé sur la valeur encodée, rendant plus difficile pour les attaquants de détecter ou de compromettre la phrase mnémonique sous-jacente._

- 🔄 **Décodage et Récupération de la Phrase Mnémonique**<br>_Permet de récupérer la phrase mnémonique d'origine en décodant la valeur combinée encodée, à condition que le nombre nécessaire d'indices soit fourni._

- 💾 **Stockage et Gestion des Sigils**<br>_Les sigils sont enregistrés dans un dossier dédié et peuvent être facilement stockés sous forme d'images, imprimés ou utilisés dans d'autres formats créatifs comme des peintures ou objets._

- 📝 **Menu Interactif**<br>_L'interface utilisateur permet de choisir entre deux options principales : `créer un sigil à partir d'une phrase mnémonique` ou `récupérer la phrase mnémonique à partir d'une valeur encodée`._

- ✅ **Validation de la Phrase Mnémonique**<br>_Vérifie que chaque mot de la phrase mnémonique existe dans la liste de mots BIP39, avec des messages d'erreur informatifs en cas de mots manquants._

- 🔗**Intégration Facile**<br>_Le code est conçu pour être facilement adaptable à différents cas d'utilisation et peut être modifié ou étendu pour s'intégrer à d'autres systèmes ou interfaces._

## Prérequis

- `Python 3.11`

- Bibliothèques Python nécessaires (_voir [Installation](#installation)_)
  - `matplotlib`
  - `numpy`
  - `shadePy`

## Installation

Assurez-vous d’avoir [Python](https://www.python.org/downloads/) installé sur votre système avant d’exécuter la commande d’installation.

1. Clonez ce dépôt

   ```bash
   git clone https://github.com/0x414854/Mnemonic_Shield.git
   ```

   ```bash
   cd Mnemonic_Shield

   ```

2. Installez les dépendances

   ```bash
   pip install -r requirements.txt
   ```

3. Préparez la liste de mots BIP39
   - Assurez-vous d’avoir le fichier de liste de mots BIP39 situé à `./utils/wordsBIP39.txt`.
   - _Vous pouvez obtenir le fichier [ici](https://github.com/0x414854/Words_BIP39/blob/main/wordsBIP39.txt)._

## Utilisation

- Exécuter le script

  ```bash
  python3 mnemonicShield.py
  ```

- Menu interactif

- 🔹 `Create a Sigil`

  - **Entrez votre phrase mnémonique BIP39.** (_12 ou 24 mots séparés par des espaces_)
  - **Le script convertit la phrase en une valeur combinée unique.**
  - **Un sigil est généré et enregistré sous forme d’image dans le dossier `sigils/`.**

  🖊️ Exemple avec une phrase mnémonique de 12 mots

  ```bash
  foster file unknown pluck economy end bird pistol awesome dentist move crucia
  ```

  📤 Output

  ```bash
  Indices : [737, 690, 1904, 1334, 562, 589, 181, 1324, 133, 469, 1159, 420]
  Encoded combined value : 1957519189511453243541897867745737060771
  Number Mapping for the sigil : [1, 9, 5, 7, 5, 1, 9, 1, 8, 9, 5, 1, 1, 4, 5, 3, 2, 4, 3, 5, 4, 1, 8, 9, 7, 8, 6, 7, 7, 4, 5, 7, 3, 7, 0, 6, 0, 7, 7, 1]
  ```

  🖼️ Le fichier `sigil.png` est créé dans le dossier `sigils/`.

  ![sigil1](https://github.com/user-attachments/assets/ca614002-9649-4b74-8114-8830c954b582)

  🖊️ Exemple avec une phrase mnémonique de 24 mots

  ```bash
  vital repair dizzy traffic library brief shell often expand south burst foam tissue twist attitude cupboard vapor country today return marine can play brave
  ```

  📤 Output

  ```bash
  Indices : [1961, 1461, 514, 1847, 1033, 224, 1580, 1230, 642, 1666, 247, 721, 1815, 1885, 118, 431, 1932, 393, 1819, 1474, 1089, 264, 1331, 219]
  Encoded combined value : 28379382023410064612010001521199486933878242917918893669086206599498889245069530
  Number Mapping for the sigil : [2, 8, 3, 7, 9, 3, 8, 2, 0, 2, 3, 4, 1, 0, 0, 6, 4, 6, 1, 2, 0, 1, 0, 0, 0, 1, 5, 2, 1, 1, 9, 9, 4, 8, 6, 9, 3, 3, 8, 7, 8, 2, 4, 2, 9, 1, 7, 9, 1, 8, 8, 9, 3, 6, 6, 9, 0, 8, 6, 2, 0, 6, 5, 9, 9, 4, 9, 8, 8, 8, 9, 2, 4, 5, 0, 6, 9, 5, 3, 0]
  ```

  🖼️ Le fichier `sigil.png` est créé dans le dossier `sigils/`.

  ![sigil](https://github.com/user-attachments/assets/05ca90ff-da32-4618-8d06-a168437effa4)

- 🔹 `Récupérer une Phrase Mnémonique`

  - **Entrez la valeur combinée encodée générée lors de la création du sigil.**
  - **Spécifiez le nombre d’indices nécessaires pour reconstruire la phrase mnémonique.**
  - **Le script récupère et affiche la phrase mnémonique originale.**

  🖊️ Exemple avec une phrase mnémonique de 12 mots

  ```bash
  Enter the encoded combined value 1957519189511453243541897867745737060771
  Enter the number of indices to reconstruct the phrase : 12
  ```

  📤 Output

  ```bash
  Reconstructed indices : [737, 690, 1904, 1334, 562, 589, 181, 1324, 133, 469, 1159, 420]
  Reconstructed mnemonic phrase : foster file unknown pluck economy end bird pistol awesome dentist move crucial
  ```

  🖊️ Exemple avec une phrase mnémonique de 24 mots

  ```bash
  Enter the encoded combined value : 28379382023410064612010001521199486933878242917918893669086206599498889245069530
  Enter the number of indices to reconstruct the phrase : 24
  ```

  📤 Output

  ```bash
  Reconstructed indices : [1961, 1461, 514, 1847, 1033, 224, 1580, 1230, 642, 1666, 247, 721, 1815, 1885, 118, 431, 1932, 393, 1819, 1474, 1089, 264, 1331, 219]
  Reconstructed mnemonic phrase : vital repair dizzy traffic library brief shell often expand south burst foam tissue twist attitude cupboard vapor country today return marine can play brave
  ```

## Sécurité et Éthique

Assurer la sécurité et l'utilisation éthique de ce projet est une priorité absolue. Vous trouverez ci-dessous les principales considérations pour une mise en œuvre sûre et responsable :

### 🔒 **Traitement Local Uniquement**

- Ce projet **ne transmet ni ne stocke aucune donnée mnémonique en ligne**.
- Tous les calculs, l’encodage et la génération d’images sont effectués localement sur votre appareil, garantissant que les informations sensibles ne quittent jamais votre machine.

### 🛡️ **Confidentialité des Données**

- La phrase mnémonique est uniquement traitée en mémoire et **n'est jamais stockée en texte clair**.
- La représentation sous forme de sigil offre une **alternative discrète** au stockage traditionnel des phrases mnémoniques, **réduisant ainsi le risque d’accès non autorisé**.

### 📁 **Pratiques de Stockage Sécurisé**

- **L’image du sigil** et **la valeur combinée encodée** servent d’alternative au stockage de la phrase mnémonique en clair.
- Il est de la responsabilité de l’utilisateur de stocker le sigil et la valeur combinée en toute sécurité, par exemple :
  - **Sur un appareil hors ligne**
  - **Sous forme d’image imprimée dans un endroit sécurisé**

### 🧑‍⚖️ **Considérations Éthiques**

- This project is designed for **personal security and privacy enhancement**.
- Les utilisateurs ne doivent **jamais utiliser cet outil à des fins illicites** ou tenter de **récupérer des phrases mnémoniques qui ne leur appartiennent pas**.
  Comme pour toute méthode de sécurité, **une protection en plusieurs couches est recommandée**. Ne vous fiez pas uniquement à une seule méthode de sauvegarde.

En suivant ces bonnes pratiques de sécurité, les utilisateurs peuvent **améliorer leur stockage de mnémonique** tout en protégeant efficacement leurs données sensibles.

## Comparaison

Ce projet offre une alternative discrète pour stocker les phrases mnémoniques BIP39 en les encodant en **un nombre unique** et en générant un **sigil** correspondant. Vous trouverez ci-dessous une comparaison entre cette approche et la méthode traditionnelle.

### ✅ Avantages de l'Encodage en Sigil

- **🔒 Sécurité Renforcée**: La phrase mnémonique n'est pas directement identifiable comme une phrase mnemonic BIP39.
- **🕵️ Discrétion Accrue**: Un sigil apparaît comme un dessin abstrait, rendant la récupération moins évidente pour un attaquant.
- **📁 Stockage Numérique ou Physique**: Peut être sauvegardé sous forme d’image ou gravé sur un support physique.

### ❌ Inconvénients de l'Encodage en Sigil

- **⚠️ Dépendance au Code**: La phrase ne peut pas être récupérée sans exécuter le programme.
- **💾 Nécessite un Fichier BIP39**: La récupération dépend du dictionnaire exact des mots BIP39.
- **📉 Moins Universel**: Un portefeuille crypto standard ne reconnaîtra pas directement ce format.
- **🛠️ Risque de Perte**: Si le code source et le sigil sont perdus, la phrase devient irrécupérable.

### 🔄 Comparaison avec une Phrase Mnémonique BIP39 Standard

| Critère                 | Encodage en Sigil                          | Phrase Mnémonique BIP39                        |
| ----------------------- | ------------------------------------------ | ---------------------------------------------- |
| **Sécurité** 🔒         | ✅ Chiffrement indirect                    | ❌ Facilement reconnaissable                   |
| **Discrétion** 🕵️       | ✅ Sigil non identifiable                  | ❌ Ressemble à une phrase secrète              |
| **Facilité d’Usage** ⚙️ | ❌ Dépend d’un script                      | ✅ Universel et portable                       |
| **Portabilité** 🛠️      | ✅ Peut être gravé ou stocké numériquement | ❌ Peut être volé s'il n'est pas bien protégé  |
| **Risque de Perte** ⚠️  | ❌ Nécessite à la fois le code et le sigil | ✅ Peut être écrit sur papier                  |
| **Récupération** 🔄     | ❌ Requiert un script et un fichier BIP39  | ✅ Directement utilisable dans un portefeuille |

### 🚀 Recommandation

- Utilisez **l’encodage en sigil** comme **méthode de sauvegarde discrète**.
- Conservez une **copie papier de la phrase BIP39 dans un endroit sécurisé** pour éviter toute perte accidentelle.
- Ajoutez **un mot de passe ou une clé supplémentaire** pour renforcer la sécurité en cas de découverte du sigil.

## Benchmarks

Actuellement, aucun benchmark officiel n'a été réalisé sur la vitesse d'exécution ou l'utilisation de la mémoire du script. Cependant, il est conçu pour être léger, et les opérations impliquées (notamment la génération du sigil) devraient s'exécuter efficacement sur la plupart des ordinateurs modernes.

## Roadmap

- [ ] `Options d’exportation` : _Permettre aux utilisateurs de sauvegarder le sigil dans d'autres formats comme `SVG` ou `PDF`._
- ✅ `Ajouter une option pour enregistrer le sigil avec ou sans la valeur combinée`

## Arborescence

.
<br>├── .gitignore
<br>├── LICENSE
<br>├── README.md
<br>├── mnemonicShield.py
<br>├── requirements.txt
<br>├── 📁 utils/
<br>&nbsp;&nbsp;&nbsp;&nbsp;└── wordsBIP39.txt
<br>└── 📁 (sigils)/
<br>&nbsp;&nbsp;&nbsp;&nbsp; └── (sigil.png)

## Contributions

N'hésitez pas à soumettre des issues et des pull requests pour améliorer ce projet !

## Soutenir le Projet

**⭐ Laissez une étoile sur GitHub ⭐**

**Votre soutien fait toute la différence !** Ce projet est maintenu grâce à l'énergie, le temps et la passion de ses contributeurs.<br>Si vous appréciez ce projet ou souhaitez aider à soutenir son développement, **vous pouvez faire un don**.

### Pourquoi faire un don ? ? 🫶

- Aider à couvrir les coûts de développement et de matériel.
- Contribuer à l'ajout de nouvelles fonctionnalités et améliorations.
- Soutenir un projet open-source pour le maintenir gratuit et accessible à tous.
- Permettre l'achat de matériel plus performant pour créer un pool de calcul dédié à la résolution de puzzles Bitcoin.

### Portefeuilles de Cryptomonnaies 🪙

Vous pouvez faire un don en utilisant les adresses de cryptomonnaies suivantes :

- **Bitcoin (BTC)** : `bc1q6n3ufauzjqgxztkklj3734cp0f7evqq3djh4ne`
- **Ethereum (ETH)** : `0x24800123e8D51F1d596c6Abe4B5DB5A10837Fe8e`
- **Bittensor (TAO)** : `5CrG7bKratZVocnxj66FF23AMVvqKHf7RSHfz49csEtJ2CuG`
- **Dogecoin (DOGE)** : `DJQnasX39Unat3vkmyBMgp4H6Kfd4wFumF`
- **Solana (SOL)** : `Gj9JkpFqdSabag8RiiNTmLaCiZrcxYa6pc4y599vft15`

#### **USDT (Tether)**

- **Binance Smart Chain (BEP-20)** : `0x24800123e8D51F1d596c6Abe4B5DB5A10837Fe8e`
- **Ethereum (ERC-20)** : `0x24800123e8D51F1d596c6Abe4B5DB5A10837Fe8e`
- **Tron (TRC-20)** : `THHcEQ8zG3ZnUXoHdBmCdpZ3AAqhoDbMpW`
- **Solana (SPL)** : `Gj9JkpFqdSabag8RiiNTmLaCiZrcxYa6pc4y599vft15`

#### **USDC (USD Coin)**

- **Binance Smart Chain (BEP-20)**: `0x24800123e8D51F1d596c6Abe4B5DB5A10837Fe8e`
- **Ethereum (ERC-20)**: `0x24800123e8D51F1d596c6Abe4B5DB5A10837Fe8e`
- **Solana (SPL)**: `Gj9JkpFqdSabag8RiiNTmLaCiZrcxYa6pc4y599vft15`

### 💬 Un Grand Merci

Un immense merci pour votre générosité. Votre soutien signifie énormément pour nous et nous motive à continuer d'améliorer ce projet. 🙏

**➡️ Passez à l'action dès maintenant ! Chaque contribution, grande ou petite, a un impact considérable.**

## License

Ce projet est sous licence **[MIT License](https://github.com/0x414854/Mnemonic_Shield/blob/main/LICENSE)**.

## Auteur

[**0x414854**](https://github.com/0x414854)
