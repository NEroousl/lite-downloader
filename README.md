# Lite Downloader

Lite Downloader is a simple Python-based tool designed to download files from any URL with an easy-to-use interface and a progress bar. It can handle file downloads efficiently and automatically names files based on the URL or server response.

### Features:
- Download any file from a URL (supports HTTP/HTTPS).
- Displays a progress bar during download using `tqdm`.
- Extracts filenames from the URL or `Content-Disposition` header.
- Saves the file locally with the proper filename or a default name.

---

## Prerequisites

Before using Lite Downloader, ensure you have the following software installed:

### 1. **Python 3.6+**
Lite Downloader requires Python 3.6 or higher. If you do not have Python installed, you can download it from the [official Python website](https://www.python.org/downloads/).

### 2. **Install Required Libraries**
Lite Downloader uses the following Python libraries:
- `requests`: For handling HTTP requests and downloading files.
- `tqdm`: For displaying a download progress bar.

To install these libraries, run the following commands in your terminal or command prompt:

```bash
pip install requests tqdm
```

---

## Installation

1. **Clone the Repository**:
   First, clone the repository to your local machine using Git.

   ```bash
   git clone https://github.com/NEroousl/lite-downloader.git
   cd lite-downloader
   ```

---

## Usage

1. **Run the Script**:
   Once you have the project set up, run the `lite-downloader.py` script:

   ```bash
   python lite-downloader.py
   ```

2. **User Interface**:
   After launching the script, it will prompt you to input the URL for the file you want to download.

   Example:
   ```bash
   Enter the download link: https://example.com/file.zip
   ```

   The downloader will fetch the file, display a progress bar, and save the file to your current directory.

3. **Download Again**:
   After a successful download, you'll be asked if you'd like to download another file. Type `y` for yes or `n` to exit.

---

## Create a Standalone Executable

If you want to create a standalone executable for Windows, you can use **PyInstaller** to package the script.

1. **Install PyInstaller**:
   Install PyInstaller using `pip`:

   ```bash
   pip install pyinstaller
   ```

2. **Build the Executable**:
   To generate the `.exe` file, run the following command:

   ```bash
   pyinstaller --onefile lite-downloader.py
   ```

   This will create a `lite-downloader.exe` in the `dist` folder, which you can run without needing Python installed.

---

## Example

Here’s an example of how it works:

1. You will be prompted for a download link:
   ```bash
   Enter the download link: https://example.com/file.zip
   ```

2. After entering the URL, the program will display a progress bar as the file is being downloaded:
   ```bash
   100%|███████████████████████████████████████████████████████████████████| 10.0M/10.0M [00:02<00:00, 5.0MB/s]
   Download completed! File saved as file.zip.
   ```

3. You will then be prompted to download another file:
   ```bash
   Do you want to download something again (y/n):
   ```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contribution

Feel free to fork the repository, submit issues, or make pull requests. Contributions are always welcome!

---

## Acknowledgements

- **Malinda Vitharana** (@NEroousl) for developing Lite Downloader.
- **tqdm**: A fast, extensible progress bar library for Python.
- **requests**: Simple HTTP requests for Python.

---
### Note:
Please ensure that you have permission to download the files you are accessing. Always respect copyrights and legal constraints when downloading files from the internet.

---

