
from redis import Redis
import time
from django.conf import settings
from typing import Callable, TypeVar,Callable

r: Redis= Redis(host=settings.REDIS_HOST, port=6379, decode_responses=True)
counter: bool = r.set("counter", "0")

RT = TypeVar('T')

def counter(func) -> Callable[..., RT]:
	def wrapper(*args, **kw) -> RT:
		req: int = r.incr("counter")
		print(req)
		return func(*args, **kw)
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
