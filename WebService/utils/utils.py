from pydantic import BaseModel
from utils.constants import SKIN_MODEL_INPUT_SHAPE, DISEASES_MODEL_INPUT_SHAPE, REPORTS_PATH
from utils.prediction import preProcessImage, predictSkinCheck, predictDiseases
from base64 import b64decode, b64encode
from PIL import Image
from io import BytesIO
from datetime import datetime
from json import loads, dumps

class B64Image(BaseModel):
	imageB64: str

class Report(BaseModel):
	predictedDisease: str
	suggestedDisease: str
	predictedConfidence: float
	imageB64: str
	comment: str

def readImage(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image

def readImageB64(imageB64):
    imageFromB64 = b64decode(imageB64)
    return readImage(imageFromB64)

def predictImage(imageOriginal):
	# Preprocess Image
	image = preProcessImage(imageOriginal, SKIN_MODEL_INPUT_SHAPE)

	# Check if Image is a valid skin with diseases
	skinPredictions = predictSkinCheck(image)
	if not skinPredictions["skinHasDiseases"]:
		return skinPredictions

	# Preprocess Image for skin diseases
	image = preProcessImage(imageOriginal, DISEASES_MODEL_INPUT_SHAPE, True)

	# Predict disease in Image
	diseasePredictions = predictDiseases(image)

	# Return Prediction
	skinPredictions.update(diseasePredictions)

	return skinPredictions

def b64_png2jpg(imageB64):
	# Clear Base64 Header
	imageB64 = imageB64.replace("data:image/png;base64,", "")

	# Convert Base64 PNG to Base64 JPG
	image = Image.open(BytesIO(b64decode(imageB64)))
	buffer = BytesIO()
	image = image.convert("RGB")
	image.save(buffer, format="JPEG")
	imageB64 = b64encode(buffer.getvalue()).decode("utf-8")

	# Add Base64 JPG Header
	imageB64 = "data:image/jpeg;base64," + imageB64
	
	return imageB64

def png2jpg(image):
	# Convert PNG to JPG
	buffer = BytesIO()
	image = image.convert("RGB")
	image.save(buffer, format="JPEG")
	return Image.open(buffer)

def createReport(report: Report):
	# Report to json
	report = loads(report.json())

	# Create report structure
	currentDateTime = datetime.now()
	now = round(datetime.timestamp(currentDateTime) * 1000)

	reportStruct = {
		'id': now,
		'predictedDisease': report['predictedDisease'],
		'suggestedDisease': report['suggestedDisease'],
		'confidence': report['predictedConfidence'],
		'imageB64': report['imageB64'],
		'comment': report['comment'],
		'createdAt': currentDateTime.strftime("%d/%m/%Y %H:%M:%S"),
	}

	# create report file as json from body
	with open(f'{REPORTS_PATH}/report_{reportStruct["id"]}.json', 'w') as reportFile:
		reportFile.write(dumps(reportStruct, indent=2))