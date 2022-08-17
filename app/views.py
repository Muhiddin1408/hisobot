from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from app.forms import ContactFrom, Expense_addFrom, AddProjectFrom
from app.models import Project, User


class Add(CreateView):
    def get(self, request, *args, **kwargs):
        form = AddProjectFrom
        content = {'form': form}
        return render(request, 'add.html', content)

    def post(self, request, *args, **kwargs):
        form = AddProjectFrom(request.POST)
        Project.objects.create(name=form.data['name'],
                                         user=request.user)


        return HttpResponseRedirect(reverse_lazy('index'))


class Index(ListView):
    queryset = Project.objects.all()
    model = Project
    template_name = 'index.html'
    context_object_name = 'projects'


class ReportDetail(ListView):
    queryset = Project.objects.all()
    template_name = 'report_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.filter(id=self.kwargs['id'])
        return context

class ReportAdd(CreateView):
    def get(self, request, *args, **kwargs):
        form = ContactFrom
        content = {'form': form}
        return render(request, 'revenue_add.html', content)

    def post(self, request, *args, **kwargs):
        form = ContactFrom(request.POST)
        product = Project.objects.get(id=kwargs['id'])

        product.income = form.data['income']
        product.costum = form.data['costum']
        product.save()

        return HttpResponseRedirect(reverse_lazy('index'))


class Expense_add(CreateView):
    def get(self, request, *args, **kwargs):
        form = Expense_addFrom
        content = {'form': form}
        return render(request, 'expense_add.html', content)

    def post(self, request, *args, **kwargs):
        form = Expense_addFrom(request.POST)
        product = Project.objects.get(id=kwargs['id'])

        product.salary = form.data['salary']
        product.markiting = form.data['markiting']
        product.save()

        return HttpResponseRedirect(reverse_lazy('index'))


class VsIndex(ListView):
    model = Project
    template_name = 'vc_index.html'
    context_object_name = 'projects'