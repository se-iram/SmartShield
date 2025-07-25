# SmartShield – Face Verification Application

**SmartShield** is a functional web application that verifies a live face captured via webcam against stored anchor images using a **Siamese Neural Network** built and trained by the team. The model is trained from scratch and deployed via a Python-based backend (Flask) for real-time face-verification.

---

## Project Overview

SmartShield enables real-time identity verification by comparing live webcam input with reference ("anchor") images. The system computes similarity scores using a trained Siamese model and classifies the input as either "Verified" or "Unverified" based on a threshold.

This system respects all hackathon rules:
- Machine learning model trained entirely by the team.
- No usage of LLM APIs or pretrained wrappers (e.g. ChatGPT, BERT).
- All code (training, ML model, backend, frontend) is fully open sourced.
- Includes frontend and backend components.
- Deployed live for user testing.
:contentReference[oaicite:1]{index=1}

---

## Repository Structure

- smart-shield/
 - ├── app.py # Backend server (Flask or Gradio)
 - ├── utils.py # Model loading, preprocessing, and inference
 - ├── requirements.txt # Python dependencies
 - ├── anchor/ # Anchor reference images for verification
 - │ └── *.jpg
 - ├── input.jpg # Saved image captured during runtime
 - ├── model/
 - │ └── siamesemodel/ # SofaedModel folder (TensorFlow format)
 - │ ├── saved_model.pb
 - │ └── variables/
 - ├── templates/ # HTML templates (if using Flask)
 - │ └── index.html
 - ├── static/
 - │ ├── style.css # Custom styles
 - │ └── app.js # Client-side logic
 - └── README.md # This file

---

## 🚀 Tech Stack

| Layer              | Technology              | Purpose                                                                 |
|--------------------|--------------------------|-------------------------------------------------------------------------|
| **Frontend**       | HTML5, CSS3, JavaScript  | Build the user interface, render camera stream, and handle interactions |
| **Styling**        | Bootstrap 5              | Ensure responsive and modern design                                     |
| **Backend**        | Python (Flask)           | Provide REST API endpoints, manage server-side logic                    |
| **Machine Learning** | TensorFlow             | Train and run the Siamese Neural Network for face verification          |
| **Image Processing** | OpenCV                 | Capture webcam input, save images, and manage frame data                |
| **Utilities**      | NumPy, OS                | Perform numerical operations and handle filesystem tasks                |
| **Deployment**     | Hugging Face Spaces / Gradio (optional) | Host the project online for demo/testing                       |
| **Version Control**| Git, GitHub              | Manage project versions and collaborate using Git repositories          |

---

## Installation & Running Locally

### Requirements
- Python 3.10
- A webcam (for live testing)
- Optional: Virtual environment

### Steps
```bash
git clone https://github.com/your-username/smart-shield-app.git
cd smart-shield-app
python -m venv env
# Activate virtual env (Windows: env\Scripts\activate, Mac/Linux: source env/bin/activate)
pip install -r requirements.txt
python app.py
```
Open a browser to http://127.0.0.1:5000/. Use the Start Camera button to enable the camera, then Verify Face to test match results.

---
### How It Works
- Preprocessing
- Input images resize to (105 × 105 × 3)
- Scaling using normalized pixel values ([0,1] range)
- Model Inference
- Siamese network compares anchor vs live frame
- Outputs similarity score between 0–1
- Decision Logic
- If score > threshold (default 0.5), returns Verified
- Otherwise returns Unverified
### UI Flow
- User clicks Start Camera
- Webcam feed appears
- User clicks Verify Face
- Server saves frame, computes similarity, returns result
- UI displays result in green/red text accordingly

---

### Model Training Details
- Architecture: Siamese Neural Network (custom L1Dist layer)
- Training performed in a Jupyter notebook/Colab:
- Anchor, positive, negative image sampling
- Used TensorFlow 2.x, trained from scratch
- Model saved as TensorFlow SavedModel via model.export()

---

### Deployment Notes
- For lightweight deployment and demos, the project can be deployed on:
  - Hugging Face Spaces using Gradio or Flask with static hosting
  - Render, Railway, or Heroku (for Flask backend)
  - Ensure model/siamesemodel is compressed if over 25MB for GitHub compatibility

---

### Author
 - Iram Hameed
 - GitHub: se-iram
 - Contact: eramhameed5@gmail.coom
