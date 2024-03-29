from django.db import models



class User(models.Model):
    email = models.EmailField()
    workplace_code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    furigana = models.CharField(max_length=100)
    employee_number = models.CharField(max_length=100)
    birthdate = models.DateField()
    gender = models.CharField(max_length=10)
    class Meta:
        app_label = 'myapp'


class Question(models.Model):
    text = models.TextField(verbose_name="質問文")
    category = models.CharField(max_length=255, verbose_name="カテゴリ")
    def __str__(self):
        return self.text
    class Meta:
        app_label = 'myapp'

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=255, verbose_name="選択肢")
    score = models.IntegerField(verbose_name="スコア")

    def __str__(self):
        return f"{self.text} ({self.score})"
    class Meta:
        app_label = 'myapp'


class StresscheckResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.CharField(max_length=100)
    class Meta:
        app_label = 'myapp'


class Calculation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stress_quality_scale = models.CharField(max_length=100)
    stress_reaction_scale = models.CharField(max_length=100)
    # Add other fields as needed based on calculation outcomes
    class Meta:
        app_label = 'myapp'


