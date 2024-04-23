from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST', 'PUT'])
def Home_page(request, *args, **kwargs):
    return Response(data={'msg':'welcome to first api'})