from flask import Flask, render_template, Response, request, jsonify
import cv2
import os
from utils import verify
import threading

app = Flask(__name__)

frame = None
camera = None
capture_thread = None
capture_active = False
INPUT_IMG_PATH = 'input.jpg'


def gen_frames():
    global frame, camera, capture_active

    while capture_active:
        success, img = camera.read()
        if not success:
            break
        frame = img.copy()
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


@app.route('/start_camera', methods=['POST'])
def start_camera():
    global camera, capture_active, capture_thread
    if not capture_active:
        camera = cv2.VideoCapture(0)
        capture_active = True
    return jsonify({'status': 'started'})


@app.route('/stop_camera', methods=['POST'])
def stop_camera():
    global camera, capture_active
    capture_active = False
    if camera is not None:
        camera.release()
        camera = None
    return jsonify({'status': 'stopped'})


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/verify', methods=['POST'])
def verify_face():
    global frame
    if frame is None:
        return jsonify({'result': 'No frame captured'}), 400
    cv2.imwrite(INPUT_IMG_PATH, frame)
    score = verify(INPUT_IMG_PATH)
    threshold = 0.5
    result = 'Verified ✅' if score > threshold else 'Unverified ❌'
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)
