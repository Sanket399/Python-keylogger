# Keylogger Project

This project is a Python-based keylogger that logs keystrokes, captures system information, monitors clipboard contents, records audio, takes screenshots, and sends the captured data via email. 

## Features

- **Keystroke Logging**: Captures every keystroke typed by the user.
- **System Information**: Logs information such as the system's IP address, processor, machine type, and public IP.
- **Clipboard Monitoring**: Captures clipboard data.
- **Audio Recording**: Records audio for a set duration using the system's microphone.
- **Screenshot Capture**: Takes screenshots at specified intervals.
- **Email Reporting**: Sends all captured data via email to a specified address.
- **File Encryption**: Encrypts captured data before sending.
- **File Deletion**: Deletes log files after they have been emailed to clean up traces.

## Requirements

- Python 3.x
- Libraries:
  - `pynput`
  - `requests`
  - `cryptography`
  - `sounddevice`
  - `scipy`
  - `PIL` (Pillow)

## Setup

1. Clone this repository:
    ```bash
    git clone <repo_url>
    cd <repo_name>
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure the email credentials in the script:
    - `email_address`: Enter the disposable email address for sending logs.
    - `password`: Enter the email password or an app-specific password.
    - `toaddr`: Enter the recipient email address to receive the logs.
  
    **Note**: For Gmail, you might need to enable "Less secure apps" or use an app password for your Gmail account.

## Credits

This project is based on a YouTube tutorial by Grant Collins.

## Disclaimer

This project is for educational purposes only. The use of keyloggers for malicious intent is illegal and unethical. Always respect privacy and adhere to legal guidelines when working with such software. Unauthorized access to computer systems or data is a criminal offense in many jurisdictions. Ensure that you have explicit consent before monitoring any system.

