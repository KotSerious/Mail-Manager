
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from blog.forms import BlogForm
from blog.models import Blog
from django.contrib.auth.mixins import LoginRequiredMixin


class BlogListView(LoginRequiredMixin, ListView):
    """
    Контроллер для отображения всех записей блога
    """
    model = Blog
    login_url = 'users:login'
    extra_context = {
        'title': 'Блог'
    }


class BlogCreateView(LoginRequiredMixin, CreateView):
    """
    Контроллер для создания новой статьи блога
    """
    model = Blog
    form_class = BlogForm
    login_url = 'users:login'
    success_url = reverse_lazy('blog:blogs')
    extra_context = {
        'title': 'Создать блог'
    }


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    """
    Контроллер для обновления данных в статье блога
    """
    model = Blog
    form_class = BlogForm
    login_url = 'users:login'
    success_url = reverse_lazy('blog:blogs')
    extra_context = {
        'title': 'Обновить блог'
    }


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    """
    Контроллер для удаления статьи блога
    """
    model = Blog
    login_url = 'users:login'
    success_url = reverse_lazy('blog:blogs')
    extra_context = {
        'title': 'Удаление блога'
    }


class BlogDetailView(LoginRequiredMixin, DetailView):
    """
    Контроллер для просмотра статьи блога
    """
    model = Blog
    login_url = 'users:login'
    extra_context = {
        'title': 'Просмотр блога'
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object
