import json
from flask_restplus import Namespace, Resource, fields
from flask import request
# import numpy as np
import base64
from io import BytesIO
from .leafclassification import predict
from PIL import Image

api = Namespace('api', description='api')

@api.route('/predict')
class Predict(Resource):
    # POST Method
    def post(self):
        # get the image in base64 form and decode it
        data = request.form['base']
        byte_data = base64.b64decode(data)
        image_data = BytesIO(byte_data)
        img = Image.open(image_data)
        plant_name = predict(img)
        # nparr = np.fromstring(base64.b64decode(data), np.uint8)

        return {'status': True, 'plant_name': plant_name}
