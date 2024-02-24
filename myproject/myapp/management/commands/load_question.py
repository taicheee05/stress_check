import pandas as pd
from django.core.management.base import BaseCommand
from myapp.models import Question

class Command(BaseCommand):
    help = 'survey_questions.csvからデータベースへ質問をロードする'

    def handle(self, *args, **kwargs):
        # df_questionがここでロードされると仮定します。question.pyからインポートするか、直接CSVファイルを読み込むかです
        # 例: df_question = pd.read_csv('path/to/survey_questions.csv')
        
        # question.pyからdf_questionをインポートする場合
        from question import df_question

        for _, row in df_question.iterrows():
            question = Question(
                text=row['D'],  # D列に具体的な質問内容
                category=row['B'],  # B列の大問IDをカテゴリとして使用
                choice_1=row['E'], score_1=row['F'],
                choice_2=row['G'], score_2=row['H'],
                choice_3=row['I'], score_3=row['J'],
                choice_4=row['K'], score_4=row['L'],
            )
            question.save()

        self.stdout.write(self.style.SUCCESS('データベースにアンケート質問を正常にロードしました'))
