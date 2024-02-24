from django.contrib import admin
from .models import User, Question, Response, Calculation

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'workplace_code', 'name', 'furigana', 'employee_number', 'birthdate', 'gender')
    search_fields = ('name', 'email')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'category')
    search_fields = ('text', 'category')

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'response')
    search_fields = ('user__name', 'question__text')

@admin.register(Calculation)
class CalculationAdmin(admin.ModelAdmin):
    list_display = ('user', 'stress_quality_scale', 'stress_reaction_scale')
    search_fields = ('user__name',)

