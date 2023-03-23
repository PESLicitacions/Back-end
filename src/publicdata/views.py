from django.shortcuts import render
import requests
import json
from django.http import JsonResponse


def get_data(request):
    context = {}
    
    num_rows = 20
    base_url = 'https://analisi.transparenciacatalunya.cat/resource/a23c-d6vp.json?$limit=20'
    
    response_API = requests.get(base_url)
    data = response_API.text
    parse_json = json.loads(data)
    print(len(parse_json))
    return JsonResponse(data, safe=false)
