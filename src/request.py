from .recipe import Recipe
from .globals_ import RECIPES, BOOST


class Request:
    def __init__(self, item: str, rate: float, multiplier: float = BOOST):
        self.item = item
        self.rate = rate
        self.multiplier = multiplier
        self.paths = []

        self.resolve_component_graph()

    def resolve_component_graph(self):
        try:
            item_recipes = RECIPES[self.item]

        except KeyError:
            self.multiplier = 1

        else:
            for recipe in item_recipes:
                factories = recipe.factories_required(self.rate, self.multiplier)
                recipe_components = [recipe.factory, factories]

                for component in recipe.component_rates(self.multiplier):
                    component_required = factories * component[1]
                    request = Request(component[0], component_required, self.multiplier)
                    recipe_components.append(request)

                self.paths.append(recipe_components)
