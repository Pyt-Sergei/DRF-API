from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile


def get_resize_content(model, width, height):
    im_io = BytesIO()
    im = Image.open(model.image.path)
    im.resize((width, height)).save(im_io, format=im.format)
    return ContentFile(im_io.getvalue())


def get_rotate_content(model, degrees):
    im_io = BytesIO()
    im = Image.open(model.image.path)
    rotated = im.rotate(degrees)
    rotated.save(im_io, format=im.format)
    return ContentFile(im_io.getvalue())
