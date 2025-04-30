![Python](https://img.shields.io/badge/Python-3.9-blue)
![Deep Learning](https://img.shields.io/badge/DeepLearning-NVIDIA-green)
![License](https://img.shields.io/badge/license-MIT-blue.svg)


# 🚗 Self-Driving Car Using Deep Learning

This repository contains the implementation and comparison of two deep learning models—**NVIDIA’s End-to-End Model** and the **DeepDriving Model**—for autonomous vehicle simulation. The models are trained and evaluated on driving datasets to predict steering angles from input camera images.

📄 **Published in IEEE Xplore | Presented at AIIOT Conference**

---

## 📌 Project Overview

- Implemented two neural networks for autonomous driving:
  - **NVIDIA CNN-based end-to-end self driving model**
  - **DeepDriving affordance-based model**
- Trained and validated using the **Udacity Self-Driving Car Dataset**
- Conducted a comprehensive analysis on model performance and scalability
- Developed under the research theme of simulation-based driving systems

---


---

## 🔍 Key Features

- 📷 Image-based steering prediction
- 📊 Comparison of end-to-end vs. affordance learning models
- 📈 Training accuracy and loss visualization
- 📝 Well-documented research methodology

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt

## 🚀 How to Run

### NVIDIA Model Training
```bash
python Codes/train_nvidia.py

### DeepDriving Model Training
```bash
python Codes/train_deepdriving.py

## 📜 Citation

Pasumarti, Sujan & Yaganti, Pavan Sai & v, Revathi & Boopalan, G & Shanmugasundaram, S. (2024). Comparative Analysis of Neural Network Models for Autonomous Driving: A Case Study of the NVIDIA model and the DeepDriving Model. 1-6. 10.1109/AIIoT58432.2024.10574744. 

## 🔗 Links
- 📄 [Published Research Paper (IEEE Xplore)](https://ieeexplore.ieee.org/document/10574744)
- 🔬 [Dataset used](https://github.com/sujan2883/Training_data/tree/master/IMG)


