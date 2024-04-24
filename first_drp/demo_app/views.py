from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from demo_app import custom_versions

# Create your views here.
@api_view(['GET', 'POST', 'PUT'])
def Home_page(request, *args, **kwargs):
    return Response(data={'msg':'welcome to first api'})


@api_view(["GET"])
def demo_version(request, *args, **kwargs):
    version = request.version
    return Response(data={'msg':f'You have hit {version} of demo-api'})

class DemoView(APIView):
    versioning_class = custom_versions.DemoViewVersion
    def get(self, request, *args, **kwargs):
        version = request.version
        return Response(data={'msg': f'if you have hit {version}'})

class AnotherView(APIView):
    versioning_class = custom_versions.AnotherViewVersion
    def get(self, request, *args, **kwargs):
        version = request.version
        if version == 'v1':
            # perform v1 related task
            return Response(data={'msg': 'v1 logic'})
        elif version == 'v2':
            # perform v2 related task
            return Response(data={'msg': 'v2 logic'})