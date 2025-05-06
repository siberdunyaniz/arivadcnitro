import os
import sys
import time
import random
import string
import subprocess
import webbrowser
from pystyle import Colors, Colorate
from colorama import init

init()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def install_package(package):
    try:
        __import__(package)
        print(Colorate.Horizontal(Colors.green_to_cyan, f"✅ {package} zaten yüklü."))
    except ImportError:
        print(Colorate.Horizontal(Colors.yellow_to_red, f"📥 {package} yükleniyor..."))
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(Colorate.Horizontal(Colors.green_to_cyan, f"🎉 {package} yüklendi."))
        except subprocess.CalledProcessError:
            print(Colorate.Horizontal(Colors.red_to_yellow, f"❌ {package} yüklenemedi. Lütfen manuel yükleyin: pip install {package}"))
            sys.exit(1)

def install_dependencies():
    packages = ['pystyle', 'colorama', 'user_agent', 'requests']
    clear_console()
    print(Colorate.Horizontal(Colors.green_to_cyan, "🔥 ArivaHackTool Bağımlılıkları Yükleniyor..."))
    for package in packages:
        install_package(package)
    print(Colorate.Horizontal(Colors.green_to_cyan, "🎉 Tüm bağımlılıklar hazır!"))
    time.sleep(1)

def loading_animation(word):
    heron = [
        "[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]",
        "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]",
        "[■■■■■■■■■□]", "[■■■■■■■■■■]"
    ]
    for _ in range(3):
        for x in heron:
            sys.stdout.write(f'\r{Colorate.Horizontal(Colors.yellow_to_red, word + x)}')
            sys.stdout.flush()
            time.sleep(0.05)
    print()

def display_banner(custom_prompt):
    clear_console()
    banner = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⢄⡀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
ATAHANARSLAN ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⠀⠀⠀⠀⠀⠀⠘⢆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢋⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢂⠀⠀⠀⠰⡀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀
ARİVA GENEL⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣣⠃⢀⠀⠀⠀⢀⠀⠀⢀⣠⠃⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⢃⠀⠀⠀⠙⡄⠀⠀⠀⢣⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⡱⢡⢠⠋⣠⠂⢀⠋⠀⢠⢾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⡀⠀⠀⠘⡆⠀⠀⠀⢰⡀⠀⠀⠀⢣⠀⠀⠀⠀
BAŞKANI⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠎⣰⠁⢇⠇⣰⠃⢠⡎⠀⠀⡆⡌⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⢀⠀⢇⠀⠀⠀⢁⠀⠀⠀⠀⢇⠀⠀⡄⠈⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠊⢀⣰⢃⢰⡞⢰⠇⡰⢹⠀⢠⢿⢠⠃⠀⠀⠀⠀⡘⠀⠀⠀⠀⠀⠀⢸⠀⢸⠀⠀⠀⢸⠀⠀⠀⠀⢸⡄⠀⡇⠀⢰⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠦⣩⣥⣰⣶⣻⡏⡎⡞⢃⡘⣐⡕⡏⢀⠇⡇⠸⠀⠀⡰⠁⢰⡇⠀⠀⠀⠀⠀⢰⢸⠀⠈⠀⠀⠀⢸⠀⠀⠀⠀⢸⠇⠀⢹⠀⠘⡆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠤⠾⠕⠞⢰⠁⡇⡞⢵⠿⣑⡇⣼⠀⣇⢰⠀⣰⠁⢠⣿⠀⠀⠀⠀⢠⠀⢸⢹⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⢸⠰⠀⠘⠀⠀⡇⠀⠀
⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡶⢀⢧⢿⢠⢱⣧⠋⠀⠀⡏⣻⠀⠛⡞⣴⡏⢀⣿⢻⠀⠀⢰⠂⢸⡄⢸⣿⠀⠠⠀⠀⠀⣾⠀⢀⠀⠀⠀⡆⡄⠀⢇⠀⡇⠀⠀
⠀⠀⠀⠀⠀⢀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠁⠸⠸⡌⢸⣿⡿⢦⣄⢀⢱⢸⠀⣦⢻⢿⡀⡞⠥⢼⣄⠀⢸⠀⢸⠃⠈⣿⠀⢰⠀⢠⢰⢻⠀⢸⢀⠀⠀⣇⢧⠀⠸⡆⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⡸⡇⢸⢹⣧⠸⠿⣿⣝⢮⡄⠹⡄⢸⢿⢄⠀⠈⢯⠉⣿⢄⡞⢠⡀⡇⠀⡟⠀⠸⢘⠀⢇⠘⡿⡆⠀⢸⠘⡀⠀⢡⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⡇⡇⢸⢸⠈⢻⡦⣿⡟⠈⢿⡸⣇⡟⡇⢀⡥⠤⣘⡆⡿⢀⢿⠺⢃⡇⢠⡇⠀⢠⡇⠀⠈⢦⢷⡘⢄⠀⢧⠱⡀⠀⢃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢡⣷⡁⣼⢸⠀⠀⠉⠙⠁⠀⠀⠑⢟⠇⠁⠞⠛⣿⣿⣿⣷⣼⣘⡄⢸⠀⣼⠀⠀⢸⢇⢠⣄⢸⠻⣏⠪⢧⡄⢣⠹⣆⠈⢧⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣻⡄⣿⠘⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠘⡷⣼⣯⡇⠉⣻⣗⡆⢠⡏⠀⠀⡞⠘⣜⡈⢦⡆⣬⡧⡄⡜⠧⣓⣘⣆⠀⢣⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⢧⢻⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠚⠓⠋⠀⢸⠃⡼⠀⠀⢠⡇⠀⢹⡇⢨⢧⢁⠀⠈⢽⡀⠉⠘⢶⠑⢄⠱⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣮⣿⣸⢸⠀⢸⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡘⢰⡇⠀⠀⣾⠇⠀⢸⡱⡼⡌⡞⡆⠀⠀⠻⣄⠀⠈⢧⠀⠳⡌⢆
⠀⢀⠄⢤⣰⠛⡄⠀⠀⠀⠀⠀⠀⠀⠀⡼⣝⡏⡏⠈⡄⢸⣞⢆⠀⠘⣷⢆⠤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⡜⠀⠀⢠⢻⡀⠀⣿⣧⠃⠹⡜⢾⡄⠀⡀⠈⢢⡀⠈⢆⠀⠈⢢
⠀⣸⣠⢤⣈⡱⡜⡆⠀⠀⠀⠀⠀⠀⠠⢱⡿⢠⠃⠀⣷⢸⢻⣆⠣⡀⠈⠒⠤⠀⠯⠟⠀⠀⠀⠀⠀⠀⢀⡿⢰⠇⠀⠀⣼⠈⣿⣀⢿⣿⣀⠀⠙⢮⣻⣄⠱⡄⠀⠙⠂⠈⢦⠀
⠈⣀⣠⡴⠳⣄⡷⠸⡄⠀⠀⠀⠀⠀⢀⢣⠇⢸⠀⠀⢸⢸⠀⠙⠣⣽⣦⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠒⠉⠃⡎⡄⠀⢀⢱⠀⢫⢹⢾⣜⢮⡑⠢⠤⠭⣟⡷⢝⣦⡀⠀⠀⠀⠣⡀
⢀⣀⣠⡛⢆⡘⠁⠀⢫⢷⡀⠀⠀⠀⡜⣾⠀⢸⠀⠀⠀⣾⠀⠀⡘⢸⠀⠑⠒⣶⠖⣏⢩⠙⠢⡀⠀⠀⣸⣸⢻⠁⠀⡼⡿⠀⠈⢎⢣⠻⡿⠟⠓⠋⠁⠀⣀⣀⠒⢮⣵⣄⠀⠀⠐
⠀⠠⠚⠱⣴⢳⠀⠀⢸⡎⣇⠀⠀⢰⣰⡟⠀⢸⠀⠀⠀⢸⡀⢠⠇⣘⠀⠀⢰⠻⠸⡘⡛⢄⠀⠈⠂⠀⡇⡏⣬⠀⢠⠃⡇⡀⠀⠈⢳⣕⣿⣦⣶⣾⠷⠛⠉⢀⡠⠤⠹⢯⢧⠀
⣷⠩⠟⠒⠁⠙⠀⢀⠟⠀⢸⢣⣠⢯⣇⡇⠀⢸⠀⠀⠀⠀⣇⡌⢠⠘⢇⠀⢸⠀⠀⢣⠙⣗⠑⢄⠀⢸⣸⣼⡛⠀⠸⠀⡇⢧⢀⡰⢋⢃⠃⠁⠠⠊⠀⣠⠖⠁⠀⠀⠀⠀⢎⣇⠀
⡵⣑⣄⠀⠤⠔⠊⠁⠀⠀⡜⠀⢹⡿⢿⡇⠀⢸⠀⠀⠀⠀⣏⢇⠈⢣⡘⡀⢸⡄⠀⠀⢳⡈⠳⢄⣁⣾⢯⢧⠇⠀⡆⢀⠀⢸⣏⠔⠹⡼⠀⡷⠁⢠⠞⠁⠀⠀⠀⠸⡇⠉
⠱⣄⠀⠀⠀⠀⠀⠀⠀⡔⡠⠃⠘⣶⣼⢧⠀⢸⠀⠀⠀⠀⡏⡎⠆⠀⠙⢿⣼⡳⣄⠀⠈⣏⠓⠤⣤⣿⡸⡾⠀⢠⡇⣸⠀⢸⡷⡀⡇⡇⣸⠀⣴⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀
⠀⡜⠳⠄⠀⠀⠤⠴⠯⠊⠀⠀⠀⡇⢿⢸⣄⠘⡄⠀⠀⢰⠁⡇⢸⢄⠀⠀⢙⣿⣮⡳⣄⠘⡆⠀⢸⠇⢳⡇⠀⢸⡇⡇⢀⣸⢱⣥⡇⡇⣧⢊⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀
⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⢟⡄⢃⠀⠀⡏⢸⢡⠆⠀⠙⠢⣾⠀⢣⠙⣮⡢⡀⠀⢸⣸⣿⡇⠀⢸⣿⠀⡜⡇⠈⣿⣛⣹⠃⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡷⢄
⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡯⣾⣧⣘⣆⡜⣠⡿⠃⠀⡆⠀⠀⢸⠀⠀⢣⠈⠻⣞⢦⢸⡏⣿⢇⠀⢸⣿⠀⠇⠇⠀⠙⢻⣹⢰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣦
⠀⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⣏⠉⢩⡿⡿⣟⠳⣖⡺⠃⠀⠀⠸⡄⠀⠀⢣⠀⠈⢳⣽⡟⣟⡘⣴⡸⡇⠀⠀⠀⠀⢀⣸⣧⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢎⣧⠉
⠀⠀⠱⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠹⡕⢼⣧⡁⠈⠳⡌⠱⡄⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠙⠳⡻⣷⡀⠹⣧⠀⡀⠀⠀⡾⢋⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⡾⢺⡂
⠀⠀⠀⠈⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠃⠸⡍⣷⣀⠀⠘⣦⣸⠀⠀⢀⡎⠣⣤⡀⠀⠀⠀⠀⠀⠈⠛⠭⢹⣿⣷⠷⠀⣰⣁⡜⠀⠀⠀⠀⠀⠀⠀⠀⢀⠏⠗⠊⠁⠈
⠀⠀⠀⠀⠀⠱⡄⠀⠀⠀⠀⠀⠀⠀⢠⠈⡀⠀⠀⢹⠛⠛⠿⣦⡇⠟⡀⡠⠻⡔⠀⢹⢯⡢⡀⠀⠀⠀⠀⢀⣜⡿⢻⣯⡹⠀⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀⢀⠏⠗⠊⠁⠈
⠀⠀⠀⠀⠀⠀⢸⣦⠀⠀⠀⠀⠀⠀⠀⠀⠃⠄⠀⠈⢆⠀⣀⡿⠁⣠⠝⠁⠀⠇⠀⡏⠀⢹⠮⣳⠄⠀⠀⠀⠠⠔⢛⢯⣿⠀⣇⡇⠀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⢰⠀⠀⠀⠀
    """
    print(Colorate.Vertical(Colors.green_to_cyan, banner))
    print(Colorate.Horizontal(Colors.green_to_cyan, "—" * 60))
    print(Colorate.Horizontal(Colors.white_to_blue, f"Programmer: @ATAHANARSLAN | Channel: @ArivaTools"))
    print(Colorate.Horizontal(Colors.white_to_blue, f"Cybersecurity: @SIBBERDUNYANIZ"))
    print(Colorate.Horizontal(Colors.green_to_cyan, "—" * 60))
    print(Colorate.Horizontal(Colors.yellow_to_red, f"Prompt: {custom_prompt}"))
    print()


install_dependencies()


os.system("pkg install espeak")


clear_console()
loading_animation("Api İle Bağlantı Kuruluyor ...")
webbrowser.open('https://t.me/ArivaTools')


custom_prompt = input(Colorate.Horizontal(Colors.green_to_cyan, "Ekranda kalacak mesajı girin (örn: Siber Gücü Serbest Bırak!): "))
if not custom_prompt.strip():
    custom_prompt = "Siber Gücü Serbest Bırak!"


display_banner(custom_prompt)
print(Colorate.Horizontal(Colors.green_to_cyan, "🔥 ArivaHackTool Nitro Generator Başlıyor..."))


try:
    num = int(input(Colorate.Horizontal(Colors.yellow_to_red, 'Kaç Nitro kodu oluşturulacak? ')))
    if num <= 0:
        raise ValueError
except ValueError:
    display_banner(custom_prompt)
    print(Colorate.Horizontal(Colors.red_to_yellow, "❌ Lütfen geçerli bir pozitif sayı girin!"))
    sys.exit(1)


filename = "DiscordNitro.txt"
display_banner(custom_prompt)
print(Colorate.Horizontal(Colors.green_to_cyan, "Nitro kodları oluşturuluyor, sabırlı olun ☺️"))
start = time.time()

try:
    with open(filename, "w", encoding='utf-8') as file:
        for _ in range(num):
            code = ''.join(random.choices(
                string.ascii_uppercase + string.digits + string.ascii_lowercase, k=16
            ))
            file.write(f"https://discord.gift/{code}\n")
    display_banner(custom_prompt)
    print(Colorate.Horizontal(Colors.green_to_cyan, f"🎉 {num} kod oluşturuldu | Zaman: {time.time() - start:.2f} saniye"))
except IOError:
    display_banner(custom_prompt)
    print(Colorate.Horizontal(Colors.red_to_yellow, "❌ Dosya yazılamadı! Depolama iznini kontrol edin."))
    sys.exit(1)


display_banner(custom_prompt)
print(Colorate.Horizontal(Colors.green_to_cyan, "Kodlar kontrol ediliyor..."))

try:
    from user_agent import generate_user_agent
    import requests
except ImportError:
    display_banner(custom_prompt)
    print(Colorate.Horizontal(Colors.red_to_yellow, "❌ Gerekli modüller eksik! Lütfen bağımlılıkları kontrol edin."))
    sys.exit(1)

try:
    with open(filename, "r", encoding='utf-8') as file:
        for line in file:
            nitro = line.strip()
            code = nitro.split('/')[-1]
            url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
            headers = {'User-Agent': generate_user_agent()}
            
            try:
                r = requests.get(url, headers=headers, timeout=5)
                display_banner(custom_prompt)
                if r.status_code == 200:
                    print(Colorate.Horizontal(Colors.green_to_cyan, f"✅ Bulundu | {nitro}"))
                    break
                else:
                    print(Colorate.Horizontal(Colors.red_to_yellow, f"❌ Geçersiz | {nitro}"))
            except requests.RequestException:
                display_banner(custom_prompt)
                print(Colorate.Horizontal(Colors.red_to_yellow, f"❌ Hata: {nitro} kontrol edilemedi (ağ sorunu)."))
except IOError:
    display_banner(custom_prompt)
    print(Colorate.Horizontal(Colors.red_to_yellow, "❌ Dosya okunamadı! Dosyanın var olduğunu kontrol edin."))
    sys.exit(1)

print(Colorate.Horizontal(Colors.green_to_cyan, "🎉 İşlem tamamlandı!"))