# Face Recognition App
This app is based on face_recognition library write by Adam Geitgey -  [GitHub repo](https://github.com/ageitgey/face_recognition). It makes face recognition process incredibly easy.

## Installation
The final version of the application is in progress, so there is no installation file yet. Instead, you can download the source and run the application from the command line. 

### Requirements to run code
- Linux, MacOS or Windows (Windows is not officially supported, but this app was write on Windows and everything was correct)
- Python 3.7+
Additional libraries:
- OpenCV 4.4.0
- dlib v19.9 or newer
- face_recognotion (link above)
- pandas

### Step by step installation
#### Installation for Linux, MacOS and Windows
1. Install Python by following the [instructions](https://www.python.org/downloads/). Downoland the newest version\
After installation you can check you Python version, by typing `python --version` in command line
2. Next, install pip. Type `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py` in command line. If you have pip already installed, upgrade it by typing `python -m pip install --upgrade pip`. It is recommended to upgrade pip even after installation. You can check you pip version by `pip --version`
3. Install OpenCV. Type `pip install opencv-python`.\
Type `python` in command line and then `import cv2` to check installation success. Nothing should show up if properly installed. Type `exit()` to exit from Python environment.
4. Install pandas. Type `pip install pandas`.\
As above, open Python and `import pandas` for checking installation success.
5. Install face_recognition library. Type `pip install face-recognition` in command line.\
As
