# Face Recognition App
This app is based on face_recognition library write by Adam Geitgey -  [GitHub repo](https://github.com/ageitgey/face_recognition). It makes face recognition process incredibly easy.

## Installation
The final version of the application is in progress, so there is no installation file yet. Instead, you can download the source and run the application from the command line. 

### Requirements to run code
- Linux, MacOS or Windows (Windows is not officially supported, but this app was write on Windows and everything was correct)
- Python 3.7+
- CMake
Additional libraries:
- OpenCV 4.4.0
- dlib v19.9 or newer
- face_recognotion (link above)
- pandas

### Step by step installation
#### Installation for Linux, MacOS and Windows
1. Install Python by following the [instructions](https://www.python.org/downloads/). Downoland the newest version\
After installation you can check you Python version, by typing ```python --version``` in command line
2. Next, install pip. Type ```curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py``` in command line. If you have pip already installed, upgrade it by typing ```python -m pip install --upgrade pip```. It is recommended to upgrade pip even after installation. You can check you pip version by ```pip --version```
3. To install CMake follow the instructions [from CMake website](https://cmake.org/install/)
4. Install Dlib. Type `pip install dlib` in command line
5. Install OpenCV. Type `pip install opencv-python`. in command line
Type `python` in command line to open Python enviroment. Then `import cv2` to check installation success. Nothing should show up if properly installed. Type `exit()` to exit from Python environment.
6. Install pandas. Type `pip install pandas`.\
As above, open Python and `import pandas` for checking installation success.
7. Install face_recognition library. Type `pip install face-recognition` in command line.


After installation you can downoland source code of the project. In command line go to place, where you want to downoland code and type `git clone https://gitlab.com/Lukaszz99/facerecognition.git`.\
When cloning is finished go to `facerecognition` folder.\
Now you can run face recognition application. Type `python main.py -e encodings/example_set.pickle -d cnn`.\
After few seconds you should see video from your compuer's camera.\
Instructions how to make your own .pickle file (this file contains coded faces for recognition) are in face_encode.py