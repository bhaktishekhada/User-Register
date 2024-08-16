
from django.urls import include, path

from User_app import views
from todo_app.views import todo_view, remove, todo_update, TodoDeleteView, TodoUpdateView, TodoListView, TodoCreateView


urlpatterns = [




    path('fbv/todo-view', todo_view, name='todo_view'),
    path('del/<str:item_id>',remove, name="del"),
    path('todo-update/<int:pk>',todo_update,name='todo_update'),
    path('cbv',TodoListView.as_view(), name='todo_list'),
    path('cbv/create/',TodoCreateView.as_view(), name='todo_create'),
    path('cbv/update/',TodoUpdateView.as_view(), name='todo_update'),
    path('cbv/delete/',TodoDeleteView.as_view(), name='todo_delete'),





]
