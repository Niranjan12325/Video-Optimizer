# 🎥 Video Streaming Optimizer (Simulation Project)

## 📌 Overview
This project simulates a video streaming system under bandwidth constraints. It calculates **frame-wise buffering delay** based on video size and available network bandwidth.

The goal is to understand how **network speed affects video playback performance**.

---

## 🚀 Features
- Reads video file frame-by-frame  
- Simulates network bandwidth conditions  
- Calculates buffering delay for each frame  
- Visualizes delay using graph  
- Real-time video playback simulation  
- Displays performance metrics  

---

## 🛠️ Technologies Used
- Python  
- OpenCV  
- Matplotlib  

---

## 📂 Project Structure
VideoStreamingOptimizer/
│
├── main.py # Main simulation script
├── sample-5s.mp4 # Sample video file
├── README.md # Project documentation


---

## ⚙️ Installation

### 1. Clone the Repository
git clone https://github.com/your-username/video-streaming-optimizer.git
cd video-streaming-optimizer


### 2. Install Dependencies
pip install opencv-python matplotlib


---

## ▶️ How to Run
python main.py


---

## ⚙️ Configuration
Modify this parameter in the code:
simulated_bandwidth = 500 # KB/s


- Increase bandwidth → smoother playback  
- Decrease bandwidth → more buffering delay  

---

## 🎮 How It Works
1. Loads a video file using OpenCV  
2. Calculates each frame’s size in KB  
3. Simulates network delay based on bandwidth  
4. Adds delay before displaying each frame  
5. Stores delay values for analysis  
6. Plots delay vs frame number graph  

---

## 📊 Output

### Console Output
- Total Frames processed  
- Average Frame Delay  

### Graph Output
- X-axis → Frame Number  
- Y-axis → Delay (seconds)  

---

## 📈 Example Insight
- Large frames → higher delay  
- Low bandwidth → more buffering  
- Helps understand adaptive streaming concepts (like YouTube, Netflix)  

---

## 🔮 Future Improvements
- Adaptive bitrate streaming (ABR)  
- Real-time network fluctuation simulation  
- Compression optimization  
- Web-based streaming dashboard  
- Integration with machine learning for prediction  

---

## 👨‍💻 Author
Niranjan E  
Email: 126003183@sastra.ac.in  

---

## ⭐ If you like this project
Give it a ⭐ on GitHub and share!
