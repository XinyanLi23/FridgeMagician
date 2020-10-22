from django.shortcuts import render

# Create your views here.


trending_recipes = [
    {
        "img": "images/K2O.jpg"
    },
    {
        "img": "images/K3O.jpg"
    },
        {
        "img": "images/K4O.jpg"
    },
        {
        "img": "images/K5O.jpg"
    }
]

def home(request):
    context = {
        "trending_recipes": trending_recipes,
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {'title': 'About'})

