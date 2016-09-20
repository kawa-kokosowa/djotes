from rest_framework import serializers
from djotes.rest.models import Note
from django.contrib.auth.models import User


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Note
        fields = ('url', 'contents', 'modified', 'created', 'owner')
