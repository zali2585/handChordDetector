print("main.py file started")

import cv2
print("cv2 imported")
from src.handDetector import HandDetector
print("handDetector imported")
from src.fingerLogic import fingers_up
print("fingersup imported")

def main():
    print("entered main")
    cap = cv2.VideoCapture(0)

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

            cv2.putText(
                frame, label, (wrist_x, wrist_y - 20), 
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