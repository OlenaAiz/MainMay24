# from django.shortcuts import render
# from django.http import HttpResponse
import random
from .models import (CreateYourTourStyle, OurServices, OurStaff, Gallery, HotTours, Contacts, DiscoverNewHorizon,
                     BookTourNow, Swiper, HeaderFooter)

from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'main.html'

# Create your views here.
# def index(request):
    # tours = CreateYourTourStyle.objects.all()
    # for item in tours:
    #     print(item.name)
    # for item in name:
    # for hottours in hottours.objects.filter(category=item, is_visible=True):
    # print(hottours.name)
    # tourStyle = CreateYourTourStyle.objects.filter(is_visible=True)
    # tourStyle = CreateYourTourStyle.objects.get(id=1)
    # tourStyle = CreateYourTourStyle.objects.first()
    # tourStyle = CreateYourTourStyle.objects.last()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['staff'] = OurStaff.objects.all()
        context['tours'] = HotTours.objects.all()
        for item in context['tours']:
            item.reviewstar_new = range(item.reviewstar)

        context['services'] = OurServices.objects.all()
        context['gallery'] = Gallery.objects.all()
        context['contacts'] = Contacts.objects.first()
        context['style'] = CreateYourTourStyle.objects.all()
        context['horizon'] = DiscoverNewHorizon.objects.all()
        context['horizon_photo'] = random.choice(context['horizon'])
        context['subscribe'] = BookTourNow.objects.first()
        context['swiper'] = Swiper.objects.all()
        context['headerfooter'] = HeaderFooter.objects.all()

        return context