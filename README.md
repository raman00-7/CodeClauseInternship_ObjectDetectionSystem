# 🧠 Object Detection System using YOLOv5
> Internship Project | CodeClause | July 2025  
> Developed by: **Raman Kumar**

---

## 📌 Project Overview

This is an AI-based Object Detection System built using **YOLOv5**, capable of detecting multiple objects in real-time using a webcam or from static images.

The model used is **YOLOv5m**, a pre-trained model trained on the **COCO dataset**, which recognizes 80 common objects like people, cars, laptops, bottles, etc.

---

## 🎯 Aim

> Build a system that detects and classifies objects in images or video streams using deep learning.

---

## ✅ Features

- 🔍 Real-time object detection via webcam  
- 🖼️ Static image detection  
- 📦 Bounding boxes with confidence scores  
- ⚡ Optimized for smoother CPU performance on Mac M2  
- 🧪 Tested with `yolov5s.pt` and `yolov5m.pt`

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| YOLOv5 (Ultralytics) | Pre-trained object detection model |
| OpenCV | Image & video stream handling |
| NumPy | Array and image data operations |
| Matplotlib | Optional visualization (for images) |

---

## 🖼️ Demo

### 📷 Static Image Detection

```bash
python3 main.py  # When using image mode
```

## 📹 Real-Time Webcam Detection
```bash
python3 main.py  # With webcam code enabled
```
*Press q to exit webcam view.

## 📁 Folder Structure

<pre>

ObjectDetectionSystem/
├── main.py             # Detection code (image & webcam)
├── requirements.txt    # Required Python packages
├── README.md           # This file
├── yolov5s.pt / yolov5m.pt  # Auto-downloaded model
├── sample.jpg          # Sample image for testing

</pre>

## 🧪 Installation & Setup:

	1.	Clone this repo (or download it)
	2.	Install requirements:

    ```bash
    pip install -r requirements.txt
    ```
    3.	Add your own image as sample.jpg (optional)
	4.	Run the code:

    ```bash
    python3 main.py
    ```
## 🔍 Object Classes Detected

Based on the COCO dataset:  
	•	People, Cars, Bikes, Bottles, Laptops, Phones, Animals, Chairs, and many more (80+ classes)  

⸻

## 🎓 What I Learned
	•	Real-time object detection with YOLOv5  
	•	Model integration with Python + OpenCV  
	•	Optimizing ML models for CPU-based environments  
	•	Handling video frames and image processing  

⸻

## 💼 Internship Info
	•	Internship Domain: Artificial Intelligence Intern  
	•	Project ID: #CC3600  
	•	Project Title: Object Detection System  
	•	Organization: CodeClause  
	•	Project Duration: 01 July 2025 – 31 July 2025  

⸻

## 🔗 Project Link

📎 GitHub Repository: https://github.com/galaxy00-7/CodeClauseInternship_ObjectDetectionSystem

⸻

## 🙌 Acknowledgements

Thanks to:
	•	Ultralytics YOLOv5  
	•	CodeClause for the opportunity  
