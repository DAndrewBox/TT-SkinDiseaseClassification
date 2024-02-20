MODELS_PATH = './models'
ACCEPTED_IMAGE_FORMATS = ['jpg', 'jpeg', 'png']
IMAGE_FORMAT_NOT_ALLOWED_MESSAGE = 'File extension not allowed! Only .jpg, .jpeg and .png are allowed.'

SKIN_MODEL_NAME = f'{MODELS_PATH}/SkinCheck_ResNetv4.h5'
SKIN_MODEL_INPUT_SHAPE = (256, 256)

DISEASES_MODEL_NAME = f'{MODELS_PATH}/HAM10000_VGG16_nadam.h5'
DISEASES_MODEL_INPUT_SHAPE = (128, 128)

DISEASES_CLASSES_FULLNAME = [
    "Bowen's Disease",
    "Basal Cell Carcinoma",
    "Benign Keratosis-like Lesions",
    "Dermatofibroma",
    "Melanoma",
    "Melanocytic Nevi",
    "Vascular Lesions",
]

DISEASES_CLASSES_INFO = {
    "Bowen's Disease": {
        "name": {
            "en": "Bowen's Disease",
            "es": "Enfermedad de Bowen",
        },
        "description": {
            "en":	"Bowen's disease is a type of skin cancer that is caused by chronic sun exposure. " +
            "It is a type of squamous cell carcinoma. It is a slow-growing cancer that can be cured if caught early. " +
            "It is also known as Bowenoid papulosis.",
            "es":	"La enfermedad de Bowen es un tipo de cáncer de piel causado por la exposición solar crónica. " +
            "Es un tipo de carcinoma escamoso. Es un cáncer de crecimiento lento que se puede curar si se detecta a tiempo. " +
            "También se conoce como papulosis de Bowenoid.",
        },
        "image": "https://i0.wp.com/post.healthline.com/wp-content/uploads/2022/05/Bowens-disease-body1.jpg",
        "link": "https://www.healthline.com/health/bowens-disease"
    },
    "Basal Cell Carcinoma": {
        "name": {
            "en": "Basal Cell Carcinoma",
            "es": "Carcinoma Basocelular",
        },
        "description": {
            "en":	"Basal cell carcinoma is the most common type of skin cancer. " +
            "It is a slow-growing cancer that rarely spreads to other parts of the body. " +
            "It usually appears as a new growth with a pearly or waxy appearance. " +
            "It can also appear as a sore that doesn't heal.",
            "es":	"El carcinoma basocelular es el tipo de cáncer de piel más común. " +
            "Es un cáncer de crecimiento lento que rara vez se propaga a otras partes del cuerpo. " +
            "Generalmente aparece como un nuevo crecimiento con un aspecto perla o cera. " +
            "También puede aparecer como una herida que no se cura.",
        },
        "image": "https://i0.wp.com/images-prod.healthline.com/hlcmsresource/images/topic_centers/SkinCancer/642x361_Basal_Cell_Carcinoma_SLIDE_1.jpg",
        "link": "https://www.healthline.com/health/basal-cell-carcinoma"
    },
    "Benign Keratosis-like Lesions": {
        "name": {
            "en": "Benign Keratosis-like Lesions",
            "es": "Lesiones benignas como queratosis",
        },
        "description": {
            "en":	"Benign keratosis-like lesions are a group of skin conditions that are caused by sun exposure. " +
            "They are not cancerous, but they can be precancerous. " +
            "They are usually harmless, but they can be removed if they are bothersome.",
            "es":	"Las lesiones benignas como queratosis son un grupo de condiciones de la piel causadas por la exposición solar. " +
            "No son cancerosos, pero pueden ser precancerosos. " +
            "Generalmente son inofensivos, pero se pueden eliminar si son molestos.",
        },
        "image": "https://post.healthline.com/wp-content/uploads/2020/08/648x364_Seborrheic-Keratosis.jpg",
        "link": "https://www.healthline.com/health/seborrheic-keratosis"
    },
    "Dermatofibroma": {
        "name": {
            "en": "Dermatofibroma",
            "es": "Dermatofibroma",
        },
        "description": {
            "en":	"Dermatofibroma is a skin condition that is caused by sun exposure. " +
            "It is a slow-growing, noncancerous tumor that usually appears on the legs. " +
            "It is also known as a dermal fibroma.",
            "es":	"El dermatofibroma es una condición de la piel causada por la exposición solar. " +
            "Es un tumor no canceroso de crecimiento lento que generalmente aparece en las piernas. " +
            "También se conoce como fibroma dermal.",
        },
        "image": "https://post.healthline.com/wp-content/uploads/2020/09/hemangioma-of-skin_thumb-1-732x549.jpg",
        "link": "https://www.healthline.com/health/dermatofibromas"
    },
    "Melanoma": {
        "name": {
            "en": "Melanoma",
            "es": "Melanoma",
        },
        "description": {
            "en":	"Melanoma is a type of skin cancer that is caused by sun exposure. " +
            "It is a slow-growing cancer that can spread to other parts of the body. " +
            "It is also known as malignant melanoma.",
            "es":	"El melanoma es un tipo de cáncer de piel causado por la exposición solar. " +
            "Es un cáncer de crecimiento lento que puede propagarse a otras partes del cuerpo. " +
            "También se conoce como melanoma maligno.",
        },
        "image": "https://i0.wp.com/post.healthline.com/wp-content/uploads/2019/06/Superficial-spreading-melanoma-1296x728-gallery_slide2.jpg",
        "link": "https://www.healthline.com/health/melanoma"
    },
    "Melanocytic Nevi": {
        "name": {
            "en": "Melanocytic Nevi",
            "es": "Melanocitos Nevi",
        },
        "description": {
            "en":	"Melanocytic nevi are a group of skin conditions that are caused by sun exposure. " +
            "They are not cancerous, but they can be precancerous. " +
            "They are usually harmless, but they can be removed if they are bothersome.",
            "es":	"Los melanocitos nevi son un grupo de condiciones de la piel causadas por la exposición solar. " +
            "No son cancerosos, pero pueden ser precancerosos. " +
            "Generalmente son inofensivos, pero se pueden eliminar si son molestos.",
        },
        "image": "https://i0.wp.com/images-prod.healthline.com/hlcmsresource/images/galleries/nevus/common_nevus-648x364-slide2.jpg?w=1575 750w",
        "link": "https://www.healthline.com/health/nevus"
    },
    "Vascular Lesions": {
        "name": {
            "en": "Vascular Lesions",
            "es": "Lesiones vasculares",
        },
        "description": {
            "en":	"Vascular lesions are a group of skin conditions that are caused by sun exposure. " +
            "They are not cancerous, but they can be precancerous. " +
            "They are usually harmless, but they can be removed if they are bothersome.",
            "es":	"Las lesiones vasculares son un grupo de condiciones de la piel causadas por la exposición solar. " +
            "No son cancerosos, pero pueden ser precancerosos. " +
            "Generalmente son inofensivos, pero se pueden eliminar si son molestos.",
        },
        "image": "https://www.researchgate.net/publication/338390221/figure/fig2/AS:865952929431552@1583470675408/Dermoscopy-homogeneous-pink-vascular-lesion-with-small-scales-on-the-surface.jpg",
        "link": "https://www.healthline.com/health/peripheral-vascular-disease"
    },
}

REPORTS_PATH = "./reports"