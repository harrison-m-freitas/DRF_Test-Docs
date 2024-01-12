from django.test import TestCase

from aluraflix.models import Program


class FixtureDataTestCase(TestCase):
    fixtures = ["initial_programs"]
    
    def test_load_fixtures(self):
        program_bizzaro = Program.objects.get(pk=1)
        all_programs = Program.objects.all()
        self.assertEqual(program_bizzaro.title, "Coisas Bizarras")
        self.assertEqual(len(all_programs), 9)