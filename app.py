import subprocess
import os
import time

def update_system():
    try:
        print("Enter your sudo password:")
        subprocess.run(["sudo", "apt", "update"], check=True)
        print("System updated successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False

def clear_terminal():
    os.system('clear')

def show_welcome_message():
    print("Welcome to Chromebook Audio Drivers Fixer!")
    print("If you've changed your ChromeOS to something else, your speakers might not work.")
    print("This program will help you fix your speakers.")
    print("Choose an option from the list below:")
    print("1. Chromebook Audio Driver Installer")
    print("2. alsamixer")
    print("3. pavucontrol")
    print()
    print("If you can't unmute one of the speakers in alsamixer, choose option 1 and then try again.")

def install_chromebook_audio_drivers():
    clear_terminal()
    print("Installing Chromebook audio drivers, please wait...")
    try:
        subprocess.run(["git", "clone", "https://github.com/WeirdTreeThing/chromebook-linux-audio.git"], check=True)
        print("Repository cloned successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository: {e}")
        return
    try:
        os.chdir("chromebook-linux-audio")
        subprocess.run(["./setup-audio"], check=True)
        print("Audio driver setup completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running setup-audio: {e}")
        return
    print("Rebooting in 3 seconds...")
    time.sleep(3)
    subprocess.run(["sudo", "reboot"])

def open_alsamixer():
    clear_terminal()
    print("Now I will open alsamixer.")
    print("To unmute the speakers, press 'M' when a speaker is selected.")
    print("Once you are done, press 'Esc' to exit alsamixer and continue.")
    print("Make sure you've selected the soundcard. To do that, press 'F6' or click on 'Select Sound Card'.")
    input("Press Enter to open alsamixer...")
    subprocess.run(["alsamixer"])

def check_and_install_pavucontrol():
    try:
        subprocess.run(["pavucontrol", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("pavucontrol is already installed.")
    except FileNotFoundError:
        print("pavucontrol not found, installing...")
        subprocess.run(["sudo", "apt", "install", "-y", "pavucontrol"])
    except subprocess.CalledProcessError as e:
        print(f"Error checking pavucontrol: {e}")

def open_pavucontrol():
    check_and_install_pavucontrol()
    clear_terminal()
    print("Now, let's configure your speakers using pavucontrol.")
    print("Follow these steps to select your speakers:")
    print("1. Open the 'Configuration' tab.")
    print("2. Find your speaker and select the 'Pro Audio' option.")
    print("3. Go to the 'Output Devices' tab.")
    print("4. Select your speakers from the list of available devices.")
    print("Once you're done, you can close pavucontrol.")
    subprocess.run(["pavucontrol"])

def main():
    if update_system():
        clear_terminal()
        show_welcome_message()
        choice = input("Enter your choice: ")

        if choice == '1':
            install_chromebook_audio_drivers()
        elif choice == '2':
            open_alsamixer()
        elif choice == '3':
            open_pavucontrol()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
