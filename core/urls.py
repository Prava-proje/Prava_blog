from django.urls import path

from core import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('site-purpose/', views.MeqsedlerView.as_view(), name='site-purpose'),
    path('technical-glance/', views.TexnikiView.as_view(), name='technical-glance'),
    path('glass-tinting/', views.SuselerView.as_view(), name='glass-tinting'),
    path('fees-and-taxes/', views.RusumView.as_view(), name='fees-and-taxes'),
    path('fines/', views.CerimeView.as_view(), name='fines'),
    path('contact-us/', views.ElaqeView.as_view(), name='contact-us'),
    path('question-answer/', views.QuestionAnswerView.as_view(), name='question-answer'),
]