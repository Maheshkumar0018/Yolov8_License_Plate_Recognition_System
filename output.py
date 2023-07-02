import cv2

video_path = './out.mp4'
cap = cv2.VideoCapture(video_path)
window_width = 640
window_height = 480
cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Frame', window_width, window_height)
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Frame', frame)
    else:
        print('Error occurred')
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
