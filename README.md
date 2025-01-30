![Static Badge](https://img.shields.io/badge/python-%233776ab?logo=python&logoColor=white) ![Static Badge](https://img.shields.io/badge/MIT%20License-grey) ![Static Badge](https://img.shields.io/badge/bitcoin-%23ff9900?logo=bitcoin&logoColor=white)

# Mnemonic Shield

This project offers an **innovative way to enhance the security of storing a BIP39 mnemonic phrase** by transforming it into a sigil, a unique cryptographic symbol.<br>The mnemonic phrase is securely encoded into a combined value using an algorithm, and the result is visually represented as a sigil. **This adds an additional layer of security**, as the mnemonic is not stored in plain text but rather as an image.

The sigil **can be stored in various formats**, such as printed images, a painting, or other creative mediums, **making it extremely difficult for attackers to recognize or access the underlying mnemonic**.<br>In the event that the sigil is lost or compromised, **the mnemonic phrase can still be recovered by decoding the encoded value, providing a secure and discreet method for backing up sensitive information.**

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Security and Ethics](security-and-ethics)
- [Comparison : Sigil Encoding vs. BIP39 Mnemonic Phrase](comparison-:-sigil-encoding-vs.-bip39-mnemonic-phrase)
- [Benchmarks](#benchmarks)
- [Roadmap](#roadmap)
- [Tree Directory](#tree-directory)
- [Contributions](#contributions)
- [Support the Project](#support-the-project)
- [License](#license)
- [Author](#author)

## Features

- 🌀 **Mnemonic Phrase to Sigil Transformation**<br>_Converts a mnemonic phrase into a unique sigil using mathematical transformations._

- 🔒 **Secure Encoding with an Algorithm**<br>_The mnemonic phrase is first converted into numerical indices from a BIP39 word list. These indices are then encoded into a combined value using the base2048 algorithm._

- 🖼️ **Visualization as an Image**<br>_The sigil is generated as a vector image, displaying a unique design based on the encoded value, making it harder for attackers to detect or compromise the underlying mnemonic._

- 🔄 **Mnemonic Phrase Decoding and Recovery**<br>_Allows for the recovery of the original mnemonic phrase by decoding the encoded combined value, as long as the necessary number of indices is provided._

- 💾 **Sigil Storage and Management**<br>_Sigils are saved in a dedicated folder and can be easily stored as images, printed, or used in other creative formats like paintings or objects._

- 📝 **Interactive Menu** <br>_The user interface allows for choosing between two main options : `creating a sigil from a mnemonic phrase` or `recovering the mnemonic phrase from an encoded value`._

- ✅ **Mnemonic Phrase Validation**<br>_Verifies that each word in the mnemonic phrase exists in the BIP39 word list, with informative error messages in case of missing words._

- 🔗**Easy Integration**<br>_The code is designed to be easily adaptable for different use cases and can be modified or extended to integrate with other systems or interfaces._

## Prerequisites

- `Python 3.11`

- Required Python libraries (_see [Installation](#installation)_)
  - `matplotlib`
  - `numpy`
  - `shadePy`

## Installation

Make sure you have [Python](https://www.python.org/downloads/) installed on your system before running the install command.

1. Clone this repository

   ```bash
   git clone https://github.com/0x414854/Mnemonic_Shield.git
   ```

   ```bash
   cd Mnemonic_Shield

   ```

2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

3. Prepare BIP39 word list
   - Make sure you have the BIP39 word list file located at `./utils/wordsBIP39.txt`.
   - _You can obtain the file from [here](https://github.com/0x414854/Words_BIP39/blob/main/wordsBIP39.txt)._

## Usage

- Run the script

  ```bash
  python3 mnemonicShield.py
  ```

- Interactive Menu

- 🔹 `Create a Sigil`

  - **Enter your BIP39 mnemonic phrase.** (_12 or 24 words separated by spaces_)
  - **The script converts the phrase into a unique combined value.**
  - **A sigil is generated and saved as an image in the `sigils/` folder.**

  🖊️ Example with a 12-word mnemonic phrase

  ```bash
  chair symptom verify cage record shadow annual forest taxi solid purity picture
  ```

  📤 Output

  ```bash
  Indices : [737, 690, 1904, 1334, 562, 589, 181, 1324, 133, 469, 1159, 420]
  Encoded combined value : 1957519189511453243541897867745737060771
  Number Mapping for the sigil : [1, 9, 5, 7, 5, 1, 9, 1, 8, 9, 5, 1, 1, 4, 5, 3, 2, 4, 3, 5, 4, 1, 8, 9, 7, 8, 6, 7, 7, 4, 5, 7, 3, 7, 0, 6, 0, 7, 7, 1]
  ```

  🖼️ `sigil.png` file is created in the `sigils/` folder.

  ![sigil1](https://github.com/user-attachments/assets/ca614002-9649-4b74-8114-8830c954b582)

  🖊️ Example with a 24-word mnemonic phrase

  ```bash
  vital repair dizzy traffic library brief shell often expand south burst foam tissue twist attitude cupboard vapor country today return marine can play brave
  ```

  📤 Output

  ```bash
  Indices : [1961, 1461, 514, 1847, 1033, 224, 1580, 1230, 642, 1666, 247, 721, 1815, 1885, 118, 431, 1932, 393, 1819, 1474, 1089, 264, 1331, 219]
  Encoded combined value : 28379382023410064612010001521199486933878242917918893669086206599498889245069530
  Number Mapping for the sigil : [2, 8, 3, 7, 9, 3, 8, 2, 0, 2, 3, 4, 1, 0, 0, 6, 4, 6, 1, 2, 0, 1, 0, 0, 0, 1, 5, 2, 1, 1, 9, 9, 4, 8, 6, 9, 3, 3, 8, 7, 8, 2, 4, 2, 9, 1, 7, 9, 1, 8, 8, 9, 3, 6, 6, 9, 0, 8, 6, 2, 0, 6, 5, 9, 9, 4, 9, 8, 8, 8, 9, 2, 4, 5, 0, 6, 9, 5, 3, 0]
  ```

  🖼️ `sigil.png` file is created in the `sigils/` folder.

  ![sigil](https://github.com/user-attachments/assets/05ca90ff-da32-4618-8d06-a168437effa4)

- 🔹 `Recover a Mnemonic Phrase`

  - **Enter the encoded combined value generated when creating the sigil.**
  - **Specify the number of indices needed to reconstruct the mnemonic phrase.**
  - **The script retrieves and displays the original mnemonic phrase.**

  🖊️ Example with a 12-word mnemonic phrase

  ```bash
  Enter the encoded combined value 1957519189511453243541897867745737060771
  Enter the number of indices to reconstruct the phrase : 12
  ```

  📤 Output

  ```bash
  Reconstructed indices : [737, 690, 1904, 1334, 562, 589, 181, 1324, 133, 469, 1159, 420]
  Reconstructed mnemonic phrase : foster file unknown pluck economy end bird pistol awesome dentist move crucial
  ```

  🖊️ Example with a 24-word mnemonic phrase

  ```bash
  Enter the encoded combined value : 28379382023410064612010001521199486933878242917918893669086206599498889245069530
  Enter the number of indices to reconstruct the phrase : 24
  ```

  📤 Output

  ```bash
  Reconstructed indices : [1961, 1461, 514, 1847, 1033, 224, 1580, 1230, 642, 1666, 247, 721, 1815, 1885, 118, 431, 1932, 393, 1819, 1474, 1089, 264, 1331, 219]
  Reconstructed mnemonic phrase : vital repair dizzy traffic library brief shell often expand south burst foam tissue twist attitude cupboard vapor country today return marine can play brave
  ```

## Security and Ethics

Ensuring the security and ethical use of this project is a top priority. Below are key considerations regarding its safe and responsible implementation :

### 🔒 **Local-Only Processing**

- This project **does not** transmit or **store any mnemonic data online**.
- All computations, encoding, and image generation are performed locally on your device, ensuring that sensitive information never leaves your machine.

### 🛡️ **Data Privacy**

- The mnemonic phrase is only processed in memory and n**ever stored in plaintext**.
- The sigil representation provides a **discreet alternative** to traditional mnemonic storage, **reducing the risk of unauthorized access**.

### 📁 **Secure Storage Practices**

- The **sigil image** and the **encoded combined** value serve as an alternative to storing the mnemonic in plaintext.
- It is the user's responsibility to store the sigil and the combined value securely, such as:
  - **On an offline device**
  - **As a printed image in a secure location**

### 🧑‍⚖️ **Ethical Considerations**

- This project is designed for **personal security and privacy enhancement**.
- Users should **never use this tool for illicit purposes** or attempt to **recover mnemonics that do not belong to them**.
  As with any security method, **layered protection is recommended**. Do not rely solely on one backup method.

By following these security best practices, users can **enhance their mnemonic storage** while keeping their sensitive data protected.

## Comparison : Sigil Encoding vs. BIP39 Mnemonic Phrase

This project offers a discreet alternative for storing BIP39 mnemonic phrases by encoding them into a **unique number** and generating a corresponding **sigil**. Below is a comparison between this approach and the traditional method.

### ✅ Advantages of Sigil Encoding

- **🔒 Enhanced Security**: The seed phrase is not directly identifiable as a BIP39 mnemonic.
- **🕵️ Increased Discretion**: A sigil appears as an abstract drawing, making recovery less obvious for an attacker.
- **📁 Digital or Physical Storage**: Can be saved as an image or engraved onto a physical medium.
- **🔢 Reduced Storage Space**: The phrase is transformed into a single, more compact number.

### ❌ Disadvantages of Sigil Encoding

- **⚠️ Code Dependency**: The phrase cannot be recovered without running the program.
- **💾 Requires a BIP39 File**: Recovery depends on the exact BIP39 word dictionary.
- **📉 Less Universal**: A standard crypto wallet will not directly recognize this format.
- **🛠️ Risk of Loss**: If the source code and sigil are lost, the phrase becomes unrecoverable.

### 🔄 Comparison with a Standard BIP39 Mnemonic Phrase

| Criterion           | Sigil Encoding                         | BIP39 Mnemonic Phrase                  |
| ------------------- | -------------------------------------- | -------------------------------------- |
| **Security** 🔒     | ✅ Indirect encryption                 | ❌ Easily recognizable                 |
| **Discretion** 🕵️   | ✅ Unrecognizable sigil                | ❌ Looks like a seed phrase            |
| **Ease of Use** ⚙️  | ❌ Script-dependent                    | ✅ Universal and portable              |
| **Portability** 🛠️  | ✅ Can be engraved or stored digitally | ❌ Can be stolen if not well protected |
| **Risk of Loss** ⚠️ | ❌ Requires both code and sigil        | ✅ Can be written on paper             |
| **Recovery** 🔄     | ❌ Needs script and BIP39 base file    | ✅ Directly usable in a wallet         |

### 🚀 Recommendation

- Use **sigil encoding** as a **discreet backup method**.
- Keep a **paper copy of the BIP39 phrase** in a secure place to avoid accidental loss.
- Add a **password or an extra key** to enhance security in case the sigil is discovered.

## Benchmarks

Currently, no official benchmarks have been performed on the execution speed or memory usage of the script. However, it is designed to be lightweight, and the operations involved (especially plotting) should run efficiently on most modern computers.

## Roadmap

- [ ] `Export options` : _Allow users to save the sigil in other formats like `SVG` or `PDF`._

## Tree Directory

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

Feel free to submit issues and pull requests to improve this project !

## Support the Project

**⭐ Giving it a star on GitHub ⭐**

**Your support makes a huge difference !** This project is maintained with the energy, time, and passion of its contributors.
<br>If you enjoy this project or want to help sustain its development, **consider making a donation**.

### Why Donate ? 🫶

- Help cover development and hardware costs.
- Contribute to new features and improvements.
- Support an open-source project to keep it free and accessible to everyone.
- Enable the purchase of better hardware to create a computational pool for solving bitcoin puzzles.

### Cryptocurrency Wallets 🪙

You can donate using the following cryptocurrency addresses:

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

### 💬 A Big Thank You

Thank you so much for your generosity. Your support truly means the world to us and motivates us to keep improving this project. 🙏

**➡️ Take action now ! Every contribution, big or small, makes a huge impact.**

## License

This project is licensed under the **[MIT License](https://github.com/0x414854/Mnemonic_Shield/blob/main/LICENSE)**.

## Author

[**0x414854**](https://github.com/0x414854)
