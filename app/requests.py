import urllib.request,json
from .models import Quote
from config import Config

base_url = 'http://quotes.stormconsultancy.co.uk/random.json'





def get_quote():
    get_quote_details_url = base_url

    url = urllib.request.urlopen(get_quote_details_url)
    quote_details_data = url.read()
    quote_details_response = json.loads(quote_details_data)

  
    id = quote_details_response.get('id')
    author = quote_details_response.get('author')
    quote =  quote_details_response.get('quote')

    quote_object = Quote(id, author, quote)

    return quote_object