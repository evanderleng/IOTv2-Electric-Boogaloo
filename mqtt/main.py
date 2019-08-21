import base64
import json
import os
from google.cloud import pubsub_v1
from google.cloud import storage
from google.cloud import vision
from time import sleep
from datetime import datetime
from picamera import PiCamera
from google.cloud.vision import types
from face_detection import highlight_faces
from PIL import Image, ImageDraw


delay=2
client = vision.ImageAnnotatorClient()

def detect_face(face_file, max_results=4):
    """Uses the Vision API to detect faces in the given file.

    Args:
        face_file: A file-like object containing an image with faces.

    Returns:
        An array of Face objects with information about the picture.
    """
    client = vision.ImageAnnotatorClient()

    content = face_file.read()
    image = types.Image(content=content)

    return client.face_detection(image=image, max_results=max_results).face_annotations
	
def takePhotoWithPiCam():
	sleep(delay)
	camera.capture(full_path)

def faces(input_filename, output_filename, max_results):
    with open(input_filename, 'rb') as image:
        faces = detect_face(image, max_results)
        print('Found {} face{}'.format(
            len(faces), '' if len(faces) == 1 else 's'))

        print('Writing to file {}'.format(output_filename))
        # Reset the file pointer, so we can read the file again
        image.seek(0)
        highlight_faces(image, faces, output_filename)

# Set the filename and bucket name
bucket = 'images1703221' # replace with your own unique bucket name
with PiCamera() as camera:
	while True:
		full_path = ('/home/pi/Desktop/pre/' + str(datetime.now()) + ' pre.jpg')
		full_path_post = ('home/pi/Desktop/' + str(datetime.now()) +' post.jpg')
		file_name = (str(datetime.now()) + ' pre.jpg')
		takePhotoWithPiCam()
		faces(full_path,full_path_post,4)
