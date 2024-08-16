from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from todo_app.forms import TodoForm
from todo_app.models import Todo


# Create your views here.
@login_required
def todo_view(request):
    item_list = Todo.objects.filter(user=request.user)
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
        form.save()
        messages.success(request, "Todo item created successfully!")
        return redirect('todo_view')
    form = TodoForm()
    page = {
        "forms": form,
        "item_list": item_list,
        "title": "TODO LIST",
    }
    print("page", page)
    return render(request, 'data.html', context=page)


@login_required
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo_view')


@login_required
def todo_update(request, pk):
    print('pk')
    # todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo = Todo.objects.get(id=pk)
    print(todo.is_completed)
    todo.is_completed = True
    todo.save()
    print(todo.is_completed)
    return redirect('todo_view')


class TodoListView(ListView):
    model = Todo
    template_name = 'data.html'
    context_object_name = 'item_list'


class TodoCreateView(CreateView,ListView):
    model = Todo
    form_class = TodoForm
    template_name = 'data.html'
    success_url = 'todo_view'
    context_object_name = "item_list"

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['is_completed']
    template_name = 'data.html'
    success_url = 'todo_view'

    def form_valid(self, form):
        form.instance.is_completed = True
        messages.success(self.request, "Todo marked as completed!")
        return super().form_valid(form)


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = 'todo_view'

    def delete(self, request, *args, **kwargs):
        messages.info(self.request, "Item removed !!!")
        return super().delete(request, *args, **kwargs)
