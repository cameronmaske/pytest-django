from django.test import TestCase
from base.models import Person, Dog, Tag, SimpleDog


class ModelTestCase(TestCase):
    def test_person(self):
        person = Person()
        print "Vanilla - test_person. Person Count", Person.objects.all()

    def test_dog(self):
        dog = Dog()
        print "Vanilla - test_dog. Person Count", Person.objects.all()

    def test_tag(self):
        dog = SimpleDog(id=1)
        dog.save()
        tag = Tag(content_object=dog)
        tag.save()
        self.assertIsNotNone(tag.content_object)
        print "Vanilla - test_tag. Dog Count", SimpleDog.objects.all()
        print "Vanilla - test_tag. Person Count", Person.objects.all()
