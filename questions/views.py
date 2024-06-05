from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from .serializers import QuestionSerializer
from .models import Question
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
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        print(serializer.error_messages)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request, ID):
        try:
            question = Question.objects.get(id = ID)
        except Question.DoesNotExist:
            return Response({"error":"Question doesn't exist."}, status=status.HTTP_404_NOT_FOUND)

        serializer = QuestionSerializer(question,data=request.data, context={"request":request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'error':f'Error.'}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,ID):
        pass
