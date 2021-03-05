from django.test import TestCase

from .models import  Tutorial

class TutorialTestCase(TestCase):
    def setUp(self):
        Tutorial.objects.create(title='this is a title')
        Tutorial.objects.create(title='this is a title')
    def test_check_slug(self):
        object1=Tutorial.objects.get(pk=1)
        object2=Tutorial.objects.get(pk=2)
        self.assertEqual(object1.slug,'this-is-a-title')
        self.assertEqual(object2.slug,'this-is-a-title-2')


