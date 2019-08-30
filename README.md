# Key-Value Storage

Задание:
* Скачать/собрать Tarantool
* Реализовать kv-хранилище доступное по http

#

API:
* POST /kv body: {key: "test", "value": {SOME ARBITRARY JSON}};
* PUT kv/{id} body: {"value": {SOME ARBITRARY JSON}};
* GET kv/{id};
* DELETE kv/{id};
* POST  возвращает 409 если ключ уже существует;
* POST, PUT возвращают 400 если боди некорректное;
* PUT, GET, DELETE возвращает 404 если такого ключа нет;
* все операции логируются.

#

Стек технологий:
* Python3;
* Django - фреймворк на языке Python;
* Tarantool - NoSQL база данных;
* Github – репозиторий для кода.

## How to deploy


Tarantool:

```bash
# install utilities (if necessary)
$ apt-get -y install sudo
$ sudo apt-get -y install gnupg2
$ sudo apt-get -y install curl
$ curl http://download.tarantool.org/tarantool/1.10/gpgkey | sudo apt-key add -

# install 'lsb-release', to know the codename of your OS
$ sudo apt-get -y install lsb-release
$ release=`lsb_release -c -s`

# install boot tool 'https' for APT
$ sudo apt-get -y install apt-transport-https

# update source code repository list
$ sudo rm -f /etc/apt/sources.list.d/*tarantool*.list
$ echo "deb http://download.tarantool.org/tarantool/1.10/ubuntu/ ${release} main" | sudo tee /etc/apt/sources.list.d/tarantool_1_10.list
$ echo "deb-src http://download.tarantool.org/tarantool/1.10/ubuntu/ ${release} main" | sudo tee -a /etc/apt/sources.list.d/$ $ $ tarantool_1_10.list

# install tarantool
$ sudo apt-get -y update
$ sudo apt-get -y install tarantool
```

```bash
$ tarantool
tarantool> box.cfg{listen = 3301}
tarantool> s = box.schema.space.create('KVstorage')
tarantool> s:format({  {name = 'key', type = 'string'}, {name = 'value', type = 'string'}  })
tarantool> s:create_index('primary', { type = 'hash', parts = {'key'}   })
tarantool> box.schema.user.grant('guest', 'read,write,execute', 'universe')
```

Django app:

```bash
$ cd ~
$ git clone https://github.com/chahkiev/KVstorage.git
$ cd KVstorage/
$ python3 -mvenv venv
$ source venv/bin/activate
$ pip3 install django
$ pip3 install -r requirements.txt
$ python3 manage.py runserver
```

## Testing

```bash
# while the server is running
$ cd ~
$ cd KVstorage/
$ python3 -m unittest -v
```
