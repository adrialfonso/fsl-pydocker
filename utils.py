from colorama import Fore, Style
import subprocess
import sys

def run_command(command, check=True):
    try:
        subprocess.run(command, check=check)
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")

def print_fsl_banner():
    text = [
        f"{Fore.BLUE}  _____ ____  _               ______   ______   ___   ____ _  _______ ____  {Style.RESET_ALL}",
        f"{Fore.BLUE} |  ___/ ___|| |             |  _ \\ \\ / /  _ \\ / _ \\ / ___| |/ /| ____|  _ \\ {Style.RESET_ALL}",
        f"{Fore.BLUE} | |_  \\___ \\| |      _____  | |_) \\ V /| | | | | | | |   | ' / |  _| | |_) |{Style.RESET_ALL}",
        f"{Fore.BLUE} |  _|  ___) | |___  |_____| |  __/ | | | |_| | |_| | |___| . \\ | |___|  _ < {Style.RESET_ALL}",
        f"{Fore.BLUE} |_|   |____/|_____|         |_|    |_| |____/ \\___/ \\____|_|\\_\\|_____|_| \\_\\{Style.RESET_ALL}",
    ]

    for line in text:
        print(line)

    print("\n")

    print(Fore.GREEN + 'Welcome to FSL! (5.0.9)')
    print("fsl-pydocker is a Python script for running FSL (FMRIB Software Library) in a Docker container.")
    print("It allows you to perform neuroimaging analysis using FSL without the need to install FSL locally.")
    print("From now on, you're on a Ubuntu 16.04.3 LTS container. Type 'exit' if you want to stop fsl-pydocker:\n")

def print_version_info():
    print(f"fsl-pydocker 1.0")
    print(f"Python Version: {sys.version}")
    docker_version = run_command(['docker', '--version'], capture_output=True, text=True)
    print(f"Docker Version: {docker_version.stdout.strip()}")