from a2wsgi import ASGIMiddleware
from app import appFastAPI

application = ASGIMiddleware(appFastAPI)