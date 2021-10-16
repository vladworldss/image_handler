import os
import io

import falcon
import structlog
from PIL import Image

from api import VALIDATION_ERROR, NOT_FOUND_ERROR
import settings as app_settings

logger = structlog.get_logger(__name__)


class BaseImageSource(object):

    def set_content_type(self, res, image_id):
        if image_id.endswith('.png'):
            res.content_type = 'image/png'
        elif image_id.endswith('.jpg'):
            res.content_type = 'image/jpg'
        else:
            raise falcon.HTTPError(
                status=falcon.HTTP_400,
                title=VALIDATION_ERROR,
                description='The "{}" parameter is unsupported.'.format(image_id.split('.')[-1])
            )


class ImageSource(BaseImageSource):

    def __on_get(self, _, res, image_id):
        res.status = falcon.HTTP_200
        res.content_type = 'image/png'
        res.set_header('X-Accel-Redirect', '@images/{}'.format(image_id))

    def on_get(self, _, res, image_id):
        res.status = falcon.HTTP_200
        self.set_content_type(res, image_id)
        image_path = os.path.join(app_settings.IMAGES_DIR, image_id)
        with open(image_path, 'rb') as f:
            res.body = f.read()


class ResizeImageSource(BaseImageSource):

    def on_get(self, _, res, width: str, height: str, image_id: str) -> None:
        img_path = os.path.join(app_settings.IMAGES_DIR, image_id)

        if not os.path.exists(img_path):
            raise falcon.HTTPError(
                status=falcon.HTTP_404,
                title=NOT_FOUND_ERROR,
                description='The file "{}" does was not found'.format(image_id)
            )

        res.status = falcon.HTTP_200
        self.set_content_type(res, image_id)

        resized_img_path = os.path.join(app_settings.IMAGES_DIR, f'{width}x{height}_{image_id}')
        if os.path.exists(resized_img_path):
            with open(resized_img_path, 'rb') as f:
                res.body = f.read()
                return

        with Image.open(img_path) as origin_img:
            resized_img = origin_img.resize((int(width), int(height)))

            img_byte_arr = io.BytesIO()
            resized_img.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()
            res.body = img_byte_arr
            resized_img.save(resized_img_path)
            logger.info(f'{resized_img_path} was saved')


class TestRes(object):

    def on_get(self, _, res):
        res.status = falcon.HTTP_200  # This is the default status
        res.body = ('This is me, ImageSource, serving a resource!')

