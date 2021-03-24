from ..models import Chef


def list_chefs():
    chef = Chef.objects.all()
    return chef
