from .models import Stock
from . forms import StockForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy



class StockListView(ListView):
    model = Stock
    template_name = 'stocks/index.html'
    context_object_name = 'stock_list'
    

class BioView(TemplateView):
    template_name = 'stocks/bio.html'
        
        
class CreateView(CreateView):
    model = Stock
    template_name = 'stocks/create.html'
    form_class = StockForm
    success_url = reverse_lazy('stock-list')


class UpdateView(UpdateView):
    model = Stock
    template_name = 'stocks/update.html'
    form_class = StockForm
    success_url = reverse_lazy('stock-list')
    

class DeleteView(DeleteView):
    model = Stock
    template_name = 'stocks/delete.html'
    context_object_name = 'stock'
    success_url = reverse_lazy('stock-list')


 
        