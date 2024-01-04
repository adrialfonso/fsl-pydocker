import argparse
import docker
from colorama import Fore, Style, init
init(autoreset=True)

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
        # Stop and remove the container once the operations are done
        container.stop()
        container.remove()

if __name__ == "__main__":
     # Parse the command-line arguments
    parser = argparse.ArgumentParser(description=f'{Fore.CYAN}(HELP PANEL) -> Run FSL Docker container:{Style.RESET_ALL}')

    # Add argument for local path
    parser.add_argument('-v', '--volume-path', type=str, required=True,
                        help=f'{Fore.YELLOW}Local path to FSL data volume{Style.RESET_ALL}')

    # Parse the arguments or show help if not provided
    args = parser.parse_args()

    # Run the container with the specified local path
    run_container(args.volume_path)
