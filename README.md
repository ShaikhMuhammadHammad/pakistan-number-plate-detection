# pakistan-number-plate-detection

# 🇵🇰 Pakistani Number Plate Detection using YOLOv8 🚗

This project implements a real-time object detection model specifically trained to detect number plates on Pakistani vehicles (cars and bikes) using **YOLOv8**. The dataset was custom-built using publicly available images from Kaggle and self-captured images, annotated with CVAT.

---

## 🔍 Project Overview

Due to the limited availability of localized datasets for license plate detection in Pakistan, this project focuses on building a dataset from scratch and training a deep learning model using the YOLOv8 object detection framework. The model was tested on images and videos for real-world performance.

---

## 🧰 Tools & Technologies

- **Python 3.10**
- **YOLOv8 (Ultralytics)**
- **OpenCV**
- **CVAT (for annotation)**
- **PyTorch**
- **Kaggle Datasets + Self-captured images**

---

## 🗂️ Folder Structure
pakistan-number-plate-detection/
│
├── config.yaml # YOLOv8 dataset config file
├── test.py # Run inference on test images
├── test_video.py # Run inference on videos
├── videos/ # Test videos
├── images/
│ ├── train/ # Training images
│ ├── val/ # Validation images
│ └── test/ # Test images
├── labels/
│ ├── train/ # Training labels (YOLO format)
│ ├── val/ # Validation labels
├── runs/ # Output from training (excluded from repo)
├── README.md
└── .gitignore
