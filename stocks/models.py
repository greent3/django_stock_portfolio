from django.db.models import Model, CharField, DateField, DecimalField


class Stock(Model):
    
    class Meta:
      ordering = ['-purchase_date']  
      
    def __str__(self):
        return f'{self.ticker} " " {str(self.purchase_date)}'
    
    ticker = CharField( max_length=6, null=False, blank=False)
    purchase_date = DateField( null=False, blank=False)
    current_price = DecimalField( max_digits=7, null=False, blank=False, decimal_places=2)
    exchange = CharField( max_length=10, null=False, blank=False)
    purchase_price = DecimalField( max_digits=7, null=False, blank=False, decimal_places=2)
    sell_date = DateField( null=True, blank=True)
    sell_price = DecimalField( max_digits=7, null=True, blank=True, decimal_places=2)
    
    def get_current_price(self):
      return f'${self.current_price}'
    
    def get_purchase_price(self):
      return f'${self.purchase_price}'
        
    def get_sell_date(self):
      if self.sell_date is None:
        return ""
      return self.sell_date      
      
    def get_sell_price(self):
      if self.sell_price is None:
        return ""
      return f'${self.sell_price}'
    
    def get_profit(self):
      if self.sell_date is None:
        end_price = self.current_price
      else:
        end_price = self.sell_price
        
      result = ((end_price - self.purchase_price) / self.purchase_price) * 100 # calculate profit percentage
      formatted_result = "{:.1f}".format(result) # format to 2 decimal places
      return str(formatted_result) + "%"
        
      
    
    
    
    
