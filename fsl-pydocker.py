import argparse
import docker
from colorama import Fore, Style, init
import sys

init(autoreset=True)

class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise argparse.ArgumentError(None, message)

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
        print(f"Content of directory {container_fsl_data_path} in the container:")
        print(ls_result.output.decode('utf-8'))

        # Display the FSL version in the container
        fsl_version = container.exec_run(['cat', '/usr/share/fsl/5.0/etc/fslversion'])
        print('Welcome to FSL!' + ' -> ' + fsl_version.output.decode('utf-8'))

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
    parser.add_argument('-v', '--volume-path', type=str, required=True,
                        help=f'{Fore.YELLOW}Local path to FSL data volume{Style.RESET_ALL}')

    try:
        return parser.parse_args(args)

    except argparse.ArgumentError as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    # Parse the command-line arguments
    args = parse_args(sys.argv[1:])

    # Run the container with the specified local path
    run_container(args.volume_path)
