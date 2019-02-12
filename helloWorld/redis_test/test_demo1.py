# -*- coding:utf-8 -*-
# pip install redis
import redis

pool = redis.ConnectionPool(host='192.168.2.122', port=6379)
r = redis.Redis(connection_pool=pool)
r.set('kw', 'hello world')
print(r.get('kw'))

r.hset("hash_test", "key1", '你好')
r.hset("hash_test", "key2", '啊！')