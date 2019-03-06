from rest_framework import serializers
from .models import Nodes,Data

class NodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nodes
        # all values
        fields = '__all__'

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        # all values
        fields = '__all__'
