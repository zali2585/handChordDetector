FINGER_TIPS = {
    "thumb": 4, 
    "index": 8,
    "middle": 12,
    "ring": 16,
    "pinky": 20
}

FINGER_MID = {
    "index": 6,
    "middle": 10,
    "ring": 14,
    "pinky": 18
}
"""

Compares y-coord of finger tip to finger mid
if finger tip < finger mid, tip = higher on screen
    finger is up
landmarks: list of 21 (x, y) pixel points
handedness: "Left" or "Right"
returns dict 
    "thumb": True,...etc

"""
fingers = {}
def fingers_up(landmarks, handedness):
    for finger, tip_id in FINGER_TIPS.items():
        #skip thumb bc it goes sideways
        if finger == "thumb":
            continue
        
        mid_id =  FINGER_MID[finger]
        fingers[finger] = landmarks[tip_id][1] < landmarks[mid_id][1]

        thumb_tip_x = landmarks[4][0]
        thumb_mid_x = landmarks[3][0]

        if handedness == "Right":
            fingers["thumb"] = thumb_tip_x > thumb_mid_x
        else:
            fingers["thumb"] = thumb_tip_x < thumb_mid_x
    return fingers

def count_fingers(landmarks):
    fingers = []

    # Index
    fingers.append(landmarks[8][1] < landmarks[6][1])

    # Middle
    fingers.append(landmarks[12][1] < landmarks[10][1])

    # Ring
    fingers.append(landmarks[16][1] < landmarks[14][1])

    # Pinky
    fingers.append(landmarks[20][1] < landmarks[18][1])

    return fingers