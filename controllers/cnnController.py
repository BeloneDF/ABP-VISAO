from flask import Flask, render_template, request, jsonify
import pybase64
import tensorflow as tf
from tensorflow.keras.preprocessing import image, image_dataset_from_directory
import numpy as np
import io
from PIL import Image
import os

classes = [
    "Bacterial_spot",
    "Early_blight",
    "Late_blight",
    "Leaf_Mold",
    "Septoria_leaf_spot",
    "Spider_mites Two-spotted_spider_mite",
    "Target_Spot",
    "Yellow_Leaf_Curl_Virus",
    "mosaic_virus",
    "healthy"
]


def cnn():
    if request.method == 'POST':
        try:
            data = request.get_json()
            image_data = pybase64.b64decode(data['foto'])
            image_file = io.BytesIO(image_data)
            img = Image.open(image_file).convert('RGB')
            img = img.resize((128, 128))

            img_array = image.img_to_array(img)
            img_array = img_array / 255.0  # Normalizar a imagem
            img_array = np.expand_dims(img_array, axis=0)

            # Verifique se o caminho do modelo está correto
            model_path = './model/keras_potato_trained_model.h5'
            if not os.path.exists(model_path):
                raise FileNotFoundError(
                    f"Modelo não encontrado no caminho: {model_path}")

            # Carregar o modelo salvo no formato Keras
            saved_model = tf.keras.models.load_model(model_path)
            prediction = saved_model.predict(img_array)
            pred_index = np.argmax(prediction)
            disease_name = classes[pred_index]

            return {
                'status': 200,
                'message': "Funcionou",
                'prediction': disease_name
            }
        except Exception as error:
            return {
                'status': 400,
                'message': "Não foi possível enviar a imagem.",
                'error': str(error)
            }, 400

    elif request.method == 'GET':
        return render_template('index.html')
    else:
        return {
            'status': 405,
            'message': "Método não aceito"
        }, 405
