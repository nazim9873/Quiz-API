from django.db import models

# Create your models here.
class Quiz(models.Model):
    STATUS = (
    ('inactive', 'inactive'),
    ('active', 'active'),
    ('finished', 'finished'),
    )
    question = models.CharField(max_length=2048)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(default="inactive" , max_length=100 ,choices=STATUS)
    created_date = models.DateTimeField(auto_now_add=True)

class Option(models.Model):
    from_quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE ,null=True,blank=True)
    text = models.CharField(max_length=2048, verbose_name='option text')
    correct = models.BooleanField(default=False)