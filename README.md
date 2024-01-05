# FSL-pydocker tool

## Overview

FSL-pydocker is a Python tool designed to simplify the execution of FSL (FMRIB Software Library) within a Docker container. This tool facilitates the seamless integration of FSL into your workflow by providing a convenient command-line interface.

## Prerequisites

Before using FSL-pydocker, ensure that the following prerequisites are met:

- **Python**: Make sure you have Python installed on your system.
- **Docker Engine**: Ensure that Docker Engine is installed and active.
- **requirements.txt**: The project requires specific dependencies listed in the `requirements.txt` file. Install them using:

  ```bash
  pip install -r requirements.txt

## Usage

This tool utilizes the brainlife/fsl Docker image. You can use it by running this command in your fsl-pydocker directory:

  ```bash
  python -m fsl-pydocker -v VOLUME_PATH   or  python3 -m fsl-pydocker -v VOLUME_PATH 

This command will start fsl-pydocker, linking the specified local FSL data path to the container's /volume/ directory. You can use the fsl-pydocker/volume/ directory as your default volume LOCAL path.


