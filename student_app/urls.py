from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.fetch_student_details_view, name='fetch_student_details'),
]
