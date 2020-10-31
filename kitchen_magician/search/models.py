from django.db import models
from django.contrib.auth.models import User

class Recipes(models.Model):
    # CASCADE, once the user is deleted, the profile will be deleted automatically 
    image_folder = 'recipes_pics/'
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=100, verbose_name='Name')

    class Meta():
        db_table = 'recipes'

    def __str__(self):
        return f'{self.name} by {self.user.username}'

class RecipesTypes(models.Model):
    type = models.CharField(max_length=50)

    class Meta():
        db_table = 'recipes_types'

    def __str__(self):
        return self.type

class RecipesTypesItems(models.Model):
    # CASCADE, once the user is deleted, the profile will be deleted automatically 
    recipe_id = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    recipe_type_id = models.ForeignKey(RecipesTypes, on_delete=models.CASCADE)
    class Meta():
        db_table = 'recipes_types_items'

    def __str__(self):
        return f'{self.recipe_id.name} - {self.recipe_type_id.type}'

class RecipesIngredients(models.Model):
    ingredient = models.CharField(max_length=100)
    
    class Meta():
        db_table = 'recipes_ingredients'

    def __str__(self):
        return self.ingredient

class RecipesIngredientsItems(models.Model):
    # CASCADE, once the user is deleted, the profile will be deleted automatically 
    recipe_id = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    recipe_ingredient_id = models.ForeignKey(RecipesIngredients, on_delete=models.CASCADE)
    class Meta():
        db_table = 'recipes_ingredients_items'

    def __str__(self):
        return f'{self.recipe_id.name} - {self.recipe_ingredient_id.ingredient}'

class RecipesInformation(models.Model):
    # CASCADE, once the user is deleted, the profile will be deleted automatically 
    information = models.CharField(max_length=500)
    recipe_id = models.ForeignKey(Recipes, on_delete=models.CASCADE)

    class Meta():
        db_table = 'recipes_information'

    def __str__(self):
        return f'{self.recipe_id.name} - {self.information}'

class RecipesInstructions(models.Model):
    # CASCADE, once the user is deleted, the profile will be deleted automatically 
    instruction = models.CharField(max_length=500)
    recipe_id = models.ForeignKey(Recipes, on_delete=models.CASCADE)

    class Meta():
        db_table = 'recipes_instructions'

    def __str__(self):
        return f'{self.recipe_id.name} - {self.instruction}'


class RecipesVideos(models.Model):
    # CASCADE, once the user is deleted, the profile will be deleted automatically 
    video = models.CharField(max_length=1000)
    recipe_id = models.ForeignKey(Recipes, on_delete=models.CASCADE)

    class Meta():
        db_table = 'recipes_videos'

    def __str__(self):
        return self.recipe_id.name

class RecipesImages(models.Model):
    # CASCADE, once the user is deleted, the profile will be deleted automatically 
    image_folder = 'recipes_pics/'
    image = models.ImageField(default= image_folder + 'default_recipe_image.jpg', upload_to=image_folder)
    recipe_id = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    
    class Meta():
        db_table = 'recipes_images'

    def __str__(self):
        return f'{self.recipe_id.name} - {self.image}'
