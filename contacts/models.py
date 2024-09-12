from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class GetInTouch(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?(380)?\d{9,15}$',
                                 message='Phone number must be entered in the format: +999999999. '
                                         'Up to 15 digits allowed.')

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, validators=[phone_regex])
    message = models.TextField()
    is_confirmed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.email}-{self.phone}'

    class Meta:
        verbose_name = 'Get in Touch'
        verbose_name_plural = 'Get in Touch'
        ordering = ['-date_created']


class BookATour(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?(380)?\d{9,15}$',
                                 message='Phone number must be entered in the format: +999999999. Up to 15 digits.')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, validators=[phone_regex])
    date = models.DateField()
    count = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)

    is_confirmed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.email}-{self.phone} / {self.date}'

    class Meta:
        verbose_name = 'Book A Tour'
        verbose_name_plural = 'Book A Tour'
        ordering = ['-date_created']
