from django.db import models


class ImageModel(models.Model):
    name = models.CharField(max_length=250, default='')
    image = models.ImageField(upload_to='site_media/')
    url = models.URLField(null=True, blank=True)
    path = models.CharField(max_length=200, default='')
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    parent = models.IntegerField(null=True, blank=True)

    @classmethod
    def create_from_file(cls, request, file):
        obj = cls()
        obj.image = file
        obj.width = obj.image.width
        obj.height = obj.image.height
        obj.save()

        obj.path = request.build_absolute_uri(obj.image.url)
        obj.name = obj.image.name.split('/')[-1]
        obj.save(update_fields=['path', 'name'])
        return obj


    @classmethod
    def create_from_content(cls, request, content, name, pk):
        obj = cls()
        obj.image.save(name, content, save=False)

        obj.width = obj.image.width
        obj.height = obj.image.height
        obj.path = request.build_absolute_uri(obj.image.url)
        obj.name = obj.image.name.split('/')[-1]
        obj.parent = pk
        obj.save()
        return obj






