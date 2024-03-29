
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from mailing.forms import MessageForm, MailingSettingsForm
from mailing.models import Message, MailingSettings, MailingLogs
from django.contrib.auth.mixins import LoginRequiredMixin


class MessageListView(ListView):
    """
    Контроллер для всех созданных сообщений
    """
    model = Message
    extra_context = {
        'title': 'Сообщения'
    }


class MessageCreateView(LoginRequiredMixin, CreateView):
    """
    Контроллер для создания нового сообщения
    """
    model = Message
    form_class = MessageForm
    login_url = 'users:login'
    success_url = reverse_lazy('client:clients')
    extra_context = {
        'title': 'Создать сообщение'
    }


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    """
    Контроллер для обновления данных в сообщении
    """
    model = Message
    form_class = MessageForm
    login_url = 'users:login'
    success_url = reverse_lazy('client:clients')
    extra_context = {
        'title': 'Обновить сообщение'
    }


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    """
    Контроллер для удаления сообщения
    """
    model = Message
    login_url = 'users:login'
    success_url = reverse_lazy('client:clients')
    extra_context = {
        'title': 'Удалить сообщение'
    }


class MessageDetailView(LoginRequiredMixin, DetailView):
    """
    Контроллер для просмотра данных сообщения
    """
    model = MailingSettings
    login_url = 'users:login'
    extra_context = {
        'title': 'Просмотр сообщения'
    }


class MailingSettingsListView(LoginRequiredMixin, ListView):
    """
    Контроллер для вывода всех вариантов настроек рассылки
    """
    model = MailingSettings
    login_url = 'users:login'
    extra_context = {
        'title': 'Расписание'
    }


class MailingSettingsCreateView(LoginRequiredMixin, CreateView):
    """
    Контроллер для создания новых настроек рассылки
    """
    model = MailingSettings
    form_class = MailingSettingsForm
    login_url = 'users:login'
    success_url = reverse_lazy('client:clients')
    extra_context = {
        'title': 'Создать рассылку'
    }


class MailingSettingsUpdateView(LoginRequiredMixin, UpdateView):
    """
    Контроллер для обновления данных в настройках рассылки
    """
    model = MailingSettings
    form_class = MailingSettingsForm
    login_url = 'users:login'
    success_url = reverse_lazy('client:clients')
    extra_context = {
        'title': 'Обновить рассылку'
    }


class MailingSettingsDeleteView(LoginRequiredMixin, DeleteView):
    """
    Контроллер для удаления настроек рассылки
    """
    model = MailingSettings
    login_url = 'users:login'
    success_url = reverse_lazy('client:clients')
    extra_context = {
        'title': 'Удалить рассылку'
    }


class MailingSettingsDetailView(LoginRequiredMixin, DetailView):
    """
    Контроллер для просмотра данных о настройках рассылки
    """
    model = MailingSettings
    login_url = 'users:login'
    extra_context = {
        'title': 'Просмотр рассылки'
    }


class MailingLogsListView(LoginRequiredMixin, ListView):
    """
    Контроллер для всех созданных сообщений
    """
    model = MailingLogs
    login_url = 'users:login'
    extra_context = {
        'title': 'Логи'
    }
