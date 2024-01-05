import argparse
import subprocess
from colorama import Fore, Style, init
import sys

# Initialize colorama for colored terminal output
init(autoreset=True)

class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise argparse.ArgumentError(None, message)

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
    print("Type 'exit' if you want to stop the fsl-pydocker container:\n")

def print_version_info():
    print(f"fsl-pydocker 1.0")
    print(f"Python Version: {sys.version}")
    docker_version = subprocess.run(['docker', '--version'], capture_output=True, text=True)
    print(f"Docker Version: {docker_version.stdout.strip()}")

def run_container(local_fsl_data_path):
    print_fsl_banner()
    try:
        # Run 'docker run' command using subprocess to start the FSL container
        subprocess.run(['docker', 'run', '-it', '--rm','-w', '/volume/', '-v', f'{local_fsl_data_path}:/volume/', 'brainlife/fsl', '/bin/bash'], check=True)

    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")

def parse_args(args):
    # Create a custom ArgumentParser with specific formatting
    parser = CustomArgumentParser(
        description=f'{Fore.CYAN}(HELP PANEL) -> Run FSL Docker container: python -m fsl-pydocker -v VOLUME_PATH{Style.RESET_ALL}'
    )

    # Define command-line arguments
    parser.add_argument('-v', '--volume-path', type=str, nargs='?',
                        help=f'{Fore.YELLOW}Local path to FSL data volume{Style.RESET_ALL}')
    parser.add_argument('--version', action='store_true', help='Show version information')

    try:
        args = parser.parse_args(args)

        # Check for missing required arguments
        if not args.volume_path and not args.version:
            parser.print_help()
            sys.exit(1)

        # Display version information and exit if requested
        if args.version:
            print_version_info()
            sys.exit(0)

    except argparse.ArgumentError as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
        parser.print_help()
        sys.exit(1)

    return args

if __name__ == "__main__":
    # Parse command-line arguments and run the FSL Docker container
    args = parse_args(sys.argv[1:])
    run_container(args.volume_path)
