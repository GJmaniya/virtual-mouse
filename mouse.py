# use for a install cv2 a "pip install opencv-python" this line for latest version 3.11.0
import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)
hand_det = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0

while True:
    ret, frame = cap.read()
    frame_height, frame_width, _ = frame.shape
    frame = cv2.flip(frame, 1)
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_det.process(rgb_frame)
    hands = output.multi_hand_landmarks 

    if hands:  # Check if hands is not None
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            for id, landmark in enumerate(hand.landmark):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                # print(x, y)
                if id == 8:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    index_x = int(screen_width / frame_width * x)
                    index_y = int(screen_height / frame_height * y)
                    pyautogui.moveTo(index_x, index_y)
                if id == 4:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    thumb_x = int(screen_width / frame_width * x)
                    thumb_y = int(screen_height / frame_height * y)
                    print(abs(index_y - thumb_y))
                    if abs(index_y - thumb_y) < 30:
                        pyautogui.click()
                        pyautogui.sleep(1)

    cv2.imshow('virtual mouse', frame)
    
    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit the loop
        break

cap.release()
cv2.destroyAllWindows()
