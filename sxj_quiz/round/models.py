from django.db import models

class Ques(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=50)
    
    def __str__(self):
        return self.question
    
class Mixed_Bag(models.Model):
    subject = models.CharField(max_length=100, primary_key=True)
    ques_ans = models.JSONField(default='dict', blank=True)
    
    def __str__(self) -> str:
        return self.subject
