# -*- coding: UTF-8 -*-
import sys
from models import sensors
from util.Serializer import serializer
from django.http import JsonResponse
import json
from django.utils import timezone
import os
# csrf defend
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_node(request):
    if request.method == 'POST':
        req = json.loads(request.body)
