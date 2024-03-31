# FSL-pydocker tool

## Overview
<p align="center">
  <img src="https://github.com/adrialfonso/fsl-pydocker/assets/90824134/3cc26b81-d605-49ed-b12b-4992f1d2e768" alt="Image" width="800"/>
</p>

Due to the difficulty to install FSL in Windows OS, we created FSL-pydocker to simplify the execution of FSL (FMRIB Software Library) within a Docker container. This tool facilitates the seamless integration of FSL into your workflow by providing a convenient command-line interface. By using FSL-pydocker you won't have problems to use FSL in Windows OS. This tool utilizes the `brainlife/fsl` Docker image. 

## Prerequisites

Before using FSL-pydocker, ensure that the following prerequisites are met:

- **Python**: Make sure you have Python installed on your system. ✅ (view appendix)
- **Docker Engine**: Ensure that Docker Engine is installed and active. ✅ (view appendix)
- **requirements.txt**: The project requires specific dependencies listed in the `requirements.txt` file. Install them using: ✅

  ```bash
    pip install -r requirements.txt

## Usage

- First, download this repository or clone it:

  ```bash
      git clone https://github.com/adrialfonso/fsl-pydocker.git

- You need to link the specified local FSL volume path (with all your data) to the container's /volume/ directory (complete path). You can use the fsl-pydocker/volume/ directory as your default local volume path. In other words, you will need to move all your data (images and other stuff) to fsl-pydocker/volume:

  <p align="center">
    <img src=https://github.com/adrialfonso/fsl-pydocker/assets/155368998/04cb4420-cee6-41a2-ad77-0065326304a4" alt="Image" width="700"/>
  </p>

- Remember that all the output will be stored in the same fsl-pydocker/volume/ directory. Open a "cmd" (Win+R and type "cmd"), navigate to your fsl-pydocker directory:

  <p align="center">
    <img src=https://github.com/adrialfonso/fsl-pydocker/assets/155368998/6f8a4fa7-0e97-4680-86ab-0a9dfc9ee110" alt="Image" width="600"/>
  </p>

- And run the following command:

  ```bash
    python -m fsl-pydocker -v VOLUME_PATH

- VOLUME_PATH corresponds to your local fsl-pydocker/volume path (absolute path). If the previous command doesn't work, try:

  ```bash
    python3 -m fsl-pydocker -v VOLUME_PATH

## Contributing

- Feel free to contribute to the development of FSL-pydocker. Create a fork of the repository, make your changes, and submit a pull request.

## Appendix

- **Python**: Make sure you have installed python 3+. If not, download it from [python.org](https://www.python.org/downloads/)
- **Docker Engine**: Docker is an open source containerization technology for building and containerizing your applications. To be able to run FSL-pydocker in a Windows OS, you need to make sure that  Docker Engine is running background. Youn can follow this easy tutorial from [Docker Desktop Documentation](https://docs.docker.com/desktop/install/windows-install/). Remember that every time you want to run FSL-pydocker, Docker Engine needs to be running (just open Docker Desktop before using FSL-pydocker).

- In order to check that both installations were succesful, try:

  ```bash
      python --version && docker ps

- or:

  ```bash
      python3 --version && docker ps

If no errors displayed, all is OK!


