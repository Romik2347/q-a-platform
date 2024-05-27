from rest_framework import serializers
from tags.serializers import TagSerializer
from .models import Question
from tags.models import Tag

class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Question
        fields = ['title', 'content', 'tags','user', 'id']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        question = Question.objects.create(**validated_data)
        question.tags.set(tags_data)
        return question