from django.forms import ModelForm, widgets, ChoiceField
from .models import Stock
from datetime import date
from django.core.exceptions import ValidationError


def clean_dates(cleaned_data):
    pd = cleaned_data.get("purchase_date")
    sd = cleaned_data.get("sell_date")
    # ensure purchase date has already passed
    if pd > date.today():
        raise ValidationError("Purchase date must be in the past")
    if sd is not None:
        # ensure sell date is afer purchase date
        if sd < pd:
            raise ValidationError("Sell date must be after purchase date")
        # ensure sell date has already passed 
        if sd > date.today():
            raise ValidationError("Sell date must be in the past")

            
        
def clean_prices(cleaned_data):
    pp = cleaned_data.get('purchase_price')
    cp = cleaned_data.get('current_price')
    sp = cleaned_data.get("sell_price")
    sd = cleaned_data.get("sell_date")
    
    # ensure stock prices are not negative
    if pp < 0 or cp < 0:
        raise ValidationError("Prices must be greater than $0.00")
    
    if sp is not None:
        if sp < 0:
            raise ValidationError("Prices must be greater than $0.00")
    
    # ensure user inputs stock price if stock is sold
    if sd is not None:
        if sp is None:
            raise ValidationError("Must input sell price if the stock is sold")
            
            
            
def clean_text(cleaned_data):
    ticker = cleaned_data.get('ticker')
    
    # ensure ticker is appropriate length
    ticker_chars = len(ticker)
    if ticker_chars < 2 or ticker_chars > 5:
        raise ValidationError("invalid ticker symbol")
    else:
        cleaned_data['ticker'] = ticker.upper()

EXCHANGES = (
    ("NYSE", "NYSE"),
    ("NASDAQ", "NASDAQ"),
    ("ADX", "ADX"),
    ("ASX", "ASX"),
    ("BOVESPA", "BOVESPA"),
    ("BSE-BOMBAY", "BSE-BOMBAY"),
    ("HKEX", "HKEX"),
    ("JPX", "JPX"),
    ("JSE", "JSE"),
    ("KRX", "KRX"),
    ("LSE", "LSE"),
    ("NSE-INDIA", "NSE-INDIA"),
    ("OMXC-COPENHAGEN", "OMXC-COPENHAGEN"),
    ("SIX", "SIX"),
    ("SSE", "SSE"),
    ("SZSE", "SZSE"),
    ("TADAWUL", "TADAWUL"),
    ("TSE", "TSE"),
    ("TSX", "TSX"),
    ("TWSE", "TWSE")
)

    
class StockForm(ModelForm):
    
    class Meta:
        model = Stock
        fields = '__all__'
        widgets = {
            'ticker': widgets.TextInput(attrs={'placeholder': "ex: TSLA"}),
            'current_price': widgets.NumberInput(attrs={'placeholder': "(USD) ex: 23.6, 12.05"}),
            # 'exchange': widgets.TextInput(attrs={'placeholder': "ex: NYSE, NASDAQ"}),
            'purchase_date': widgets.DateInput(attrs={'type': 'date'}),
            'sell_date': widgets.DateInput(attrs={'type': 'date'}),
        }
    
    exchange = ChoiceField(choices=EXCHANGES)
        
    def clean(self):
        cleaned_data = super().clean()
        clean_dates(cleaned_data)
        clean_prices(cleaned_data)
        clean_text(cleaned_data)