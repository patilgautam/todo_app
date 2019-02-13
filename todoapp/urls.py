
from django.urls import path

from todoapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecompleted', views.deleteCompletedTodo, name='deletecompleted'),
    path('deleteall', views.deleteAllTodo, name='deleteall')
]

