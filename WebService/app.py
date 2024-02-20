from fastapi import FastAPI, File, UploadFile, Body
from utils.constants import ACCEPTED_IMAGE_FORMATS, IMAGE_FORMAT_NOT_ALLOWED_MESSAGE, DISEASES_CLASSES_FULLNAME, DISEASES_CLASSES_INFO
from utils.utils import predictImage, B64Image, b64_png2jpg, png2jpg, readImage, readImageB64, createReport, Report

appFastAPI = FastAPI()

@appFastAPI.post('/api/predictImage')
async def predictImageFromFile(file: UploadFile = File(...)):
	# Verify file extension
	imageExtension = str(file.filename.split('.')[-1]).lower()

	if imageExtension not in ACCEPTED_IMAGE_FORMATS:
		return {'error': IMAGE_FORMAT_NOT_ALLOWED_MESSAGE}
	
	# Verify if its png
	if imageExtension == 'png':
		imageOriginal = png2jpg(readImage(await file.read()))
		return predictImage(imageOriginal)
	
	# Get Image from file (if it's not png)
	imageOriginal = readImage(await file.read())

	return predictImage(imageOriginal)

@appFastAPI.post('/api/predictImageB64')
def predictImageFromB64(imageB64: B64Image = Body(...)):
	# Verify file extension (if b64 string contains file extension)
	imageB64 = imageB64.imageB64
	imageExtension = str(imageB64.split(',')[0].split(';')[0].split('/')[-1]).lower()
	if imageExtension not in ACCEPTED_IMAGE_FORMATS:
		return {'error': IMAGE_FORMAT_NOT_ALLOWED_MESSAGE}
	
	# Verify if its png
	if imageExtension == 'png':
		imageB64 = b64_png2jpg(imageB64)
		
	# Get Image from file
	imageB64 = imageB64.split(',')[1]
	imageOriginal = readImageB64(imageB64)
		
	return predictImage(imageOriginal)

@appFastAPI.get('/api/getSkinDiseaseById/{diseaseId}')
async def getSkinDiseaseById(diseaseId: int):
	skinDiseaseName = DISEASES_CLASSES_FULLNAME[diseaseId] if diseaseId < len(DISEASES_CLASSES_FULLNAME) else None

	if skinDiseaseName is None:
		return {'error': 'Skin disease not found'}
	
	skinDisease = DISEASES_CLASSES_INFO[DISEASES_CLASSES_FULLNAME[diseaseId]]
	return skinDisease

@appFastAPI.get('/api/getSkinDiseaseAll')
async def getSkinDiseaseAll():
	listOfSkinDiseases = []
	for skinDiseaseName in DISEASES_CLASSES_FULLNAME:
		skinDisease = DISEASES_CLASSES_INFO[skinDiseaseName]
		listOfSkinDiseases.append(skinDisease)

	return listOfSkinDiseases

@appFastAPI.post('/api/sendReport')
async def sendReport(report: Report = Body(...)):
	createReport(report)

	return {'message': '¡El reporte ha sido enviado con éxito!'}