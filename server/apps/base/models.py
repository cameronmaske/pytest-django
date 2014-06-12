from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class Person(models.Model):
    happy = models.BooleanField(default=True)
    unhappy = models.BooleanField(default=False)
    name = models.CharField(max_length=30)
    nickname = models.SlugField(max_length=36)
    age = models.IntegerField()
    bio = models.TextField()
    birthday = models.DateField()
    birth_time = models.TimeField()
    appointment = models.DateTimeField()
    blog = models.URLField()


class Dog(models.Model):
    owner = models.ForeignKey('Person')
    breed = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)


class SimpleDog(models.Model):
    breed = models.CharField(max_length=50, default="simple")

class Tag(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
