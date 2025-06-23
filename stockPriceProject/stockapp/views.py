from django.shortcuts import render
import yfinance as yf
# Create your views here.
def get_stock_price(request):
    context = {}
    if request.method == "POST":
        symbol = request.POST.get('symbol')
        try:
            stock = yf.Ticker(symbol)
            price = stock.info['regularMarketPrice']
            context['price'] = price
            context['symbol'] = symbol.upper()
        except:  
            context['error'] = "Invalid company symbol or data unavailable"
    
    return render(request,'stockapp/stock_form.html',context)