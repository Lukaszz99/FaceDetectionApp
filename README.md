# Face Recognition App

This app is a result of summer practice in Joint Institute for Nuclear Research in Dubna. The main core of the application is the video recognition system based on face_recognition library write by Adam Geitgey -  [GitHub repo](https://github.com/ageitgey/face_recognition). It makes face recognition process incredibly easy and efficient in live-time.

 Running this app from one executable file is still unable due to early version, so if you want to run it you have to download source code and all libraries used in code. Installation instruction is below.

## Installation

The final version of the application is in progress, so there is no installation file yet. Instead, you can download the source and run the application from the command line. 

### Requirements to run code

- Linux, MacOS or Windows (Windows is not officially supported, but this app was write on Windows and everything was correct)
- Python 3.7+ </br> </br>
This code use additional libraries
- OpenCV 4.4.0
- dlib v19.9 or newer
- face_recognition (link above)
- pandas

## Step by step libraries installation

### Installation on Linux and MacOS

1. Install Python by following the [instructions](https://www.python.org/downloads/). Download the newest version. After installation you can check you Python version, by typing in command line

    ``` shellscript
    python --version
    ```

2. Next, install pip. Type in command line

    ```shellscript
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    ```

    If you have pip already installed, upgrade it by typing ```python -m pip install --upgrade pip```. It is recommended to upgrade pip even after installation. You can check you pip version by ```pip --version```. Minimum required version is 20.2.1.

3. Install OpenCV. Type in command line

    ``` shellscript
    pip install opencv-python
    ```

    After installation type `python` in command line to open Python environment. Then

     ```python
     >>> import cv2
     ```

      to import OpenCV library. If nothing will show it's mean installation success. Type `exit()` to exit from Python environment.

4. To install Pandas type in command line

     ```shellscript
     pip install pandas
     ```

    After installation open Python environment and check installation success. This time to import Pandas type `import pandas`.

5. Finally let's install face_recognition library.

    1. Firstly install dlib library. [How to install dlib on Linux and MacOS](https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf)

    2. After that, you can install face_recognition module. Type in command line

        ```shellscript
         pip install face_recognition
        ```

    Check installation success in the same way as in 3rd and 4th point.

### Installation on Windows

Follow the instructions from the previous chapter from 1st to 4th point. Remember to add Python to your PATH environment variable (select checkbox in Python executable installer). To install face_recognition library, you need to take more steps.

1. You need to install Visual C++. If you have installed Microsoft Visual Studio you can skip this step.

    a. You can install only Visual C++ from [this link](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019). Download Build Tools for Visual Studio 2019. Open installer and choose `C++ build tools` in installer's window. After that select install. This will require about 2.1GB of free disc space

    b. Other way is to  install [Microsoft Visual Studio](https://visualstudio.microsoft.com/downloads) - download Community version.

2. Install CMake from [this link](https://cmake.org/download/). To make installation as easy as possible get .msi installer

3. Install dlib library from [this link](http://dlib.net/). After download dlib.zip unpack it and go to dlib folder. Next follow this commands

    ```shellscript
    cd examples
    mkdir build
    cd build
    cmake -G "Visual Studio 16 2019" -T host=x64 ..
    cmake --build. --config Release
    ```

    If you dont have newest version of Visual C++, you should type your version in `cmake -G "your version"...`

4. Finally install face_recognition library

    ```shellscript
    pip install face_recognition
    ```

After installation you can download source code of the project. In command line go to place, where you want to download code and type `git clone https://gitlab.com/Lukaszz99/facerecognition.git`.\
When cloning is finished go to `facerecognition` folder.\
Now you can run face recognition application. Type `python main.py -e encodings/example_set.pickle -d cnn`.\
After few seconds you should see video from your computer's camera.\
Instructions how to make your own .pickle file (this file contains coded faces for recognition) are in face_encode.py

Code documentation is available in this link.
