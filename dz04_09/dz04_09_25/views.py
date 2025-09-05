from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
import json

def index(request):
    return HttpResponse("Привет")

def company_info(request):
    avto = Avtosallon("AwesomeCorp", 2020, ["Alice", "Bob", "Charlie"])
    return JsonResponse(avto, safe=False, encoder=AvtosallonEncoder)

class Avtosallon:
    def __init__(self,name,founded,employees):
        self.name = name
        self.founded = founded
        self.employees = employees

class AvtosallonEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Avtosallon):
            return{"name": obj.name, "founded": obj.founded, "employees": obj.employees}
        return super().default(obj)
    
