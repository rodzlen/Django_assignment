from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.db.models import Q

from todo_list.form import TodoUpdateForm
from todo_list.models import Todo


class TodoListView(ListView):
    queryset = Todo.objects.all().order_by('-created_at')
    template_name = 'todo_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset= queryset.filter(
                Q(title__icontains=q) |
                Q(content__icontains=q)
            )
        return queryset

class TodoDetailView(DetailView):
    model=Todo
    template_name = 'todo_detail.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        print(pk)
        return queryset.filter(pk=pk)

class TodoCreateView(LoginRequiredMixin,CreateView):
    model=Todo
    template_name = 'todo_create.html'
    form_class = TodoUpdateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        from django.http import HttpResponseRedirect
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('todo:detail', kwargs={'pk':self.object.pk})
class TodoUpdateView(LoginRequiredMixin,UpdateView):
    model= Todo
    template_name = 'todo_update.html'
    fields= ('title','description','start_date','end_date','is_complete')

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.user.is_superuser:
            pk = self.kwargs.get('pk')
            return queryset.filter(pk=pk)
        return queryset.filter(user=self.request.user)
    def get_success_url(self):
        return reverse_lazy('todo:detail',kwargs={'pk':self.object.pk})
class TodoDeleteView(LoginRequiredMixin,DeleteView):
    model= Todo

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser:
            pk = self.kwargs.get('pk')
            return queryset.filter(pk=pk)
        return queryset.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('todo:list')
