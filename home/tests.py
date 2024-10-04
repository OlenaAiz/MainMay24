from django.test import TestCase
from Home.models import *

# Create your tests here.


class CreateYourTourStyleTestCase(TestCase):
    def setUp(self):
        CreateYourTourStyle.objects.create(name='city explorer', is_visible=True, sort='1',
                                       style_photo='createyourtourstyle/%Y/%m/%d/', buttonname='Get in Touch', slug=True)
        CreateYourTourStyle.objects.create(name='historical excursion', is_visible=True, sort='2', style_photo='createyourtourstyle/%Y/%m/',
                                           buttonname='Get in Touch', slug=True)

    def test_createyourtourstyle(self):
        cityexplorer = CreateYourTourStyle.objects.get(name='city explorer')
        historicalexcursion = CreateYourTourStyle.objects.get(name='historical excursion')
        self.assertEqual(cityexplorer.name(), 'city explorer')
        self.assertEqual(cityexplorer.is_visible, True)
        self.assertEqual(historicalexcursion.is_visible, True)
        self.assertEqual(cityexplorer.sort, '1')
        self.assertEqual(cityexplorer.style_phoyo, '1')
        self.assertEqual(cityexplorer.slug, True )
        self.assertEqual(historicalexcursion.sort, '2')
        self.assertEqual(cityexplorer.buttonname, 'Get in Touch')
        self.assertEqual(historicalexcursion.buttonname, 'Get in Touch')
        self.assertEqual(cityexplorer.is_visible, False)
        self.assertEqual(historicalexcursion.is_visible, False)


class DiscoverNewHorizonTestCase(TestCase):

    def setUp(self):
        DiscoverNewHorizon.objects.create(name='about us', description='great company with various routes', photo='1',
                                          buttonname='Get in Touch')
    def test_discover_new_horizon(self):
        aboutus = DiscoverNewHorizon.objects.get(name='about us')
        whychooseus = DiscoverNewHorizon.objects.get(name='why choose us')
        ourmission = DiscoverNewHorizon.objects.get(name='our mission')
        self.assertEqual(aboutus.name(), 'about us')
        self.assertEqual(aboutus.photo, '1')
        self.assertEqual(aboutus.description, 'great company with various routes')
        self.assertEqual(aboutus.buttonname, 'Get in Touch')

class OurServicesTestCase(TestCase):

class HotToursTestCase(TestCase):

class OurStaffTestCase(TestCase):

class BookTourNowTestCase(TestCase):

class GalleryTestCase(TestCase):

class ContactsTestCase(TestCase):

class SwiperTestCase(TestCase):


