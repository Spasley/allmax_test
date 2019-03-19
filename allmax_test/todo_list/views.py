from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Record, choices


class TodoListView(LoginRequiredMixin, CreateView):

    model = Record
    fields = ['text', 'priority']
    success_url = '/todo_list/app'

    def form_valid(self, form):
        form.instance.user_id_id = self.request.user.id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        user = self.request.user
        if user.is_staff:
            records = Record.objects.all().order_by('priority')
        else:
            records = Record.objects.filter(user_id_id=user.id).order_by('priority')
        for record in records:
            record.priority = dict(choices).get(record.priority, '???')
        kwargs['todos'] = records
        kwargs['choices'] = choices
        return super().get_context_data(**kwargs)


class DeleteRecordView(LoginRequiredMixin, DeleteView):

    model = Record
    success_url = reverse_lazy('todo_list')


class UpdateRecordView(LoginRequiredMixin, UpdateView):

    model = Record
    fields = ['priority', 'text']
    success_url = reverse_lazy('todo_list')

    def form_valid(self, form):
        form.instance.user_id_id = self.request.user.id
        return super().form_valid(form)
