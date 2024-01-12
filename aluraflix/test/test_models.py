from django.test import TestCase

from aluraflix.models import Program


class ProgramModelTestCase(TestCase):
    def setUp(self):
        self.program = Program(
            title="Fast and Furious",
            realese_date="2002-02-02",
        )
        
    
    def test_default_attributes(self):
        "Test default attributes of the model Program"
        self.assertEqual(self.program.title, "Fast and Furious")
        self.assertEqual(self.program.type, "F")
        self.assertEqual(self.program.realese_date, "2002-02-02")
        self.assertEqual(self.program.likes, 0)
        self.assertEqual(self.program.dislikes, 0)
