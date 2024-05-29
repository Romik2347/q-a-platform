from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .serializers import QuestionSerializer
import time
class QuestionView(APIView):
    """
    question
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        print("POST")
        serializer = QuestionSerializer(data=request.data, context ={"request":request})
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data)
        print(serializer.error_messages)
        return Response(serializer.errors)

    def put(self,request, ID):
        pass

    def delete(self,request,ID):
        pass
