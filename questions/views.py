from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .serializers import QuestionSerializer

class QuestionView(APIView):
    """
    question
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = QuestionSerializer(data=request.data, context ={"request":request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self,request, ID):
        pass

    def delete(self,request,ID):
        pass
