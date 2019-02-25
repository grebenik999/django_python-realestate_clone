from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices, price_choises, state_choises


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'bedroom_choices': bedroom_choices,
        'price_choises': price_choises,
        'state_choises': state_choises
    }

    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')

    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    print('mvp', mvp_realtors)

    return render(request, 'pages/about.html', {'realtors': realtors, 'mvp_realtors': mvp_realtors})
