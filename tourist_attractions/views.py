from multiprocessing import context
from django.shortcuts import render

# Create your views here.
attractions = [
    {'attraction_name': 'Grand Place', 'city': 'Brussels'},
    {'attraction_name': 'The Canals of Bruges', 'city': 'Bruges'},
    {'attraction_name': 'The Belfry of Bruges', 'city': 'Bruges'},
    {'attraction_name': 'Gravensteen and Old Town', 'city': 'Ghent'},
    {'attraction_name': 'Basilica of the Holy Blood', 'city': 'Bruges'},
    {'attraction_name': 'Meuse Valley', 'city': 'Dinant'},
    {'attraction_name': 'Mechelen Old Town', 'city': 'Mechelen'},
    {'attraction_name': 'Ghents Canals', 'city': 'Ghent'},
    {'attraction_name': 'Waterloo', 'city': 'Waterloo'},
    {'attraction_name': 'Grand Place (Grote Markt)', 'city': 'Antwerp'},
    {'attraction_name': 'Semois Valley', 'city': 'Semois Valley'},
    {'attraction_name': 'Cathedral of Saint Bavo', 'city': 'Ghent'},
    {'attraction_name': 'Antwerp Art Museums', 'city': 'Antwerp'},
    {'attraction_name': 'Horta Museum and Town Houses', 'city': 'Brussels'},
    {'attraction_name': 'Cathedral of Our Lady', 'city': 'Antwerp'},
    {'attraction_name': 'Rubens House ', 'city': 'Antwerp'},
    {'attraction_name': 'MAS', 'city': 'Antwerp'},
    {'attraction_name': 'Antwerp Zoo', 'city': 'Antwerp'},
    {'attraction_name': 'Chocolate Nation', 'city': 'Antwerp'},
    {'attraction_name': 'Antwerp-Centraal Railway Station', 'city': 'Antwerp'}
]


def home(request):
    context = {"attractions": attractions}
    return render(request, "tourist_attractions/home.html", context)
