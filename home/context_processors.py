from .models import Contacts


def contacts(request):
    contacts = Contacts.objects.first()
    return {'contacts': contacts}