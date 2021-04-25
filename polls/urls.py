from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # /polls/
    path('', views.index, name="index"),
    # /polls/5
    path('polls/<int:question_id>/', views.detail, name="detail"),
    # /polls/5/result
    path('polls/<int:question_id>/result', views.result, name="result"),
    # /polls/5/votes
    path('polls/<int:question_id>/votes', views.votes, name="votes"),
]