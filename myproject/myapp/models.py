from django.db import models

class User(models.Model):
    email = models.EmailField()
    workplace_code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    furigana = models.CharField(max_length=100)
    employee_number = models.CharField(max_length=100)
    birthdate = models.DateField()
    gender = models.CharField(max_length=10)

class Question(models.Model):
    text = models.TextField()
    category = models.CharField(max_length=100)

class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.CharField(max_length=100)

class Calculation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stress_quality_scale = models.CharField(max_length=100)
    stress_reaction_scale = models.CharField(max_length=100)
    # Add other fields as needed based on calculation outcomes
