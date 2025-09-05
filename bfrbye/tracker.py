import cv2
import mediapipe as mp
import winsound
import time
import threading
from datetime import datetime

from bfrbye.dialog import show_input_dialog
from bfrbye.storage import save_response


#PICDIR = "./pics/"
#PICFORMAT = ".jpg"

class HandTracker:
    def __init__(self, config):
        self.config = config
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mp_face_detection=mp.solutions.face_detection.FaceDetection(min_detection_confidence=0.7)
        self.webcam = cv2.VideoCapture(0)
        self.counter = 0
        self.mp_drawing=mp.solutions.drawing_utils

    def run(self):
        while self.webcam.isOpened():
            ret, img = self.webcam.read()
            if not ret:
                break

            # face detection using MediaPipe
            img =cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            self.results_face=self.mp_face_detection.process(img)
            self.results_hands = self.hands.process(img)

            if self.results_hands.multi_hand_landmarks and self.results_face.detections:
                picked, img = self.detect_hand_on_face(img)
                if picked:
                    winsound.Beep(1500, 1000) # frequency in Hz, duration in ms
                    #filename = PICDIR + datetime.now().strftime('%Y%m%d-%H%M%S') + PICFORMAT
                    #cv2.imwrite(filename,img)
                    response = []
                    thread = threading.Thread(target = show_input_dialog, args=(response,))
                    thread.start()
                    thread.join()
                    
                    if len(response):
                        save_response(response[0], self.config)
            
        time.sleep(2)


        self.webcam.release()
        cv2.destroyAllWindows()

    def detect_hand_on_face(self, img):
        picked = 0
        if self.results_face.detections:
            for detection in self.results_face.detections:
                face_box = detection.location_data.relative_bounding_box
                self.mp_drawing.draw_detection(img,detection)
        
        if self.results_hands.multi_hand_landmarks:
            for hand_landmarks in self.results_hands.multi_hand_landmarks:
                for node in hand_landmarks.landmark:

                    xmax = face_box.xmin + face_box.width
                    ymax = face_box.ymin + face_box.height

                    if((node.x > face_box.xmin and node.x < xmax) and (node.y > face_box.ymin and node.y < ymax)):
                        picked +=1
                        self.counter+=1
                        print(self.counter)
                        break
                self.mp_drawing.draw_landmarks(img, hand_landmarks, connections=self.mp_hands.HAND_CONNECTIONS)
            
            

            return True if picked>0 else False, img
        
        return False, None
