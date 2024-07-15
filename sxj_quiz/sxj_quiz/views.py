from django.shortcuts import render
from django.contrib.staticfiles import finders
import json

def home(request):
    return render(request, "index.html")

def rules(request, parse):
    path = finders.find("json/rules.json")
    with open(path , 'r') as js:
        rules = json.load(js)

    ctxt = {
        "rules":rules[f"rules{parse}"]
    }
    
    return render(request, "rules.html", context=ctxt)