# iris_recogniser-authentication-
security

Iris Recognition System (Eye-Based Authentication)
This project implements a simple biometric authentication system using OpenCV and the Local Binary Patterns Histograms (LBPH) algorithm. Instead of traditional face recognition, this system is adapted to recognize the iris/eye region based on features extracted from captured eye images.

Table of Contents
Overview





Overview
The system consists of three main scripts:

Creater.py: Captures images of the user's eye (iris region) and saves them for training. It also registers the user's ID and name.

trainer.py: Trains the LBPH recognizer using the captured eye images.

Recognizer.py: Uses the trained model to detect and identify a user's eye in real-time via the webcam, announcing the recognized name using Text-to-Speech (TTS).

Prerequisites
You need to have Python installed on your system. The following Python libraries are required:

File Descriptions
Setup and Usage
1. Folder Structure Setup
You need to manually create the necessary folders:

Note: Ensure the haarcascade_eye.xml is accessible to OpenCV, as the code uses cv2.data.haarcascades to load it.

2. Data Collection (Creater.py)
Run this script to enroll new users.

Enter the Username and a Unique ID (e.g., 1, 2, 3).

The script will capture 30 images of your eye region and save them in the Data/ folder (e.g., Data/1.1.jpg, Data/1.2.jpg, etc.).

Your ID and name will be logged in c:/fr/datatext.txt.

3. Training (trainer.py)
After collecting data for one or more users, run the training script.

This will train the LBPH recognizer.

The trained model (IrisTrainer.yml) will be saved to C:/fr/recognizer/. You must run this script again every time you add a new user.

4. Recognition (Recognizer.py)
Run the main script for real-time iris authentication.

The webcam will open.

When an eye is detected, the system will attempt to predict the user.

If recognized (confidence < 70), the name will be displayed and spoken via TTS.

Press q to exit the recognition loop.

Workflow
Enroll User: Run Creater.py to capture eye images and register ID/Name.

Train Model: Run trainer.py to update the recognition model.

Authenticate: Run Recognizer.py for real-time identification.
