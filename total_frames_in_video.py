import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture('sample.mp4')

if not cap.isOpened():
    print("Error opening video file")
    exit()
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("Total frames in the video:", total_frames)

# Get the video's duration in seconds
fps = cap.get(cv2.CAP_PROP_FPS)
duration = total_frames / fps

# Calculate the frame rate (frames per second)
frame_rate = total_frames / duration

# Print the frame rate
print("Frame rate:", frame_rate)
cap.release()

