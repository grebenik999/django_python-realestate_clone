from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Listing


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)

    return render(request, 'listings/listings.html', {'listings': page_listings})


def listing(request, listing_id):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
