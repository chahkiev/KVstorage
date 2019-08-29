import requests
import json
import ast
import datetime
from tarantool import Connection

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt


def correct_body(body):
    print(body)
    logger("correct_body()", body)
    try:
        body = body.decode("utf-8")
        data = ast.literal_eval(body)

        print(data)
        print(data['key'])
        print(data['value'])
    except:
        return False

    print('key' in data and 'value' in data)
    return 'key' in data and 'value' in data
    # return isinstance(data['key'], str) and isinstance(data['value'], dict)
    # return True


def key_exists(key):
    logger("key_exists()", key)
    c = Connection("127.0.0.1", 3301)
    print("key_exists()")
    exists = list(c.select("KVstorage", key))
    print(exists != [])
    return exists != []


def add_kv(key, value):
    print("sdfgh")
    logger("add_kv()", key + " " + value)
    c = Connection("127.0.0.1", 3301)
    print("add_key()")
    try:
        c.insert("KVstorage", (key, value))
        print(c.select("KVstorage", key))
        return True
    except:
        return False


def update_value(key, value):
     logger("update_value", key + " " + value)
     c = Connection("127.0.0.1", 3301)
     print("update_value()")
     c.update("KVstorage", str(key), [('=', 1, value)] )
     print(c.select("KVstorage", key))


def get_key(body):
    logger("get_key()", body)
    body = body.decode("utf-8")
    data = ast.literal_eval(body)

    print(data['key'])
    key = data['key']
    return str(key)


def get_value(body):
    logger("get_body()", body)
    body = body.decode("utf-8")
    data = ast.literal_eval(body)

    print(data['value'])
    value = data['value']
    return str(value)


def get_kv(key):
    logger("get_kv()", key)
    c = Connection("127.0.0.1", 3301)
    print("get_kv()")
    print(c.select("KVstorage", key))
    return list(c.select("KVstorage", key))


def delete_kv(key):
    logger("delete_kv()", key)
    c = Connection("127.0.0.1", 3301)
    print("delete_kv()")
    c.delete("KVstorage", key)
    return


def logger(func, value):
    f = open("logfile.txt","a+")
    now = datetime.datetime.today().strftime("%Y-%m-%d  %H:%M:%S")
    message = now + " : " + str(func) + "    " + str(value) + "\n"
    f.write(message)
    f.close()
    return


@csrf_exempt
def kv(request):
    print('JUST KEY-VALUE')
    print(request.body)
    # body = b'{"key": "test", "value": {"foo": "bar"}}'
    body = request.body

    if not correct_body(body):
        print('Parse ERROR POST')
        return HttpResponse(status=400)

    if request.method == 'POST':
        key = get_key(body)
        print("key = ", key)
        value = get_value(body)
        print(key, "--", value)
        if key_exists(key):
            return HttpResponse(status=409)
        else:
            add_kv(key, value)
            return HttpResponse("Successfully added")


@csrf_exempt
def id(request, id):
    key = id
    print('ID KEY-VALUE')
    print(request.method)
    # body = b'{"key": "test", "value": {"foooo": "bar"}}'
    body = request.body

    if request.method == 'PUT':
        if not correct_body(body):
            print('Parse ERROR PUT')
            return HttpResponse(status=400)
        if not key_exists(key):
            return HttpResponse(status=404)
        else:
            value = get_value(body)
            update_value(key, value)
            return HttpResponse("Successfully updated")

    elif request.method == 'GET':
        if not key_exists(key):
            return HttpResponse(status=404)
        else:
            get_kv(key)
            print(get_kv(key))
            return HttpResponse(get_kv(key))

    elif request.method == 'DELETE':
        if not key_exists(key):
            return HttpResponse(status=404)
        else:
            delete_kv(key)
            return HttpResponse("Successfully deleted")
