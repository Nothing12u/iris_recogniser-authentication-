import cv2
import pyttsx3
import os  

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Load the pre-trained Haar Cascade for face detection
load = cv2.CascadeClassifier('c:/fr/haarcascade_frontalface_default.xml')

# Open the camera
cap = cv2.VideoCapture(0)

# Create the face recognizer
rec = cv2.face.LBPHFaceRecognizer_create()

# Load the trained data (make sure the path is correct)
rec.read("c:/fr/recognizer/TraningData1.yml")

# Define the font for text
font = cv2.FONT_HERSHEY_COMPLEX_SMALL

# Read the user data
f = open("c:/fr/datatext.txt", "r")
user = {}
for x in f:
    y, z = x.split(" ", 1)  # Ensure the split works even with extra spaces
    user[y] = z.replace("\n", "")

while True:
    # Capture frame from camera
    status, img = cap.read()

    # Convert the captured frame to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = load.detectMultiScale(gray, 1.3, 5)

    # Loop through the detected faces
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Predict the id and confidence level of the detected face
        id, conf = rec.predict(gray[y:y + h, x:x + w])

        if conf < 75:  # Confidence check for face recognition
            name = user.get(str(id), "Unknown")  # Use 'Unknown' if no match is found
        else:
            name = "Unknown"

        # Use text-to-speech to announce the name
        engine.say(name)
        engine.runAndWait()

        # Display the name on the image
        cv2.putText(img, str(name), (x, y + h + 20), font, 0.8, (255, 255, 255), 2)

    # Show the resulting image with face recognition
    cv2.imshow('FaceDetect', img)

    # Exit the loop when 'q' is pressed
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

# Close everything when done
f.close()
cap.release()
cv2.destroyAllWindows()

