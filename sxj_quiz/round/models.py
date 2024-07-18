from django.db import models
import time

def file_path(instance, name):
    return str(int(time.time())) + f"/{name}"
    

class Round(models.Model):
    name = models.CharField(max_length=40, blank=True)
    def __str__(self):
        return self.name
    
class Que_ans(models.Model):
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    def __str__(self):
        return self.question
    
class MixedBag(models.Model):
    subject = models.CharField(max_length=30)
    q_ans = models.JSONField(default=dict)
            
    def __str__(self):
        return self.subject
    
class Au_Vis(models.Model):
    ques = models.CharField(max_length=400)
    image = models.FileField(upload_to=file_path)
    answr = models.CharField(max_length=50)
    def __str__(self):
        return self.ques
    
class Multiple(models.Model):
    ques = models.CharField(max_length=300)
    answer = models.CharField(max_length=50)
    choi = models.JSONField(default=list)
    
    def save(self, *args, **kwargs):
        if self.answer not in self.choi and len(self.choi) != 4:
            raise ValueError
        else:
            super().save()
            
    def __str__(self):
        return self.ques
