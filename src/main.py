print("main.py file started")

import cv2
print("cv2 imported")
from src.handDetector import HandDetector
print("handDetector imported")
from src.fingerLogic import fingers_up
from src.fingerLogic import count_fingers
print("fingersup imported")

def main():
    print("entered main")
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("Camera open failed.")
        return
    print("camera opened.")
    detector = HandDetector(max_hands=2)
    
    while True:
        success, frame = cap.read()
        

        if not success:
            print("Could not read frame.")
            break

        frame = cv2.flip(frame, 1)
        hands = detector.find_hands(frame,draw=True)

        for hand in hands:

            label = hand["label"]
            landmarks = hand["landmarks"]
            wrist_x, wrist_y = landmarks[0]

            fingers = count_fingers(landmarks)
            total_up = sum(fingers)
            if total_up >= 3:
                state = "Open"
            else:
                state = "Closed"

            cv2.putText(
                frame, f"{label}: {state}", (wrist_x, wrist_y - 40), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2
            )

        cv2.imshow("Hand Detector", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("nameguard passed.")
    main()