from django.db import models
from django.contrib.auth.models import User
from main.models import Subject as sj
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.SlugField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Course(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    title = models.CharField(max_length = 200)
    slug = models.SlugField()
    overview = models.TextField()
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
    created = models.DateField(auto_now_add = True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class content(models.Model):
    module = models.ForeignKey(Module, on_delete = models.CASCADE)
    content_type = models.ForeignKey(ContentType,
                                     related_name = 'content',
                                      on_delete = models.CASCADE,
                                       limit_choices_to = {
                                           'model__in':(
                                               'text',
                                               'video',
                                               'image',
                                               'file'
                                           )
                                       })
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')

class ItemBase(models.Model):
    user = models.ForeignKey(User,
                             related_name = '%(class)s_related',
                             on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    created = models.DateField(auto_now_add = True)

    class Meta:
        abstract =True
    
    def __str__(self):
        return self.title

class Text(ItemBase):
    content = models.TextField()

class File(ItemBase):
    file = models.FileField(upload_to='files')

class Image(ItemBase):
    file = models.FileField(upload_to='images')

class Video(ItemBase):
    url = models.URLField()







