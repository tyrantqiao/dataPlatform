from rest_framework import serializers
from .models import Nodes,Data,SearchData,Order,Commodity

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

class SearchDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchData
        # all values
        fields = '__all__'

class OrderSerializer(serializers.OrderSerializer):
    class Meta:
        model = Order
        # all orders
        fields = '__all__'

class CommoditySerializer(serializers.CommoditySerializer):
    class Meata:
        model = Commodity
        # all commodities
        fields = '__all__'
