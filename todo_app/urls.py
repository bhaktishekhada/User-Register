from django.urls import include, path

from todo_app.views import todo_view, remove

urlpatterns = [
    path('todo_view', todo_view, name='todo_view'),
    path('del/<str:item_id>', remove, name="del"),
]
