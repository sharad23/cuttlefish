from django.test import TestCase
from experiment.models import TestModel



class ModelTest(TestCase):

    def test_add(self):
        self.assertEqual(len(TestModel.get_all()), 0)
        self.assertEqual(1, 1)