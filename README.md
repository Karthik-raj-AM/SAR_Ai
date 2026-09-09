# SAR_Ai 🚁

## AI-Based Search and Rescue Survivor Detection System

**SAR_Ai** is an AI-powered computer vision project designed to assist **Search and Rescue (SAR) operations** by detecting survivors from aerial imagery and live camera feeds.

The project uses **YOLO-based object detection** to identify people/survivors in challenging environments such as forests, mountains, disaster-affected areas, and other locations where manual search can be difficult or dangerous.

The long-term goal is to integrate the trained AI model with a **search-and-rescue drone**, enabling autonomous or assisted survivor detection during aerial missions.

---

## 🎯 Project Objective

The primary objective of SAR_Ai is to develop a lightweight and practical AI system capable of:

* Detecting survivors from aerial images
* Detecting people using a live camera
* Processing drone camera footage
* Training a custom object-detection model
* Testing trained models on new images
* Providing a foundation for future autonomous drone integration

The system is intended to support rescue teams by helping them identify potential survivors more quickly over large search areas.

---

## 🧠 Technology Stack

| Technology   | Purpose                            |
| ------------ | ---------------------------------- |
| Python       | Main programming language          |
| YOLO         | Object detection                   |
| OpenCV       | Image and camera processing        |
| PyTorch      | Deep learning framework            |
| NumPy        | Numerical operations               |
| Git          | Version control                    |
| GitHub       | Source-code management             |
| Raspberry Pi | Planned onboard computing platform |
| Drone        | Planned aerial deployment platform |

---

## 📂 Project Structure

```text
SAR_Ai/
│
├── .gitignore
│
├── README.md
│
├── train.py
│   └── Train the custom YOLO detection model
│
├── test_ai.py
│   └── Test the AI detection pipeline
│
├── test_trained.py
│   └── Test the trained model on images
│
├── live_ai.py
│   └── Run AI detection using a live camera feed
│
├── camera_ai.py
│   └── Camera-based AI detection
│
└── dataset/
    └── data.yaml
        └── Dataset configuration for YOLO
```

> Training images and labels are intentionally excluded from the repository when they are large or covered by `.gitignore`.

---

# 🚀 Features

### 1. Custom AI Training

SAR_Ai supports training a custom object-detection model using a dedicated search-and-rescue dataset.

The model can be trained to recognize survivors/people from aerial imagery.

### 2. Aerial Image Detection

The trained model can be tested on images captured from drones or other aerial platforms.

This is particularly useful for environments such as:

* 🌲 Dense forests
* ⛰️ Mountainous terrain
* 🌧️ Disaster-affected regions
* 🏚️ Damaged structures
* 🌾 Large open areas
* 🏞️ Difficult-to-access locations

### 3. Live Camera Detection

The project includes camera-based detection functionality.

A webcam can be used during development to test the AI model before deploying it onto a drone.

### 4. Custom Dataset

The project uses a custom dataset configured through:

```text
dataset/data.yaml
```

This allows the model to be trained specifically for the intended Search and Rescue application.

### 5. Future Drone Integration

The AI system is being developed with eventual drone deployment in mind.

A future version can combine:

```text
Drone Camera
     ↓
Raspberry Pi
     ↓
YOLO AI Model
     ↓
Survivor Detection
     ↓
GPS Coordinates
     ↓
Ground Station / Rescue Team
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/Karthik-raj-AM/SAR_Ai.git
```

Enter the project directory:

```bash
cd SAR_Ai
```

---

## 2. Create a Python virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

---

## 3. Install dependencies

Install the required packages used by the project.

For example:

```bash
pip install ultralytics opencv-python numpy torch torchvision
```

Depending on the model and hardware being used, additional dependencies may be required.

---

# 📊 Dataset Configuration

The YOLO dataset configuration is stored in:

```text
dataset/data.yaml
```

The configuration defines information such as:

* Training dataset location
* Validation dataset location
* Number of classes
* Class names

Example:

```yaml
path: ../dataset

train: images/train
val: images/val

names:
  0: survivor
```

The exact configuration should match the dataset structure being used.

---

# 🏋️ Model Training

The main training script is:

```text
train.py
```

Run:

```bash
python train.py
```

The training process produces a trained YOLO model that can subsequently be used for testing and live detection.

Training performance will depend on:

* Dataset size
* Image quality
* Number of training epochs
* Model size
* GPU availability
* Dataset diversity
* Annotation quality

---

# 🧪 Testing the Model

After training, the trained model can be tested using:

```bash
python test_trained.py
```

Additional testing functionality is available through:

```bash
python test_ai.py
```

These scripts are intended to help evaluate the detection pipeline and model performance.

---

# 📷 Live Camera Detection

The project includes live camera functionality.

Run:

```bash
python live_ai.py
```

A webcam can be used during development to verify that the trained model can perform real-time detection.

Camera-based testing is useful before attempting deployment on an aerial platform.

---

# 🖥️ Development Workflow

The current development workflow is:

```text
Dataset Collection
        ↓
Image Annotation
        ↓
Dataset Preparation
        ↓
YOLO Training
        ↓
Model Testing
        ↓
Webcam Testing
        ↓
Aerial Image Testing
        ↓
Drone Integration
```

---

# 🚁 Planned Drone Architecture

The long-term objective is to integrate SAR_Ai into an autonomous search-and-rescue drone.

A possible architecture is:

```text
                 ┌────────────────────┐
                 │   Drone Camera     │
                 └─────────┬──────────┘
                           ↓
                 ┌────────────────────┐
                 │   Raspberry Pi     │
                 │                    │
                 │   YOLO AI Model    │
                 └─────────┬──────────┘
                           ↓
                 ┌────────────────────┐
                 │ Survivor Detection │
                 └─────────┬──────────┘
                           ↓
                 ┌────────────────────┐
                 │ Position / GPS     │
                 └─────────┬──────────┘
                           ↓
                 ┌────────────────────┐
                 │ Ground Station     │
                 │ / Rescue Team      │
                 └────────────────────┘
```

---

# 🔮 Future Development

The project is currently focused on developing and testing the AI detection system.

Planned improvements include:

### AI Improvements

* Improve dataset size and quality
* Increase detection accuracy
* Reduce false detections
* Improve detection in dense vegetation
* Improve detection at different altitudes
* Test different YOLO model sizes
* Optimize the model for edge computing

### Drone Integration

* Raspberry Pi deployment
* Real-time onboard inference
* Drone camera integration
* GPS-based survivor location
* Automatic search-area coverage
* Autonomous waypoint missions
* Geofencing
* Ground-station communication

### Advanced Detection

Future versions may explore:

* Human detection in difficult terrain
* Thermal-camera-based detection
* Multi-camera detection
* Night-time search
* Object tracking
* Survivor location estimation
* AI-assisted search patterns

---

# 📈 Current Development Status

| Component               | Status            |
| ----------------------- | ----------------- |
| Python environment      | ✅                 |
| YOLO development        | ✅                 |
| Dataset preparation     | ✅                 |
| Dataset configuration   | ✅                 |
| Custom training script  | ✅                 |
| Model testing scripts   | ✅                 |
| Live camera testing     | ✅                 |
| GitHub repository       | ✅                 |
| Aerial testing          | 🔄 In development |
| Raspberry Pi deployment | 🔜 Planned        |
| Drone integration       | 🔜 Planned        |
| Autonomous SAR mission  | 🔜 Planned        |

---

# ⚠️ Limitations

SAR_Ai is currently a research and development project.

Detection performance can vary depending on:

* Camera resolution
* Flight altitude
* Lighting conditions
* Weather
* Vegetation density
* Survivor visibility
* Dataset quality
* Model configuration

The system should therefore be treated as an **AI-assisted search tool**, not as a replacement for trained search-and-rescue personnel.

---

# 🤝 Contributions

Contributions and suggestions are welcome.

Potential areas for contribution include:

* Dataset improvement
* Model optimization
* Computer vision
* Drone integration
* Embedded AI
* Autonomous navigation
* Search-and-rescue algorithms

---

# 📜 License

This project is currently under development.

A suitable open-source license can be added once the project's distribution requirements are finalized.

---

# 👨‍💻 Project

**SAR_Ai**

AI-based Search and Rescue Survivor Detection

Built with:

**Python • YOLO • OpenCV • PyTorch • Computer Vision • Drone Technology**

---

## ⭐ Project Vision

> **Use AI and autonomous drones to help rescue teams find survivors faster in areas that are difficult, dangerous, or too large to search manually.**

This project is being developed as a foundation for a future **AI-enabled Search and Rescue drone system**.
