import requests
import json
import ast
from tarantool import Connection

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


def correct_body(body):
    print(body)
    try:
        body = body.decode("utf-8")
        body = ast.literal_eval(body)
    except:
        return False
    # return isinstance(body['key'], str) and isinstance(body['value'], dict)
    return True


def key_exists(key):
    # c = Connection("127.0.0.1", 3301)
    # working with TARANTOOL
    return False

def get_key(body):
    body = body.decode("utf-8")
    body = ast.literal_eval(body)
    key = body['key']
    return key

def get_value(body):
    body = body.decode("utf-8")
    body = ast.literal_eval(body)
    key = body['value']
    return value

def main(request):
    print("I AM MAIN VIEW FUNCTION")
    return render(request, 'spider/main.html')


def kv(request):
    print('JUST KEY-VALUE')
    print(request.body)
    body = b'{"key": "test", "value": {"foo": "bar"}}'
    # body = request.body

    if not correct_body(body):
        print('Parse ERROR')
        return HttpResponse(status=400)

    if request.method == 'POST':
        key = get_key(body)
        if not key_exists(key):
            return HttpResponse(status=409)
        else:
            # add key
            pass

    return render(request, 'spider/kv.html')


def id(request, id):
    print('ID KEY-VALUE')
    print(request.method)
    if request.method == 'PUT':
        if not correct_body(request):
            print('Parse ERROR PUT')
            return HttpResponse(status=400)
        if not key_exists(23):
            return HttpResponse(status=404)
        else:
            # update value
            pass

    elif request.method == 'GET':
        if not key_exists(23):
            return HttpResponse(status=404)
        else:
            # get value
            pass

    elif request.method == 'DELETE':
        if not key_exists(23):
            return HttpResponse(status=404)
        else:
            # delete value
            pass

    return render(request, 'spider/id.html')
