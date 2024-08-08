import socketio
import eventlet
import numpy as np
from flask import Flask
from keras.models import load_model
import base64
from io import BytesIO
from PIL import Image
import cv2

sio = socketio.Server()

app = Flask(__name__) #'__main__'
speed_limit = 27
def img_preprocess(img):
    img = img[60:135,:,:]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img,  (3, 3), 0)
    img = cv2.resize(img, (200, 66))
    img = img/255
    return img


@sio.on('telemetry')
def telemetry(sid, data):
    speed = float(data['speed'])
    image = Image.open(BytesIO(base64.b64decode(data['image'])))
    image = np.asarray(image)
    image = img_preprocess(image)
    image = np.array([image])
    steering_angle = float(model.predict(image))

    # Determining direction based on ther sign of steering angle
    direction = "right" if steering_angle >= 0 else "left"

    # Converting steering angle to a decimal rounded of to 4 decimals
    steering_angle_rounded = round(abs(steering_angle), 4)

    # Converting steering angle to absolute value for rounding
    steering_angle_abs = abs(steering_angle)

    throttle = 1.0 - speed / speed_limit
    print('{} {} {}'.format(direction, throttle, speed))
    send_control(steering_angle, throttle)

    # Print direction and rounded angle
    print('Direction: {}, Angle: {:.4f}'.format(direction, steering_angle_rounded))



@sio.on('connect')
def connect(sid, environ):
    print('Connected')
    send_control(0, 0)

def send_control(steering_angle, throttle):
    sio.emit('steer', data = {
        'steering_angle': str(steering_angle),
        'throttle': str(throttle)
    })


if __name__ == '__main__':
    model = load_model('xxxx_model.h5')
    app = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)
