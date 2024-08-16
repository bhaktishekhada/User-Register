from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class Todo(models.Model):

    title = models.CharField(max_length=100)
    details = models.TextField()
    due_date = models.DateTimeField(default=timezone.now)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="todo_item",
    )

    class Meta:
        db_table = "todos"
        verbose_name = "todo_item"
        verbose_name_plural = "todo_items"

    def __str__(self):
        return self.title
