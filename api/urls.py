from django.urls import path
from .views import signUp, createTask, deleteTask, updateTask, MyTokenObtainPairView, ApiSearchTaskListView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
  path('sign-up/', signUp),
  path('list-tasks/', ApiSearchTaskListView.as_view()),
  path('create-task/', createTask),
  path('update-task/', updateTask),
  path('delete-task/<str:id>/', deleteTask),
  path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
