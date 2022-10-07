from django.shortcuts import redirect, render
from .models import Review
from .forms import ReviewForm

def create(req):
    if req.method == 'POST':
        data = ReviewForm(req.POST)

        if data.is_valid():
            data.save()

            return redirect('reviews:index')

    else:
        data = ReviewForm()

    return render(req, 'reviews/create.html', {'data': data})


def index(req):
    data = Review.objects.all().order_by('id')

    return render(req, 'reviews/index.html', {'data': data})


def detail(req, _id):
    db_data = Review.objects.get(id=_id)

    return render(req, 'reviews/detail.html', {'data': db_data})


def update(req, _id):
    db_data = Review.objects.get(id=_id)

    if req.method == 'POST':
        data = ReviewForm(req.POST, instance=db_data)

        if data.is_valid():
            data.save()

            return redirect('reviews:index')

    else:
        data = ReviewForm(instance=db_data)

    return render(req, 'reviews/create.html', {'data': data})


def delete(req, _id):
    Review.objects.get(id=_id).delete()

    return redirect('reviews:index')