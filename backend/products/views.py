from rest_framework import authentication, generics, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from yaml import serialize

from .models import Product
from .serializers import ProductSerializer
from .permissions import IsStaffEditorPermission

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_create(self, serializer): # modificar la creacion
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content = content)
        # send a django signal (revisar curso anterior)

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_filed = 'pk'

product_detail_view = ProductDetailAPIView.as_view()

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_filed = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            ## 

product_update_view = ProductUpdateAPIView.as_view()

class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_filed = 'pk'

    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)

product_delete_view = ProductDeleteAPIView.as_view()

class ProductListAPIView(generics.ListAPIView):
    """ 
    Not gonna use this method
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_list_view = ProductListAPIView.as_view()

# class ProductMixinView(
#     mixins.ListModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.CreateModelMixin,
#     generics.GenericAPIView
#     ):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'pk'

#     def get(self, request, *args, **kwargs): # HTTP GET method
#         print(args, kwargs)
#         pk = kwargs.get('pk') # el lookup_field se encuentra en el kwargs
#         if pk is not None:
#             return self.retrieve(request, *args, **kwargs)
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#     def perform_create(self, serializer): # modificar la creacion
#         # serializer.save(user=self.request.user)
#         print(serializer.validated_data)
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content') or None
#         if content is None:
#             content = "Single view doing cool stuff"
#         serializer.save(content = content)

# product_mixin_view = ProductMixinView.as_view()

# # function based views
# @api_view(['GET', 'POST'])
# def product_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method

#     if method == 'GET':
#         if pk is not None:
#             # detail view
#             obj = get_object_or_404(Product, pk=pk)
#             data = ProductSerializer(obj, many=False).data
#             return Response(data)
#         # list view
#         queryset = Product.objects.all()
#         data = ProductSerializer(queryset, many=True).data
#         return Response(data)

#     if method == 'POST':
#         # create an item
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True): # muestra mensaje si el serializer no es valido
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content') or None
#             if content is None:
#                 content = title
#             serializer.save(content = content)
#             return Response(serializer.data)
#         return Response({"invalid": "No good data"}, status=400)