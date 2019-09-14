#!/usr/bin/env tarantool

box.cfg{
    listen = 3301,
    background = true,
    log = 'KVstorage.log',
    pid_file = 'KVstorage.pid'
}
s = box.schema.space.create('KVstorage')
s:format({  {name = 'key', type = 'string'}, {name = 'value', type = 'string'}  })
s:create_index('primary', { type = 'hash', parts = {'key'}   })
box.schema.user.grant('guest', 'read,write,execute', 'universe')
