from django.test import TestCase
from django.urls import reverse, resolve
from stocks import urls
from stocks.views import StockListView, BioView, CreateView, UpdateView, DeleteView


class TestUrls(TestCase):
    
    def test_stock_list_url_is_resolved(self):
        url = reverse('stock-list')
        self.assertEquals(resolve(url).func.view_class, StockListView)

    def test_bio_view_url_is_resolved(self):
        url = reverse('bio-view')
        self.assertEquals(resolve(url).func.view_class, BioView)
        
    def test_stock_create_url_is_resolved(self):
        url = reverse('stock-create')
        self.assertEquals(resolve(url).func.view_class, CreateView)
        
    def test_stock_update_url_is_resolved(self):
        url = reverse('stock-update', args=['1'])
        self.assertEquals(resolve(url).func.view_class, UpdateView)
        
    def test_stock_delete_url_is_resolved(self):
        url = reverse('stock-delete', args=['1'])
        self.assertEquals(resolve(url).func.view_class, DeleteView)
        
    
        
        
        
        
    # path('stock-list/', views.StockListView.as_view(), name='stock_list_view'),
    # path('bio/', views.BioView.as_view(), name='bio_view'),
    # path('create/', views.CreateView.as_view(), name='stock-create'),
    # path('update/<int:pk>/', views.UpdateView.as_view(), name='stock-update'),
    # path('delete/<int:pk>/', views.DeleteView.as_view(), name='stock-delete')