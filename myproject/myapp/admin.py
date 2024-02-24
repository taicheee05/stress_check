from django.contrib import admin
from .models import User, Question, StresscheckResponse, Calculation, Choice

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'workplace_code', 'name', 'furigana', 'employee_number', 'birthdate', 'gender')
    search_fields = ('name', 'email')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'category')
    search_fields = ('text', 'category')

@admin.register(StresscheckResponse)
class StresscheckResponseAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'response')
    search_fields = ('user__name', 'question__text')

@admin.register(Calculation)
class CalculationAdmin(admin.ModelAdmin):
    list_display = ('user', 'stress_quality_scale', 'stress_reaction_scale')
    search_fields = ('user__name',)

class ChoiceInline(admin.TabularInline):  # またはadmin.StackedInline
    model = Choice
    extra = 3  # デフォルトで表示する選択肢の数

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['text', 'category']}),
    ]
    inlines = [ChoiceInline]  # Question編集ページにChoiceモデルをインライン表示
    list_display = ('text', 'category')  # 質問リストで表示するフィールド
    search_fields = ['text']  # 質問テキストでの検索を有効化
