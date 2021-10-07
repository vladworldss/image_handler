# from logging.config import dictConfig

import falcon


from api.resources import (
    ImageSource
)

import settings as app_settings

# # dictConfig(app_settings.LOGGING)

# # falcon_app = falcon.API(middleware=[ContentEncodingMiddleware(), FakeLoginMiddleware()])


app = falcon.API()
test_resource = ImageSource()
app.add_route(app_settings.IMAGE_SOURCE_ROUTE, test_resource)


# # falcon_app.set_error_serializer(error_serializer)



