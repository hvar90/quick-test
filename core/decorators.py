import redis
import time
r = redis.Redis(host='redis', port=6379, decode_responses=True)
counter = r.set("counter", "0")

def counter(func):
	def wrapper(*args, **kw):
		requests = r.incr("counter")
		print(requests)
		func(*args, **kw)
	return wrapper
	
def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            instr = "'{0}', '{1}'".format(method.__name__, (te - ts) * 1000,)
            print (instr)
        return result
    return timed
