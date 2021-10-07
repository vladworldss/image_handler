import falcon


class ImageSource(object):

    def __on_get(self, _, res, image_id):
        res.status = falcon.HTTP_200  # This is the default status
        res.content_type = 'image/png'
        res.set_header('X-Accel-Redirect', '@images/{}'.format(image_id))
        

    def on_get(self, _, res, image_id):
        res.status = falcon.HTTP_200
        res.content_type = 'image/png'
        with open('../static/images/{}'.format(image_id), 'rb') as f:
            res.body = f.read()


class TestRes(object):

    def on_get(self, _, res):
        res.status = falcon.HTTP_200  # This is the default status
        res.body = ('This is me, ImageSource, serving a resource!')

