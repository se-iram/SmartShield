# SmartShield: Real-Time Face Verification App using Siamese Neural Network

## 📌 Overview
FaceMatch is a facial recognition system trained from scratch using a Siamese Neural Network built with TensorFlow. It compares two face images and tells if they belong to the same person.

## 🎯 Problem Statement
Traditional login systems or security checks require passwords or badges. This app uses facial recognition as a secure and user-friendly alternative.

## 🧰 Tech Stack
- Python
- TensorFlow / Keras
- OpenCV
- Kivy (for local GUI) or Streamlit
- NumPy, Pandas
- GitHub for version control

## 📂 Dataset
We used [FaceScrub Dataset](link here) to train the Siamese Network.
Images are preprocessed to grayscale 100x100 pixels.

## 🧠 ML Model
- Architecture: Custom Siamese CNN
- Loss: Contrastive Loss
- Training Epochs: 15
- Accuracy Achieved: 94%

See `train_model.ipynb` for full training code.

## 🚀 How to Run

```bash
git clone https://github.com/yourname/facematch.git
cd facematch
pip install -r requirements.txt
python app.py
