from django.db import models
from tinymce.models import HTMLField

class Question(models.Model):
    title = models.CharField(max_length=50)
    content = HTMLField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name = "user_questions")
    tags = models.ManyToManyField("tags.Tag")
    
    def __str__(self):
        return self.title
