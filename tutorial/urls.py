from django.urls import path
from . import views

app_name = 'tutorial'

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('index/', views.CBView.as_view()),
    path('schoolList/', views.SchoolListView.as_view(), name = 'list'),
    path('<int:pk>/', views.SchoolDetailView.as_view(), name = 'detail'),
    path('create/', views.SchoolCreateView.as_view(), name = 'create'),    
    path('update/<int:pk>/', views.SchoolUpdateView.as_view(), name = 'update'),
    path('delete/<int:pk>/', views.SchoolDeleteView.as_view(), name = 'delete'),
    path('student_detail/<int:pk>/', views.StudentDetailView.as_view(), name = 'student_detail'),
    path('student_create/', views.StudentCreateView.as_view(), name = 'student_create'),
    path('student_update/<int:pk>/', views.StudentUpdateView.as_view(), name = 'student_update'),
    path('student_delete/<int:pk>/', views.StudentDeleteView.as_view(), name = 'student_delete'),
]
