from django.test import TestCase
from stocks.models import Stock

class TestModels(TestCase):
    
    def setUp(self):
        """
        - Create a stock without sale data (sell_date, sell_price) to test DB logic for unsold stocks.
        - Create a stock with sale data (sell_date, sell_price) to test DB logic for sold stocks.
        """
        self.unsold_stock = Stock.objects.create(
            ticker="CLLS",
            purchase_date= "2021-05-03",
            purchase_price= 18.0,
            current_price= 2.0,
            exchange= "NASDAQ",
        )
        self.sold_stock = Stock.objects.create(
            ticker="TSLA",
            purchase_date= "2021-05-03",
            purchase_price= 18.0,
            current_price= 2.0,
            exchange= "NASDAQ",
            sell_date= "2021-06-28",
            sell_price= 16.0
        )
        
        
    def test_get_current_price(self):
        self.assertEquals(Stock.get_current_price(self.unsold_stock), "$2.0") # Python automatically removes trailing zeros
        self.assertEquals(Stock.get_current_price(self.sold_stock), "$2.0")
    
    
    def test_get_purchase_price(self):
        self.assertEquals(Stock.get_purchase_price(self.unsold_stock), "$18.0")
        self.assertEquals(Stock.get_purchase_price(self.sold_stock), "$18.0")
    
    def test_get_sell_date(self):
        self.assertEquals(Stock.get_sell_date(self.unsold_stock), '')
        self.assertEquals(Stock.get_sell_date(self.sold_stock), "2021-06-28")
      
    def test_get_sell_price(self):
        self.assertEquals(Stock.get_sell_price(self.unsold_stock), '')
        self.assertEquals(Stock.get_sell_price(self.sold_stock), "$16.0")
    
    def test_get_profit(self):
        self.assertEquals(Stock.get_profit(self.unsold_stock), "-88.9%")
        self.assertEquals(Stock.get_profit(self.sold_stock), "-11.1%")
    
  