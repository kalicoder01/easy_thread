# easy_thread
## The easiest way to make a thread

### PyPi (download module): https://pypi.org/project/easy-thread/



```py
from easy_thread import easy_thread

def hello():
	while True:
		print('hello')

def goodbye():
	while True:
		print('bye')

easy_thread(hello)
easy_thread(goodbye)
```

