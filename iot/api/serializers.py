from rest_framework import serializers
from .models import Nodes

class NodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nodes
        # all values
        fields = '__all__'
