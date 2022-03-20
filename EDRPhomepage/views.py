from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student, Subject
from .serializers import ItemSerializer
# Create your views here.

#playing with dummy data first
@api_view(['GET'])
def getdata(request):
    item = Student.objects.all()
    serializer=ItemSerializer(item, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def updatedata(request, pk):
    item=Subject.objects.get(id=pk)
    serializer=ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.update()
    return Response(serializer.data)