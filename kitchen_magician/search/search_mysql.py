# from search.models import RecipeTemp # for python3 manage.py shell
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", __file__)
# import django
# django.setup()

from .models import Recipes
from .models import RecipesTypes
from .models import RecipesTypesItems
from .models import RecipesInformation
from .models import RecipesIngredients
from .models import RecipesIngredientsItems
from django.contrib.auth.models import User


recipes = [
    {
        "name": "Simple Garlic Shrimp",
        "information": "If you like shrimp and LOVE garlic, I hope you give this fast and delicious recipe a try soon. Enjoy!"
    },
        {
        "name": "Grilled Marinated Shrimp",
        "information": "This makes the best shrimp! Remove from skewers and serve on a bed of pasta with sauce for a great meal."
    }
]

class UpdateRecipes():
    def __init__(self, user_name):
        self.user_name = user_name

    # update recipe information
    def update_recipes_information(self, recipe):
        information = "If you like shrimp and LOVE garlic, I hope you give this fast and delicious recipe a try soon. Enjoy!"
        info = RecipesInformation(information=information, recipe_id=recipe)
        info.save()


    # update recipes
    def update_recipes(self):
        user_name = self.user_name
        user = User.objects.filter(username=user_name).first()
        recipe_1 = Recipes(user=user, name="Simple Garlic Shrimp")
        recipe_1.save()
        self.update_recipes_information(recipe_1)

