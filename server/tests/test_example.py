from django.test import TestCase
from example.models import Dog


class ExampleTestCase(TestCase):
    def test_example(self):
        dog = Dog(name="Fido", breed="lab", pk=1)
        dog.save()

        db_dog = Dog.objects.get(pk=1)
        self.assertEqual(db_dog, dog)
