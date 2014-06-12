from django.test import TestCase
from base.models import Person, Dog, Tag

from factory import SubFactory, SelfAttribute, LazyAttribute
from factory.django import DjangoModelFactory
from datetime import datetime, time, date
import pytz


class PersonFactory(DjangoModelFactory):
    FACTORY_FOR = 'base.Person'
    age = 21
    bio = "A great guy"
    birthday = date(1989, 1, 1)
    birth_time = time(0, 0)
    appointment = datetime(2014, 1, 1, tzinfo=pytz.UTC)
    blog = "http://www.great-blog.com/"


class DogFactory(DjangoModelFactory):
    FACTORY_FOR = 'base.Dog'
    owner = SubFactory(PersonFactory)
    breed = "pug"
    created = datetime(2014, 1, 1, tzinfo=pytz.UTC)

from django.contrib.contenttypes.models import ContentType


class TagFactory(DjangoModelFactory):
    ABSTRACT_FACTORY = True

    object_id = SelfAttribute('content_object.id')
    content_type = LazyAttribute(
        lambda o: ContentType.objects.get_for_model(o.content_object))


class DogTagFactory(TagFactory):
    FACTORY_FOR = 'base.tag'
    content_object = SubFactory(DogFactory)


class ModelTestCase(TestCase):
    def test_person(self):
        PersonFactory.build()
        print "Factory boy - test_person: Person Count", Person.objects.all()

    def test_dog(self):
        DogFactory.build()
        print "Factory boy - test_dog: Person Count", Person.objects.all()

    def test_tag(self):
        dog = DogFactory.build(id=1)
        tag = DogTagFactory.build(content_object=dog)
        print tag.__dict__

        self.assertIsNotNone(tag.content_object)
        print "Factory boy - test_tag: Dog Count", Dog.objects.all()
        print "Factory boy - test_dog: Person Count", Person.objects.all()
