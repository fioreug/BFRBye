import time
import logging
import cv2
import mediapipe as mp
import winsound
import atexit

logging.basicConfig(
    filename="app.log",
    encoding="utf-8",
    filemode="a",
    format="{asctime} - {message}", #{levelname}
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)

def exit_handler():
    logging.info("Exiting application")

sleep = 2

mp_hands = mp.solutions.hands
mp_face_detection=mp.solutions.face_detection.FaceDetection(min_detection_confidence=0.7)
mp_drawing=mp.solutions.drawing_utils

webcam=cv2.VideoCapture(0)
picked = 0

logging.warning("Starting application")

while webcam.isOpened():
    success, img = webcam.read()

    # face detection using MediaPipe
    img =cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results_face=mp_face_detection.process(img)
    results_hands = mp_hands.Hands().process(img)
    
    if results_hands.multi_hand_landmarks and results_face.detections:

        # draw the face detection annotations on the image
        img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        
        if results_face.detections:
            for detection in results_face.detections:
                face_box = detection.location_data.relative_bounding_box
                #print(face_box.xmin)
                mp_drawing.draw_detection(img,detection)
        
        if results_hands.multi_hand_landmarks:
            for hand_landmarks in results_hands.multi_hand_landmarks:
                for node in hand_landmarks.landmark:

                    xmax = face_box.xmin + face_box.width
                    ymax = face_box.ymin + face_box.height
                    #print("{} < {} < {} ?".format(face_box.xmin, node.x, xmax))
                    #print("{} < {} < {} ?".format(face_box.ymin, node.y, ymax))
                    #print("-------------")

                    if((node.x > face_box.xmin and node.x < xmax) and (node.y > face_box.ymin and node.y < ymax)):
                        picked+=1
                        break

                mp_drawing.draw_landmarks(img, hand_landmarks, connections=mp_hands.HAND_CONNECTIONS)
            #counter+=1
            #print(counter)
    else:
        sleep = 2

    #cv2.imshow("io",img)
    
    if(picked):
        #print('\a')
        winsound.Beep(1500, 1000) # frequency in Hz, duration in ms
        print("STOP")
        logging.warning("Hands up!")
        picked=0
        sleep = 2
    
    time.sleep(sleep)
    if cv2.waitKey(100) & 0xFF == ord("q"):
        logging.info("Exiting application")
        break
