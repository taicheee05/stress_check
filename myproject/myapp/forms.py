from django import forms
from .models import StresscheckResponse  # Responseモデルをインポート

class StressCheckForm(forms.ModelForm):
    class Meta:
        model = StresscheckResponse  # フォームのモデルとしてResponseを使用
        fields = ['user', 'question', 'response']  # フォームに表示するフィールド
        # 必要に応じてwidgetsやlabelsのカスタマイズを追加
