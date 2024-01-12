from rest_framework import serializers

from aluraflix.models import Program


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ["title", "type", "realese_date", "likes"]