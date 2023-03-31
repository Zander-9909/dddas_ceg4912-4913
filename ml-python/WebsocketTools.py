import cv2 #opencv-python (not sure if that's the name on OSX, check opencv website)
import base64
from flask import Flask, request #install pip and use pip install flask

app = Flask(__name__)
cam = cv2.VideoCapture(0)

@app.route('/image', methods=['POST'])
def send_image():
    # Capture image
    succ,img = cam.read()
    if(succ):
        # Encode image
        _, encoded = cv2.imencode('.png', img)
        encoded_string = base64.b64encode(encoded)

        # Send image
        return {'image': encoded_string.decode()}
app.run(host='0.0.0.0')


# import React, { useState, useEffect } from 'react';
# import { View, Image } from 'react-native';
# import io from 'socket.io-client';

# const socket = io('http://localhost:5000');

# export default function App() {
#   const [image, setImage] = useState(null);

#   useEffect(() => {
#     socket.on('connect', () => {
#       console.log('Connected to server');
#     });

#     socket.on('image', (data) => {
#       // Decode image
#       const decoded = atob(data.image);
#       const buffer = new ArrayBuffer(decoded.length);
#       const uint8 = new Uint8Array(buffer);
#       for (let i = 0; i < decoded.length; i++) {
#         uint8[i] = decoded.charCodeAt(i);
#       }

#       // Create image source
#       const type = 'image/png';
#       const blob = new Blob([uint8], { type });
#       const source = { uri: URL.createObjectURL(blob) };
#       setImage(source);
#     });
#   }, []);

#   return (
#     <View>
#       <Image source={image} />
#     </View>
#   );
# }
