import falcon


class ImageSource(object):

    def on_get(self, req, res):
        res.status = falcon.HTTP_200  # This is the default status
        res.body = ('This is me, ImageSource, serving a resource!')
