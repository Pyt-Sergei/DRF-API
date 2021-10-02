from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ImageSerializer
from .models import ImageModel

from .file import get_resize_content, get_rotate_content


def index(request):
    return HttpResponse("You've gone ...")


@api_view(['GET', 'POST'])
def image_list(request):

    if request.method == 'GET':
        images = ImageModel.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        file = request.data.get('file')
        image = ImageModel.create_from_file(request, file)

        serializer = ImageSerializer(image)
        return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def image_detail(request, pk):
    """
        Retrieve, update or delete a code image.
    """
    try:
        image = ImageModel.objects.get(pk=pk)
    except ImageModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ImageSerializer(image)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def resize_picture(request, pk):
    """
        resize picture size by posted --form width, --from height
    """
    try:
        model = ImageModel.objects.get(pk=pk)
    except ImageModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    width = int(request.data.get('width', 0))
    height = int(request.data.get('height', 0))

    if width == 0:
        width = model.image.width
    if height == 0:
        height = model.image.height

    name = model.image.name.split('/')[-1]
    name = name.split('.')
    name = name[0] + f"_{pk}." + name[-1]

    content = get_resize_content(model, width, height)
    image = ImageModel.create_from_content(request, content, name, pk)
    serializer = ImageSerializer(image)

    return Response(serializer.data)


@api_view(['POST'])
def rotate_picture(request, pk):
    try:
        model = ImageModel.objects.get(pk=pk)
    except ImageModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    degrees = int(request.data.get('degrees'))

    name = model.image.name.split('/')[-1]
    name = name.split('.')
    name = name[0] + f"_{pk}." + name[-1]

    content = get_rotate_content(model, degrees)
    image = ImageModel.create_from_content(request, content, name, pk)
    serializer = ImageSerializer(image)

    return Response(serializer.data)



