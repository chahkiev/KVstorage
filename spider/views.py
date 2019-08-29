import requests
import json
import ast
import datetime
from tarantool import Connection

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


def correct_body(body):
    print(body)
    logger("correct_body()", body)
    try:
        body = body.decode("utf-8")
        body = ast.literal_eval(body)
    except:
        return False
    # return isinstance(body['key'], str) and isinstance(body['value'], dict)
    return True


def key_exists(key):
    logger("key_exists()", key)
    c = Connection("127.0.0.1", 3301)
    print("key_exists()")
    exist = list(c.select("KVstorage", key))
    print(exist != [])
    return exist != []


def add_kv(key, value):
    logger("add_kv()", key+" "+value)
    c = Connection("127.0.0.1", 3301)
    print("add_key()")
    try:
        c.insert("KVstorage", (key, value))
        print(c.select("KVstorage", key))
        return True
    except:
        return False


def update_value(key, value):
     logger("update_value", key+" "+value)
     c = Connection("127.0.0.1", 3301)
     print("update_value()")
     c.update("KVstorage", key, [('=', 1, value)] )
     print(c.select("KVstorage", key))


def get_key(body):
    logger("get_key()", body)
    body = body.decode("utf-8")
    body = ast.literal_eval(body)
    key = body['key']
    return key


def get_value(body):
    logger("get_body()", body)
    body = body.decode("utf-8")
    body = ast.literal_eval(body)
    value = body['value']
    return value


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


def kv(request):
    print('JUST KEY-VALUE')
    print(request.body)
    body = b'{"key": "test", "value": {"foo": "bar"}}'
    # body = request.body

    if not correct_body(body):
        print('Parse ERROR')
        return HttpResponse(status=400)

    if request.method == 'GET':  # change to POST
        key = get_key(body)
        value = get_value(body)
        if key_exists("key777"):  # change for KEY
            return HttpResponse(status=409)
        else:
            add_kv("key777", "value88005553535") # change for KEY and VALUE
            return HttpResponse("Successfully added")

    # return render(request, 'spider/kv.html')


def id(request, id):
    print('ID KEY-VALUE')
    print(request.method)
    body = b'{"key": "test", "value": {"foo": "bar"}}'
    # body = request.body

    if request.method == 'GET':   # change to PUT
        if not correct_body(body):
            print('Parse ERROR PUT')
            return HttpResponse(status=400)
        if not key_exists("key1"): # change to KEY
            return HttpResponse(status=404)
        else:
            update_value('key1', 'value15') # change to ID nad VALUE
            return HttpResponse("Successfully updated")


    elif request.method == 'GET':
        if not key_exists(id): # change for ID
            return HttpResponse(status=404)
        else:
            get_kv(id) # change for ID
            print(get_kv(id))
            # return render(request, 'spider/id.html', {'json': get_kv("key1")})
            return HttpResponse(get_kv(id))

    elif request.method == 'GET':  # change to DELETE
        if not key_exists("key1"):   # change for id
            return HttpResponse(status=404)
        else:
            delete_kv("key1") # change for id
            return HttpResponse("Successfully deleted")

    #
    # return render(request, 'spider/id.html')
