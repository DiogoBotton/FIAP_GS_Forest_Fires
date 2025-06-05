import numpy as np
import tensorflow as tf

IMG_SIZE = (299, 299)

def prepare_image_for_predict(image):
    """
    Prepara a imagem para enviar ao modelo
    
    - Redimensiona a imagem para o tamanho especificado (299x299)
    - Normaliza a imagem entre 0 a 1
    - Expande as dimensões para ficar no formato (1, X, Y, Canais)
    """
    image = tf.io.decode_image(image, channels=3)  # decodifica JPEG/PNG/etc.
    image.set_shape([None, None, 3])  # define a forma esperada
    image = tf.image.resize(image, IMG_SIZE)
    image = image / 255.0
    processed_image = np.expand_dims(image, axis=0)
    return processed_image