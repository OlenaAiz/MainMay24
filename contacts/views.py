from django.shortcuts import render, redirect
from .models import BookATour, GetInTouch
from .forms import BookATourForm, GetInTouchForm


def index(request):
    if request.method == 'POST':
        form = GetInTouchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

        form = BookATourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    if request.method == 'GET':
        message = GetInTouch.objects.all().order_by('-id')
        book_a_tour = BookATour.objects.all()
        form_book = BookATourForm()
        form_get_in_touch = GetInTouchForm()

        context = {
            'message': message,
            'book_a_tour': book_a_tour,
            'form_book': form_book,
            'form_get_in_touch': form_get_in_touch
        }
        return render(request, 'contacts.html', context)