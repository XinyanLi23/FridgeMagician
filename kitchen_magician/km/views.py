from django.shortcuts import render

# Create your views here.


trending_recipes = [
    {
        "img": "images/slider/K2O.jpg"
    },
    {
        "img": "images/slider/K3O.jpg"
    },
        {
        "img": "images/slider/K4O.jpg"
    },
        {
        "img": "images/slider/K5O.jpg"
    }
]

groups = [
    {
        "group": "Vegan Group",
        "img": "images/groups/vegan.jpg",   
    },
    {
        "group": "Keto Group",
        "img": "images/groups/keto.jpg",   
    },
    {
        "group": "Vegetarian Group",
        "img": "images/groups/vegetarian.jpg",   
    },
    {
        "group": "Gluten Free Group",
        "img": "images/groups/gluten-free.jpg",   
    },
    {
        "group": "Pescatarian Group",
        "img": "images/groups/pescatarian.jpg",   
    },
    {
        "group": "Paleo Group",
        "img": "images/groups/paleo.jpg",   
    },
    {
        "group": "Low Carb Group",
        "img": "images/groups/low-carb.jpg",   
    },
    {
        "group": "Raw Group",
        "img": "images/groups/raw.jpg",
    },
]

trending_recipes_carousel = [
    {
        "img": "images/slider/K2O.jpg",
        "alt": "k20"
    },
    {
        "img": "images/slider/K3O.jpg",
        "alt": "k30"
    },
        {
        "img": "images/slider/K4O.jpg",
        "alt": "k40"
    },
        {
        "img": "images/slider/K5O.jpg",
        "alt": "K50"
    }
]

def home(request):
    context = {
        "trending_recipes": trending_recipes,
        "trending_recipes_carousel": trending_recipes_carousel,
        "groups": groups,
    }
    return render(request, 'home.html', context)

def test(request):
    return render(request, 'notes/test.html', {'title': 'Test'})
