🔐 Ransomware Simulation Script
A Real-World Ransomware Simulation for Educational Purposes

⚠️ Disclaimer:
This script is intended solely for educational purposes. Unauthorized use of ransomware, including encrypting files on systems without permission, is illegal and unethical. Always ensure you have explicit authorization before running encryption tools on any system.

📋 Overview
The Ransomware Simulation Script replicates core elements of file encryption and decryption, simulating how ransomware operates. Built using Python's Fernet encryption from the cryptography library, it serves both as an educational tool and a practical demonstration of encryption mechanics.

Key Features:
🔑 Automatic Key Generation and Secure Key Storage.
🔒 File Encryption: Selective or full encryption of files in a directory.
📂 Custom File-Type Targeting: Encrypt specific file formats.
📝 Detailed Error Logging: Logs any encryption/decryption errors.
🛡️ Secure Key Deletion: Safely overwrites and deletes the key file after decryption.
⏱️ Fast Processing: Efficient file handling and encryption/decryption times.

🚀 Getting Started

1. Clone the Repository

<hr>

git clone https://github.com/tejasbargujepatil/RansomwareSimulator.git

<hr> 

**cd  < Repository Folder Name >**

<hr>

3. Install Dependencies
The script automatically installs missing dependencies during runtime, but you can manually install the required libraries upfront:


<hr>

**pip install cryptography**

<hr>

3. Run the Script
Execute the script:



**python RansomwareSimulator.py**

<hr>

🛠️ How to Use
Provide Folder Path:
When prompted, enter the path to the folder containing files for encryption/decryption.

<hr>

**Enter the path to the folder to simulate attack: /path/to/folder**

<hr>

Select File Types:
Choose whether to encrypt all files or target specific file types (e.g., .txt, .jpg).

<hr>


**Do you want to encrypt all files? (yes/no): no**  
**Enter file types to encrypt (e.g., .txt .jpg): .txt .pdf**

<hr>

Encryption Process:
The script generates an encryption key and encrypts the specified files.

Decryption Process:
After 30 seconds, the script decrypts the files using the same key.

Key Deletion:
Once decryption is completed, the key is securely deleted to prevent unauthorized access.

🔑 Key Features
📦 1. Automatic Dependency Handling
The script installs required dependencies at runtime, ensuring smooth execution. Alternatively, you can manually install them using:


<hr>


**pip install cryptography**

<hr>


🔒 2. File Encryption & Decryption
Targeted Encryption: Encrypt specific file types.
Full Encryption: Encrypt all files in a directory.
📝 3. Error Handling and Logging
Issues encountered during encryption/decryption are logged in error_log.txt for troubleshooting.

🗝️ 4. Secure Key Management
The encryption key is securely deleted using a method that overwrites the key file with random data before deletion, ensuring it cannot be recovered.

💡 Example Workflow

<hr>



**Enter the path to the folder to simulate attack: /path/to/folder**  
**Do you want to encrypt all files? (yes/no): no**  *(Type No To Encrypt All Files)*
**Enter file types to encrypt (e.g., .txt .jpg): .txt** *(Type Extensions Of Files To Encrypt Specific Files)*

<hr>


**Encryption Step: Encrypts .txt files and logs any issues.
Decryption Step: Files are decrypted after 30 seconds.
Key Management: The encryption key is securely deleted post-decryption.
🛡️ Security and Safety
Secure Deletion: The encryption key is securely overwritten and deleted after use.
Detailed Logs: All operations are logged, with errors saved in error_log.txt.**
<hr>

**📂 File Structure**



**.
├── ransomware_simulation.py     # Main ransomware simulation script
├── error_log.txt                # Log file for errors encountered
└── README.md                    # Project documentation**
📚 Dependencies
<br>
This project requires only one external Python library:
<hr>
cryptography (Fernet encryption)
<hr>
Install it via pip:




**pip install cryptography**


📜 License
This project is licensed under the MIT License. You are free to modify and distribute the code while adhering to the license.

💬 Contact & Support
For questions, feedback, or support, feel free to reach out!
Author: Tejas Barguje Patil

<p align="left"> <a href="https://www.instagram.com/Tejas_Barguje_Patil" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram" width="40" height="40"/> </a> 
 
  <a href="mailto:tejasbarguje9@gmail.com" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" alt="Email" width="40" height="40"/> </a> </p>

**Happy encrypting! 🔐**

