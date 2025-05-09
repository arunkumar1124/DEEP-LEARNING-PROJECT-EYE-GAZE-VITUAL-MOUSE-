👁️🖱️ Adaptive Eye-Gaze Virtual Mouse using Deep Learning
A hands-free human-computer interaction system that uses eye movement and facial gestures to control the mouse pointer, enabling accessible and intuitive device control for users with physical limitations.

📌 Project Description
This project introduces a deep learning-based virtual mouse system that leverages MediaPipe, CNNs, and PyAutoGUI to enable cursor control using eye gaze, blinks, and facial gestures. It provides a non-contact, vision-based interface suitable for people with motor impairments and for hands-free applications.

✨ Features
🔍 Real-time eye tracking using webcam

🖱️ Cursor movement with eye direction

👁️ Blink-based clicking gestures

🎤 Optional voice command integration

🧠 Personalized user calibration for better control

🔄 Multithreaded system for simultaneous gesture and voice input

🧰 Technologies Used
Python

OpenCV

MediaPipe (Face Mesh)

TensorFlow / Keras (for gesture recognition)

PyAutoGUI

SpeechRecognition + pyttsx3 (voice control)

🧠 System Architecture
Eye Movement Detection

Uses MediaPipe FaceMesh to extract facial landmarks.

Tracks movement of eye landmarks and maps them to screen coordinates.

Gesture Recognition

Eye blinks and head gestures (like nods) mapped to mouse click actions.

Mouse Control & Interaction

PyAutoGUI simulates mouse movement and click events.

Optional voice commands trigger complex interactions.

Multithreading

Eye tracking and voice recognition run concurrently using threading.

📦 Installation
bash
Copy
Edit
git clone [https://github.com/your-username/eye-gaze-virtual-mouse.git](https://github.com/arunkumar1124/DEEP-LEARNING-PROJECT-EYE-GAZE-VITUAL-MOUSE-.git)
cd eye-gaze-virtual-mouse
pip install -r requirements.txt
▶️ Running the Application
bash
Copy
Edit
python main.py
Make sure your webcam is connected and accessible.

📈 Results & Performance
Gesture classification accuracy: ~95%

Real-time processing: < 0.5 seconds latency

Cursor tracking smoothness: Highly responsive

🧪 Future Improvements
Add drag and drop

Expand to AR/VR interactions

Integrate gaze-based keyboard

Use deep CNN for improved gesture classification

🧑‍💻 Authors
Arunkumar M (221501013)

Charu Stash P (221501021)
Department of Artificial Intelligence and Machine Learning
Rajalakshmi Engineering College, Thandalam

📜 License
This project is licensed under the MIT License.
