import cv2
import matplotlib.pyplot as plt
import os

# -----------------------------
# Video Streaming Optimizer
# -----------------------------

# Replace this with the path to your video file
video_file = r'C:\Users\niran\OneDrive\Documents\GitHub\video optimizer\sample-5s.mp4'

# Check if the video file exists
if not os.path.exists(video_file):
    print("Error: Video file not found!")
    exit()

# Simulated network bandwidth in KB/s
simulated_bandwidth = 500

# Open the video file
cap = cv2.VideoCapture(video_file)
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

frame_delays = []
frame_count = 0

# Process video frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Calculate simulated buffering delay based on frame size
    frame_size = frame.nbytes / 1024  # Convert bytes to KB
    delay = frame_size / simulated_bandwidth
    frame_delays.append(delay)
    frame_count += 1

    # Display the frame
    cv2.imshow("Video Streaming Optimizer", frame)

    # Press 'q' to quit early
    if cv2.waitKey(int(delay * 1000)) & 0xFF == ord('q'):
        break

# Release video resources
cap.release()
cv2.destroyAllWindows()

# -----------------------------
# Plot buffering delays
# -----------------------------
plt.figure(figsize=(8, 4))
plt.plot(frame_delays, label='Simulated Frame Delay (s)')
plt.xlabel('Frame Number')
plt.ylabel('Delay (seconds)')
plt.title('Video Streaming Optimizer Simulation')
plt.legend()
plt.show()

# -----------------------------
# Print summary metrics
# -----------------------------
avg_delay = sum(frame_delays) / len(frame_delays)
print(f"Total Frames: {frame_count}")
print(f"Average Frame Delay: {avg_delay:.4f} seconds")
