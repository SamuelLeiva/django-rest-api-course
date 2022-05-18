from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]
    
    def get_my_discount(self, obj): #se reflejará en el campo de my_discount
        if obj.hasattr(obj, 'id'):
            return None
        if not isinstance(onj, Product):
            return None
        return obj.get_discount() #llama al metodo del model