from django.shortcuts import render

def search(request):
    context = {
        'title': 'Search',
    }

    if request.method == 'POST':
        keywords = request.POST['keywords']
        print(keywords)
        context['keywords'] = keywords
        return render(request, 'search.html', context)
    return render(request, 'search.html', context)

