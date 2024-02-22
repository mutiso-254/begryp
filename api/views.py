from rest_framework import generics
from rest_framework.response import Response


class TesterAPI(generics.GenericAPIView):
    def post(self, request):
        name = request.data['name']
        return Response(f'Hi {name}, this is a tester')