# Discord Nitro Generator

**An educational tool for generating and checking Discord Nitro gift codes, built with Python.**

This project demonstrates the creation and validation of Discord Nitro gift codes using Python, featuring a vibrant CLI interface with `pystyle` and `colorama` for gradient-colored outputs. It includes automated dependency installation, a persistent ASCII banner, and a customizable prompt, making it a visually appealing and user-friendly tool for learning purposes.

## Features
- **Automated Dependency Installation**: Installs required packages (`pystyle`, `colorama`, `user_agent`, `requests`) seamlessly.
- **Colorful Interface**: Uses `pystyle` for `green_to_cyan` and `yellow_to_red` gradient text, inspired by `ArivaHackTool`.
- **Persistent ASCII Banner**: Displays a branded banner with every screen refresh.
- **Custom Prompt**: Allows users to set a persistent message displayed below the banner.
- **Telegram Integration**: Redirects to `t.me/ArivaTools` at startup.
- **Termux Compatibility**: Supports `espeak` for audio feedback on Termux.
- **Robust Error Handling**: Manages invalid inputs, file I/O issues, network errors, and missing dependencies.
- **Code Generation & Validation**: Generates random Nitro codes and checks their validity via Discord's API.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/arivadcnitro.git
   cd arivadcnitro
   ```
2. Run the script:
   ```bash
   python arivadcnitro.py
   ```
3. For Termux, ensure `espeak` is installed:
   ```bash
   pkg install espeak
   ```

## Requirements
- Python 3.7+
- Pip packages: `pystyle`, `colorama`, `user_agent`, `requests`
- Termux (optional): `espeak`

## Usage
1. Launch the script to install dependencies automatically.
2. Enter a custom prompt (e.g., "Siber Gücü Serbest Bırak!").
3. Specify the number of Nitro codes to generate.
4. The script saves codes to `DiscordNitro.txt` and checks their validity.

## Disclaimer
**This project is for educational purposes only.** Generating and checking random Discord Nitro codes may violate Discord's Terms of Service, potentially leading to account bans or legal consequences. Use responsibly and only with explicit permission. The author is not responsible for misuse.

## Credits
- **Programmer**: @ATAHANARSLAN
- **Channel**: [t.me/ArivaTools](https://t.me/ArivaTools)
- **Cybersecurity**: @SIBBERDUNYANIZ