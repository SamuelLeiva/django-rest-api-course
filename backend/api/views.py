import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    # request -> HttpRequest -> Django
    #request body
    print(request.GET) # url query parameters
    print(request.POST)
    body = request.body
    data = {}
    try:
        data = json.loads(body) #string of JSON -> Python dict
    except:
        pass
    print(data)

    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    print(data)
    return JsonResponse(data)