import argparse
import sys
from colorama import Fore, Style, init
from utils import print_fsl_banner, print_version_info, run_command

# Initialize colorama for colored terminal output
init(autoreset=True)

class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise argparse.ArgumentError(None, message)

def run_container(local_fsl_data_path):
    print_fsl_banner()
    # Run 'docker run' command using run_command to start the FSL container
    run_command(['docker', 'run', '-it', '--rm','-w', '/volume/', '-v', f'{local_fsl_data_path}:/volume/', 'brainlife/fsl', '/bin/bash'])

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
