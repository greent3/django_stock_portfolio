from django.test import TestCase, Client 
from django.urls import reverse 
from stocks.models import Stock
import json



class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        
        self.example_stock = Stock.objects.create(
            ticker= "MTA",
            purchase_date= "2021-11-19",
            purchase_price= "7.95",
            current_price= "5.81",
            exchange= "NYSE"
        )
        
        self.list_url = reverse('stock-list')
        self.create_url = reverse('stock-create')
        self.update_url = reverse('stock-update', args=[self.example_stock.pk])
        self.delete_url = reverse('stock-delete', args=[self.example_stock.pk])
        
        
        
        
        
    
    def test_stock_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'stocks/index.html')
    
    
    
    
    
    
    
    def test_bio_view_GET(self):
        response = self.client.get(reverse('bio-view'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'stocks/bio.html')
    
    
    
    
    
    
    
    def test_stock_create_GET(self):
        response = self.client.get(self.create_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'stocks/create.html')
        
        
        
        
    
    
    
    def test_stock_create_POST(self):
        data = {
            "ticker": "CLLS",
            "purchase_date": "2021-05-03",
            "purchase_price": 18.04,
            "current_price": 2.10,
            "exchange": "NASDAQ",
            "sell_date": "2021-06-28",
            "sell_price": 16.02
        }
        response = self.client.post(self.create_url, data, format='json')
        
        self.assertEquals(Stock.objects.count(), 2)
        self.assertRedirects(response, self.list_url, status_code=302,
                             target_status_code=200, msg_prefix='', fetch_redirect_response=True)
        
                
                
                
                
                
    def test_stock_update_GET(self):
        response = self.client.get(self.update_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'stocks/update.html')
        
    
    
    
    
    
    
    
    def test_stock_update_POST(self):
        data = {
            "ticker": "MTA",
            "purchase_date": "2021-11-19",
            "purchase_price": 18.00,
            "current_price": 2.00,
            "exchange": "NYSE",
            "sell_date": "2022-06-28",
            "sell_price": 16.00
        }
        response = self.client.post(self.update_url, data, format='json')
        
        self.assertEquals(Stock.objects.count(), 1)
        self.assertRedirects(response, self.list_url, status_code=302,
                             target_status_code=200, msg_prefix='', fetch_redirect_response=True)
    
    
    
    
    
    
    
    
    def test_stock_delete_GET(self):
        response = self.client.get(self.delete_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'stocks/delete.html')
    
    
    
    
    
    
    
    
    
    def test_stock_delete_POST(self):
        response = self.client.post(self.delete_url)
        
        self.assertEquals(Stock.objects.count(), 0)
        self.assertRedirects(response, self.list_url, status_code=302,
                             target_status_code=200, msg_prefix='', fetch_redirect_response=True)
    
    
    
    
