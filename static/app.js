function startCamera() {
    fetch('/start_camera', { method: 'POST' })
        .then(() => {
            document.getElementById('video-box').style.display = 'block';
            document.getElementById('start-btn').style.display = 'none';
            document.querySelector('#webcam-stream').src = "/video_feed";
        });
}

function stopCamera() {
    fetch('/stop_camera', { method: 'POST' })
        .then(() => {
            document.getElementById('video-box').style.display = 'none';
            document.getElementById('start-btn').style.display = 'inline-block';
            document.querySelector('#webcam-stream').src = "";
            document.getElementById('result-text').innerText = '';
        });
}

function verifyFace() {
    fetch('/verify', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result-text').innerText = data.result;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result-text').innerText = 'Error verifying face.';
    });
}
