import json

from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse

from products.models import Product



def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
        return JsonResponse(data)
        #print(data)
        #json_data_str = json.dumps(data)
        # model instance (model_data)
        # turn a Pythom dict
        #return Json to my client
    # return HttpResponse(data, headers={"content-type": "application/json"})