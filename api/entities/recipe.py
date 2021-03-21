class Recipe:
    def __init__(self, title, ingredients, steps, time, servings):
        self.__title = title
        self.__ingredients = ingredients
        self.__steps = steps
        self.__time = time
        self.__servings = servings

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, ingredients):
        self.__ingredients = ingredients

    @property
    def steps(self):
        return self.__steps

    @steps.setter
    def steps(self, steps):
        self.__steps = steps

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, time):
        self.__time = time

    @property
    def servings(self):
        return self.__servings

    @servings.setter
    def servings(self, servings):
        self.__servings = servings