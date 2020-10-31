from typing import Counter
from django.shortcuts import render
from .models import Recipes, RecipesInformation # for python3 manage.py shell
from django.contrib.auth.models import User


def search(request):
    context = {
        'title': 'Search',
    }

    if request.method == 'POST':
        keywords = request.POST['keywords']
        context['keywords'] = keywords
        print(context['keywords'])
        context['recipes'] = search_information(keywords)
        print(context['recipes'])
        return render(request, 'search.html', context)
    return render(request, 'search.html', context)



def filter(keywords):
    results = []
    users = User.objects.filter(username=keywords)
    for user in users:
        recipes = Recipes.objects.filter(user=user)
        for recipe in recipes:
            results.append(f'{recipe.name} by {recipe.user}')
    return results

def search_information(keywords):
    results = []
    infos = RecipesInformation.objects.filter(information__contains=keywords)
    for info in infos:
        recipe = info.recipe_id
        results.append(f'{recipe.name} by {recipe.user}')
    return results
