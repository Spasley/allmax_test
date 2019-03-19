from django.urls import path
from . import views


urlpatterns = [
    path('app/', views.TodoListView.as_view(), name='todo_list'),
    path('delete/<int:pk>', views.DeleteRecordView.as_view(), name='delete'),
    path('update/<int:pk>', views.UpdateRecordView.as_view(), name='update'),
]
