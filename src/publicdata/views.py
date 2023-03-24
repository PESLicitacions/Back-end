from django.shortcuts import render
import requests
import json
from django.http import JsonResponse


def get_data(request):
    context = {}
    
    num_rows = '212594'
    base_url = 'https://analisi.transparenciacatalunya.cat/resource/a23c-d6vp.json?$limit=' + num_rows
    response_API = requests.get(base_url)
    data = response_API.text
    parse_json = json.loads(data)
    print(len(parse_json))
    return JsonResponse(data, safe=False)
