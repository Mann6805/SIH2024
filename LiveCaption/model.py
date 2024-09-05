import speech_recognition as sr
import cv2

# Initialize speech recognizer
recognizer = sr.Recognizer()

# Initialize OpenCV Video Capture
cap = cv2.VideoCapture(0)

while True:
    # Capture video frame
    ret, frame = cap.read()
    if not ret:
        break

    # Display video frame
    cv2.imshow('Video Feed', frame)

    # Capture audio and process with SpeechRecognition
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        try:
            caption = recognizer.recognize_google(audio)
            print("Recognized Text:", caption)
        except sr.UnknownValueError:
            caption = "Could not understand audio"
        except sr.RequestError:
            caption = "Could not request results"

    # Overlay text on the video frame
    if caption:
        text_size = cv2.getTextSize(caption, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0]
        text_x = (frame.shape[1] - text_size[0]) // 2
        text_y = frame.shape[0] - 20
        cv2.putText(frame, caption, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Exit loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()