from typing import Counter
from django.shortcuts import render


test = ['lunch', 'lunch', 'lunch', 'dinner', 'dinner', 'breakfast']

def search(request):
    context = {
        'title': 'Search',
    }

    if request.method == 'POST':
        keywords = request.POST['keywords']
        print(keywords)
        context['keywords'] = filter(keywords)
        
        return render(request, 'search.html', context)
    return render(request, 'search.html', context)

def filter(keywords):

    return keywords + '-' + str(test.count(keywords))
