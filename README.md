# Zoro 

This project provides a graphical user interface (GUI) wrapper for the waifu2x-ncnn-vulkan model, enabling users to easily upscale images by 2x or 4x. It's built using customtkinter for a modern and user-friendly experience. **This application is designed for Linux systems.**

## Features

* **Image Upscaling:** Upscales images using the powerful waifu2x-ncnn-vulkan model.
* **Scaling Options:** Offers 2x and 4x scaling options.
* **Graphical User Interface (GUI):** Provides a simple and intuitive interface using customtkinter.
* **File Selection:** Allows users to easily select input images.
* **Easy to Use:** Streamlined workflow for quick image upscaling.
* **Linux Specific:** Designed and tested for Linux environments.

## License

This project is licensed under the **GNU General Public License v3.0 (GPLv3)**. See the `LICENSE` file for more details.

The model waifu2x-ncnn-vulkan is licensed under the **MIT**. See the `LICENSE` file inside the model folder for more details.
## Prerequisites

* Python 3.11 or higher
* CustomTkinter (`customtkinter`)
* Pillow (`PIL`)

## Installation

1.  **Clone the repository (or download the script):**

    ```bash
    git clone git@github.com:Yoru-cyber/zoro.git
    cd waifu2x-gui-wrapper
    ```

2.  **Install dependencies using pip or poetry:**

    ```bash
    pip install .
    ```

    ```bash
    poetry env use
    poetry install
    ```

## Usage

1.  **Run the script:**

    ```bash
    python src/zoro/main.py
    ```

2.  **Using the GUI:**

    * Click the "Select your image" button to choose the image you want to upscale.
    * Select the desired scaling factor (2x or 4x).
    * Click the "Upscale" button to start the upscaling process.
    * The upscaled image will be saved to the same directory as the input image, with a "_upscaled" suffix.

## Notes

* **Linux Compatibility:** This application is specifically designed for Linux systems.
* Ensure that the `waifu2x-ncnn-vulkan` executable is correctly installed and accessible from your system's command line.
* The output image will be saved in the root location of the project.
* Depending on the size of the input image and your system's resources, the upscaling process may take some time.
* If you encounter any issues related to `waifu2x-ncnn-vulkan` itself, please refer to the official waifu2x-ncnn-vulkan documentation.