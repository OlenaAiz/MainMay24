from django.db import models
# from ckeditor.fields import RichTextField
# Create your models here.


class CreateYourTourStyle(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField()
    style_photo = models.ImageField(upload_to='createyourtourstyle/%Y/%m/%d/', blank=True, null=True)
    buttonname = models.CharField(max_length=100)
    slug = models.SlugField(default=True)

    def __iter__(self):
        for tour in self.tours.filter(is_visible=True):
            yield tour

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Tour Style'
        verbose_name_plural = 'Tour Styles'
        ordering = ('sort',)


class DiscoverNewHorizon(models.Model):
    # name_of_class = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    photo = models.ImageField(upload_to='discoverNewHorizon/%Y/%m/%d/')
    buttonname = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}{self.description}{self.buttonname}'

    class Meta:
        verbose_name = 'Discover New Horizon'
        verbose_name_plural = 'Discover New Horizons'
        ordering = ('name',)


class OurServices(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    icon = models.CharField(max_length=100, default='fl-bigmug-line-equalization3')

    def __str__(self):
        return f'{self.name}{self.description}'

    class Meta:
        verbose_name = 'Our Service'
        verbose_name_plural = 'Our Services'
        ordering = ('name',)


class HotTours(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    photo = models.ImageField(upload_to='hottours/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    reviewstar = models.PositiveSmallIntegerField()
    reviews = models.PositiveSmallIntegerField()
    tourstyle = models.ForeignKey(CreateYourTourStyle, on_delete=models.CASCADE, related_name='tours')
    date = models.DateField(auto_now_add=True)
    # photo = models.ImageField(upload_to='hotTours/%Y/%m/%d/', blank=True, null=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return (f'{self.name}{self.date}'
                f'{self.description}{self.photo}{self.price}{self.reviewstar}{self.reviews}{self.tourstyle}')

    class Meta:
        verbose_name = 'Hot Tour'
        verbose_name_plural = 'Hot Tours'
        ordering = ('date',)


class OurStaff(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    phone_number = models.TextField(max_length=255)
    photo = models.ImageField(upload_to='ourstaff/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return f'{self.name}-{self.position}'

    class Meta:
        verbose_name = 'Our Staff'
        verbose_name_plural = 'Our Staff'
        ordering = ('position',)


class BookTourNow(models.Model):
    description1 = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    buttonname = models.CharField(max_length=100, unique=True)
    is_confirmed = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='booktournow', blank=True, null=True)

    def __str__(self):
        return f'{self.description1}{self.buttonname}'

    class Meta:
        verbose_name = 'Book A Tour Now'
        verbose_name_plural = 'Book A Tour Now'
        ordering = ('description1',)


class Gallery(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
        ordering = ('name',)


class Contacts(models.Model):
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.TextField(max_length=20)

    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.address}'

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ('address',)


class Swiper(models.Model):
    photo_swiper = models.ImageField(upload_to='swiper', blank=True, null=True)
    advertise1 = models.CharField(max_length=100, unique=True)
    text12 = models.CharField(max_length=100, unique=True)
    text21 = models.CharField(max_length=100, unique=True)
    button = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.text12}-{self.text21}-{self.button}'

    class Meta:
        verbose_name = 'Swiper'
        verbose_name_plural = 'Swipers'
        ordering = ('text12', )


class HeaderFooter(models.Model):
    name = models.CharField(max_length=100, unique=True)
    photo = models.ImageField(upload_to='headerfooter', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'headerfooter'
        verbose_name_plural = 'headerandfooter'
        ordering = ('name',)