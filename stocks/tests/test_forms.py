from django.test import TestCase
from stocks.forms import StockForm


class TestForms(TestCase):
    
    
    
    
    def test_stock_form_valid_data(self):
        form = StockForm(data={
            'ticker': 'MTA',
            'purchase_date': '2020-11-13',
            'current_price': 2.00,
            'exchange': 'NYSE',
            'purchase_price': 1.00,
            'sell_date': '2021-12-12',
            'sell_price': 4.00
        })
        
        self.assertTrue(form.is_valid())
    
    
    
    
    
    def test_stock_form_invalid_data(self):
        form = StockForm(data={})
        
        try:
            self.assertTrue(form.is_valid())
        except TypeError: #unable to clean a form with no data
            pass
    
    
    
    
    def test_stock_form_clean_dates(self):
        # sell date is before purchase date
        form = StockForm(data={
            'ticker': 'MTA',
            'purchase_date': '2020-11-13',
            'current_price': 2.00,
            'exchange': 'NYSE',
            'purchase_price': 1.00,
            'sell_date': '2019-12-12',
            'sell_price': 4.00
        })
        self.assertFalse(form.is_valid())
        
        # sell date is in the future
        form = StockForm(data={
            'ticker': 'MTA',
            'purchase_date': '2020-11-13',
            'current_price': 2.00,
            'exchange': 'NYSE',
            'purchase_price': 1.00,
            'sell_date': '2100-12-12',
            'sell_price': 4.00
        })
        self.assertFalse(form.is_valid())

        # purchase date is in the future
        form = StockForm(data={
            'ticker': 'MTA',
            'purchase_date': '2100-11-13',
            'current_price': 2.00,
            'exchange': 'NYSE',
            'purchase_price': 1.00,
            'sell_date': '2019-12-12',
            'sell_price': 4.00
        })
        self.assertFalse(form.is_valid())
        
        
        
        
    def test_stock_form_clean_prices(self):
        # current price is negative
        form = StockForm(data={
            'ticker': 'MTA',
            'purchase_date': '2020-11-13',
            'current_price': -2.00,
            'exchange': 'NYSE',
            'purchase_price': 1.00,
            'sell_date': '2021-12-12',
            'sell_price': 4.00
        })
        self.assertFalse(form.is_valid())
        
        # sell date but no sell price
        form = StockForm(data={
            'ticker': 'MTA',
            'purchase_date': '2020-11-13',
            'current_price': -2.00,
            'exchange': 'NYSE',
            'purchase_price': 1.00,
            'sell_date': '2021-12-12'
            })
        self.assertFalse(form.is_valid())
        

    
    def test_stock_form_clean_text(self):
        # ticker is too long
        form = StockForm(data={
            'ticker': 'TESLASHARES',
            'purchase_date': '2020-11-13',
            'current_price': -2.00,
            'exchange': 'NYSE',
            'purchase_price': 1.00,
            'sell_date': '2021-12-12'
            })
        self.assertFalse(form.is_valid())