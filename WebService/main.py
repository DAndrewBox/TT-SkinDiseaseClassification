import uvicorn
import os
from dotenv import load_dotenv
load_dotenv()

UVICORN_HOST = os.getenv("UVICORN_HOST")

if __name__ == '__main__':
    uvicorn.run("app:appFastAPI", port=8111, host=UVICORN_HOST, workers=4, reload=True)