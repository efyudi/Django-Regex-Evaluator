from django.urls import path
from regex.views import RegexView, evaluate_regex

urlpatterns = [
    path('regex/', RegexView.as_view(), name='regex_home'),
    path('evaluate_regex/', evaluate_regex, name='evaluate_regex'),
]