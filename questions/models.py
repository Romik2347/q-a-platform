from django.db import models
from tinymce.models import HTMLField

class Question(models.Model):
    title = models.CharField(max_length=50)
    content = HTMLField()
    timestamp = models.DateField(auto_now_add=True)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name = "user_questions")
    tags = models.ManyToManyField("tags.Tag")
    answered = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class Answer(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name = "answers")
    content = HTMLField()
    timestamp = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default = False)

    def __str__(self):
        return f"Answer from {self.user}"
