from django.shortcuts import render
from .forms import MemoryModelForm
from .model_holder import model


def index(request):
    form = MemoryModelForm(request.POST or None)
    if form.is_valid():
        review = form.cleaned_data.get('review')
        result = model(review).item()
        context = {'form': form, 'result': f'Review is {result}'}
        return render(request, 'index.html', context)

    return render(request, 'index.html', {'form': form})
