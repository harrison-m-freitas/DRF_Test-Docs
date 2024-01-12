from django.test import TestCase

from aluraflix.serializers import ProgramSerializer
from aluraflix.models import Program


class ProgramSerializerTestCase(TestCase):
    
    def setUp(self) -> None:
        self.program = Program(
            title="Fast and Furious",
            realese_date="2002-02-02",
            type="F",
            likes=35206,
            dislikes=1021
        )
        self.serializer = ProgramSerializer(instance=self.program)
    
    
    def test_serializer_fields(self):
        "Test the serializers fields"
        data = self.serializer.data
        
        self.assertEqual(set(data.keys()), set(["title", "type", "realese_date", "likes"]))
        
        
    def test_serializer_data(self):
        "Test the serializers data"
        data = self.serializer.data
        
        self.assertEqual(data['title'], self.program.title)
        self.assertEqual(data["type"], self.program.type)
        self.assertEqual(data["realese_date"], self.program.realese_date)
        self.assertEqual(data["likes"], self.program.likes)
