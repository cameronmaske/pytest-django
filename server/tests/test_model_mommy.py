from django.test import TestCase
from base.models import Person, Dog, Tag
from model_mommy import mommy

from model_mommy.recipe import Recipe, foreign_key


class ModelTestCase(TestCase):
    def test_person(self):
        person = mommy.prepare(Person)
        print "Mommy - test_person:Person Count", Person.objects.all()

    def test_dog(self):
        dog = mommy.prepare(Dog)
        print "Mommy - test_dog: Person Count", Person.objects.all()

    def test_tag(self):
        # dog = Recipe(Dog)
        # tag_recipe = Recipe(
        #     Tag,
        #     content_object=foreign_key(dog))

        # tag = tag_recipe.prepare()
        dog = mommy.prepare(Dog)
        tag = mommy.prepare(Tag)
        tag.content_object = dog
        self.assertIsNotNone(tag.content_object)
        print "Mommy - test_tag: Dog Count", Dog.objects.all()
        print "Mommy - test_tag: Person Count", Person.objects.all()
