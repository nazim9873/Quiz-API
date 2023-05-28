from django.urls import path
from base import views


urlpatterns = [
    path('quizzes/', views.quiz_list),
    path('quizzes/active/', views.quiz_active),
    path('quizzes/<int:pk>/result/', views.quiz_result),
    path('quizzes/all/', views.quiz_list),
]
