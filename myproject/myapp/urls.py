from django.urls import path
from . import views  # viewsをインポート

urlpatterns = [
    path('', views.index, name='index'),  # ホームページ
    path('survey/', views.survey, name='survey'),  # ストレスチェックの調査ページ
    path('results/', views.results, name='results'),  # 結果表示ページ
    path('myapp/', views.ProductListView.as_view(), name="list"),

]
