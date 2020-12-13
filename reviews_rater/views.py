from django.shortcuts import render

from .forms import ReviewForm
from .model_holder import model

result_mapper = {0: 'bad', 1: 'good'}


def index(request):
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        review = form.cleaned_data.get('review')
        result = model(review).item()
        context = {'form': form, 'result': f'Review is {result_mapper[result]}'}
        return render(request, 'index.html', context)

    return render(request, 'index.html', {'form': form})
