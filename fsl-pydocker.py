import argparse
import docker
from colorama import Fore, Style, init
import sys

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

def print_version_info():
    print(f"fsl-pydocker 1.0")
    print(f"Python Version: {sys.version}")
    print(f"Docker Version: {docker.__version__}")

def run_container(local_fsl_data_path):
    try:
        # Create a Docker client
        client = docker.from_env()

        # Specify the Docker image to use
        image = "brainlife/fsl"

        # Directory inside the container where the volume will be mounted
        container_fsl_data_path = "/volume/"

        # Container configuration
        container_config = {
            'tty': True,
            'stdin_open': True,
            'detach': True,
            'working_dir': '/fsl-pydocker',
            'command': '/bin/bash',
            'volumes': {local_fsl_data_path: {'bind': container_fsl_data_path, 'mode': 'rw'}}
            # Mount the local directory into the container with read and write permissions
        }

        # Run the container with the specified volume
        container = client.containers.run(image, **container_config)

        # Execute 'ls' command inside the container to list the content of the specified directory
        ls_result = container.exec_run(['ls', container_fsl_data_path])
        print("\n" + f"Content of directory {container_fsl_data_path} inside the container:")
        print(ls_result.output.decode('utf-8'))

        # Tool description
        print_fsl_banner()
        print(Fore.GREEN + 'Welcome to FSL! (5.0.9)')
        print("fsl-pydocker is a Python script for running FSL (FMRIB Software Library) in a Docker container.")
        print("It allows you to perform neuroimaging analysis using FSL without the need to install FSL locally.")

        # Main loop
        print("\nEnter a command to run inside the container (type 'exit' to exit) ")
        while True:
            user_command = input("fsl-pydocker@root $ ")
            if user_command.lower() == 'exit':
                break
            else:
                command_result = container.exec_run(user_command)
                print(command_result.output.decode('utf-8'))

    except Exception as e:
        print(f"{Fore.RED}An error occurred: {str(e)}{Style.RESET_ALL}")

    finally:
        container.stop()
        container.remove()

def parse_args(args):
    # Use the custom parser to suppress the default error message
    parser = CustomArgumentParser(
        description=f'{Fore.CYAN}(HELP PANEL) -> Run FSL Docker container: python -m fsl-pydocker -v VOLUME_PATH{Style.RESET_ALL}'
    )

    # Add argument for local volume path
    parser.add_argument('-v', '--volume-path', type=str, nargs='?',
                        help=f'{Fore.YELLOW}Local path to FSL data volume{Style.RESET_ALL}')
    # New options for version information
    parser.add_argument('--version', action='store_true', help='Show version information')

    try:
        args = parser.parse_args(args)

        if not args.volume_path and not args.version:
            # If no arguments are provided, show help
            parser.print_help()
            sys.exit(1)

        if args.version:
            print_version_info()
            sys.exit(0)

    except argparse.ArgumentError as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
        parser.print_help()
        sys.exit(1)

    return args

if __name__ == "__main__":
    # Parse the command-line arguments
    args = parse_args(sys.argv[1:])

    # Run the container with the specified local path
    run_container(args.volume_path)
