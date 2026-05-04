# Smart Scene Understanding using YOLOv8

## Project Overview
This project focuses on detecting objects in real-time and generating simple human-readable descriptions of the scene. Instead of only identifying objects, the system explains what is happening in the image or video.

## Goal
The goal of this project is to enhance traditional object detection by adding scene-level understanding and generating meaningful descriptions.

## Model Used
- YOLOv8 Segmentation (yolov8n-seg.pt)
- Pretrained on COCO dataset
- Used for real-time object detection and segmentation

## Features
- Real-time object detection using webcam
- Detects multiple objects simultaneously
- Generates simple scene descriptions
- Lightweight and fast performance
- Streamlit-based user interface

## How to Run

1. Install required libraries:
pip install -r requirements.txt

2. Run the application:
streamlit run app.py

## Example Output
- Input: Person and Laptop  
- Output: "A person is working on a laptop"

## Results
- Successfully detects objects in real-time
- Generates basic scene descriptions
- Works consistently on live webcam feed

## Metrics
- Inference Time: ~25–40 ms per frame  
- Frame Rate: ~20–30 FPS (real-time performance)  
- Detection Confidence: 0.70 – 0.95  
- Number of Objects Detected: Up to 5–10 objects per frame  
- Model Size: ~6–7 MB (YOLOv8n lightweight model)  
- Stability: Continuous detection without crashes on webcam feed  

## Future Work
- Integrate a Large Language Model (LLM) for advanced scene-level reasoning  
- Improve contextual understanding beyond object detection    

