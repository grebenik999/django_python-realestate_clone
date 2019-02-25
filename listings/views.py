from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

from .choices import bedroom_choices, price_choises, state_choises
from .models import Listing


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)

    return render(request, 'listings/listings.html', {'listings': page_listings})


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    return render(request, 'listings/listing.html', {'listing': listing})


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Search by Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)

    # Search by City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # Search by State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Search by Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Search by Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'bedroom_choices': bedroom_choices,
        'price_choises': price_choises,
        'state_choises': state_choises,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
