from django.db import models
from django.db.models.signals import pre_save
from cmsproject.utils import unique_slug_generator

class Tutorial(models.Model):
    title=models.CharField(max_length=256)
    slug=models.SlugField(max_length=150,unique=True)

    def __str__(self):
        return self.title
def slug_save(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance,instance.title,instance.slug)
pre_save.connect(slug_save,sender=Tutorial)



