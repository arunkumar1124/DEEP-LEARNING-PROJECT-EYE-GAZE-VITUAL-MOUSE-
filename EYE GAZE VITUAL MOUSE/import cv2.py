import cv2
import mediapipe as mp
import pyautogui
import pyttsx3
import speech_recognition as sr
import threading
import time

# Voice commands mapping
voice_commands = {
    "open Google Chrome": "open google chrome",
    "open YouTube": "open youtube",
    "search in YouTube": "search in youtube"
}

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Create a text-to-speech engine
engine = pyttsx3.init()

# Function to execute voice commands
def execute_command(command):
    if command == "open google chrome":
        pyautogui.hotkey('win', 'r')
        pyautogui.write("chrome")
        pyautogui.press('enter')
    elif command == "open youtube":
        pyautogui.hotkey('win', 'r')
        pyautogui.write("chrome")
        pyautogui.press('enter')
        pyautogui.write("https://www.youtube.com/")
        pyautogui.press('enter')
    elif command == "search in youtube":
        engine.say("Please provide the search term for YouTube.")
        engine.runAndWait()
        
        # Listen for the search term
        with sr.Microphone() as source:
            print("Listening for the search term...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        
        try:
            search_term = recognizer.recognize_google(audio)
            print("Search term:", search_term)
            pyautogui.hotkey('win', 'r')
            pyautogui.write("chrome")
            pyautogui.press('enter')
            pyautogui.write("https://www.youtube.com/")
            pyautogui.press('enter')
            pyautogui.hotkey('ctrl', 'f')
            time.sleep(1)
            pyautogui.write(search_term)
            pyautogui.press('enter')
        except sr.UnknownValueError:
            print("Could not understand the search term")
            return

# Function to continuously listen for voice commands
def listen_for_commands():
    while True:
        with sr.Microphone() as source:
            print("Listening for a command...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        
        try:
            text = recognizer.recognize_google(audio)
            print("Recognized:", text)
            if text in voice_commands:
                execute_command(voice_commands[text])
                engine.say("Command executed")
                engine.runAndWait()
            else:
                print("Unknown voice command")
        except sr.UnknownValueError:
            print("Could not understand your voice command")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service:", e)

# Start the voice recognition thread
voice_thread = threading.Thread(target=listen_for_commands)
voice_thread.daemon = True
voice_thread.start()

# Face mesh initialization and webcam loop
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 1:
                screen_x = screen_w * landmark.x
                screen_y = screen_h * landmark.y
                pyautogui.moveTo(screen_x, screen_y)
        
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        
        if (left[0].y - left[1].y) < 0.02:
            pyautogui.click()
            pyautogui.sleep(1)
    
    cv2.imshow('Eye Controlled Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close OpenCV windows
cam.release()
cv2.destroyAllWindows()