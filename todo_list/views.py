from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import FormMixin, DeleteView, UpdateView
from .models import List
from .forms import ListForm


# Create your views here.
class Home(FormMixin, ListView):
    model = List
    template_name = 'home.html'
    context_object_name = 'all_items'
    form_class = ListForm

    def post(self, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            messages.success(self.request, 'Item has been added to list!')
            return redirect(self.request.path)
        else:
            messages.warning(self.request, 'Insert item name first to add item!')
            return redirect(self.request.path)


class Delete(DeleteView):
    model = List
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('home')
    success_message = 'Item has been deleted!'

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(Delete, self).delete(request, *args, **kwargs)


class UpdateTaskStatus(View):
    model = List

    def get(self, *args, **kwargs):
        item = get_object_or_404(List, id=kwargs['pk'])
        if item.completed:
            item.completed = False
            messages.warning(self.request, 'Task Uncompleted!')
        else:
            item.completed = True
            messages.success(self.request, 'Task Completed!')
        item.save()

        return HttpResponseRedirect('/')


class EditTask(UpdateView):
    model = List
    template_name = 'edit.html'
    form_class = ListForm
    context_object_name = 'item'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Item has been edited!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Insert item name first to edit item!')
        return redirect(self.request.path)
