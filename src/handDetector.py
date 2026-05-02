import cv2
import mediapipe as mp

class HandDetector:
    #constructor
    def __init__(self, max_hands = 2, detection_confidence=0.7, tracking_confidence=0.7):
        self.mp_hands = mp.solution.hands
        self.mp_draw = mp.solutions.drawing_utils

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=max_hands,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence
        )
    """
    converts image to RGB for mediapipe, creates empty list of hands found in frame
    
    """
    def find_hands(self, frame, draw=True):
        detected_hands = []

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.hands.process(rgb_frame)

        if not results:
            return detected_hands
        
        height, width, channels = frame.shape

        for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
            landmarks = []

            label = "Unknown"

            if results.multi_handedness:
                label = results.multi_handedness[i].classification[0].label

            for landmark in hand_landmarks.landmark:
                x = int(landmark.x * width)
                y = int(landmark.y * height)

                landmarks.append((x,y))

            detected_hands.append({
                "label": label,
                "landmarks": landmarks

            })

            if draw:
                self.mp_draw.draw_landmarks(
                    frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS
                )
        return detected_hands

                
    
