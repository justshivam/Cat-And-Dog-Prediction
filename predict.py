import tensorflow as tf
import logging
import os
import json
import sys

def predict_img(model, img_path):
    image = tf.keras.preprocessing.image.load_img(img_path, target_size=(180, 180))
    image_p = tf.keras.preprocessing.image.img_to_array(image)
    image_p = image_p.reshape((1, image_p.shape[0], image_p.shape[1], image_p.shape[2]))
    image_p = tf.keras.applications.resnet.preprocess_input(image_p)
    pred = model.predict(image_p)
    pred_string = 'Cat' if pred[0][0] > 0.5 else 'Dog'
    print(f'Prediction is: {pred_string}\nConfidence is: {max(pred[0])}')

if __name__ == '__main__':
    paths = sys.argv[1:]
    if len(paths) == 0:
        print('Please pass the paths as program argument.')
        sys.exit()
    logging.getLogger('tensorflow').setLevel(logging.FATAL)
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    json_file = open('resnet50.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model_json = json.loads(loaded_model_json)
    model = tf.keras.models.model_from_config(loaded_model_json, custom_objects=None)
    model.load_weights('resnet50.h5')
    for path in paths:
        print(path)
        predict_img(model, path)