from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["POST"]) #allowed Methods
def api_home(request, *args, **kwargs):
    """ 
    DRF API View 
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True): # muestra mensaje si el serializer no es valido
        instance = serializer.save()
        print(instance)
        # instance = form.save() // otra forma usando forms
        return Response(serializer.data)
    return Response({"invalid": "No good data"}, status=400)