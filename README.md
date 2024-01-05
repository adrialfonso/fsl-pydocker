# FSL-pydocker tool

## Overview
<p align="center">
  <img src="https://github.com/adrialfonso/fsl-pydocker/assets/90824134/3cc26b81-d605-49ed-b12b-4992f1d2e768" alt="Image" width="800"/>
</p>

FSL-pydocker is a Python tool designed to simplify the execution of FSL (FMRIB Software Library) within a Docker container. This tool facilitates the seamless integration of FSL into your workflow by providing a convenient command-line interface. This tool utilizes the `brainlife/fsl` Docker image. 

## Prerequisites

Before using FSL-pydocker, ensure that the following prerequisites are met:

- **Python**: Make sure you have Python installed on your system. ✅
- **Docker Engine**: Ensure that Docker Engine is installed and active. ✅
- **requirements.txt**: The project requires specific dependencies listed in the `requirements.txt` file. Install them using: ✅

  ```bash
    pip install -r requirements.txt

## Usage

- You need to link the specified local FSL volume path (with all your data) to the container's /volume/ directory. You can use the fsl-pydocker/volume/ directory as your default local volume path. Navigate to your fsl-pydocker directory and run the following command:

  ```bash
    python -m fsl-pydocker -v VOLUME_PATH   or  python3 -m fsl-pydocker -v VOLUME_PATH

- Feel the synergy of FSL and Docker working harmoniously with FSL-pydocker, simplifying your neuroimaging tasks. Happy analyzing!

## Contributing

- Feel free to contribute to the development of FSL-pydocker. Create a fork of the repository, make your changes, and submit a pull request.

