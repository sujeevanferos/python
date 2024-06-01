import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Hands and Drawing modules
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Open the webcam
cap = cv2.VideoCapture(0)

# Track previous y position of index finger tip for scrolling detection
previous_y = None
scroll_threshold = 20  # Minimum movement to trigger a scroll

with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Flip the frame horizontally for a later selfie-view display
        frame = cv2.flip(frame, 1)

        # Convert the BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame and detect hands
        results = hands.process(rgb_frame)

        # Draw hand landmarks and handle scrolling
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Get the y position of the index finger tip
                index_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * frame.shape[0]

                if previous_y is not None:
                    # Determine scroll direction based on movement
                    if abs(index_tip_y - previous_y) > scroll_threshold:
                        if index_tip_y < previous_y:
                            pyautogui.scroll(5)  # Scroll up
                        else:
                            pyautogui.scroll(-5)  # Scroll down

                # Update previous y position
                previous_y = index_tip_y

        else:
            previous_y = None  # Reset if no hand is detected

        # Display the frame
        cv2.imshow('Hand Gesture Scrolling', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
