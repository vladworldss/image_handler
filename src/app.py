# from logging.config import dictConfig

import falcon


from api.resources import (
    ImageSource,
    ResizeImageSource,
    TestRes
)

import settings as app_settings


app = falcon.API()
app.add_route(app_settings.IMAGE_SOURCE_ROUTE, ImageSource())
app.add_route(app_settings.IMAGE_RESIZE_ROUTE, ResizeImageSource())
app.add_route('/test', TestRes())
