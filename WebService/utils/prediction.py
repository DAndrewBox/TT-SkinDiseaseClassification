import tensorflow as tf
import numpy as np
from PIL import Image
from utils.constants import SKIN_MODEL_NAME, DISEASES_MODEL_NAME, DISEASES_CLASSES_FULLNAME, DISEASES_CLASSES_INFO

def preProcessImage(image: Image.Image, inputShape: tuple, normalize: bool = False):
    # Preprocess Image
    image = image.resize(inputShape)
    image = np.asfarray(image)
    image = np.expand_dims(image, axis=0)

    # Normalize Image
    if normalize:
        image = image / 255.

    return image

def loadSkinCheckModel():
    # Load Model
    model = tf.keras.models.load_model(SKIN_MODEL_NAME)
    return model

def predictSkinCheck(image: np.ndarray):
    # Predict Image
    model = loadSkinCheckModel()
    prediction = model.predict(image)
    predictionValue = round(prediction.tolist()[0][0] * 10000) / 100
    return {
        "skinHasDiseasesPrediction": float(f'{(100. - predictionValue):.8f}'),
        "skinHasDiseases": predictionValue < 50,
    }

def loadDiseasesModel():
    # Load Model
    model = tf.keras.models.load_model(DISEASES_MODEL_NAME)
    return model

def predictDiseases(image: np.ndarray):
    # Predict Image
    model = loadDiseasesModel()
    prediction = model.predict(image)
    return prediction2Dict(prediction)

def prediction2Dict(prediction: np.ndarray):
    # Convert Prediction to Dictionary
    prediction = prediction.tolist()
    prediction = prediction[0]

    # Get Prediction Rates for each Disease rounded at 4 decimals
    predictionRates = {
        DISEASES_CLASSES_FULLNAME[i]: float(f'{(prediction[i] * 100):.4f}') for i in range(len(prediction))
    }

    # Get sorted prediction rates with all information
    sortedPredictions = sorted(predictionRates.items(), key=lambda x: x[1], reverse=True)
    sortedPredictionsWithInfo = []
    for i in range(len(sortedPredictions)):
        sortedPredictionsWithInfo.append([
            DISEASES_CLASSES_INFO[sortedPredictions[i][0]]["name"],
            sortedPredictions[i][1],
            DISEASES_CLASSES_INFO[sortedPredictions[i][0]]["image"]
        ])

    prediction = predictionRates

    predictions_dict = {
      "prediction": prediction,
      "topPrediction": max(prediction, key=prediction.get),
      "topPredictionInformation": DISEASES_CLASSES_INFO[max(prediction, key=prediction.get)],
      "sortedPredictions": sortedPredictionsWithInfo
    }

    return predictions_dict