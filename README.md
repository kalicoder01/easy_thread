# easy_thread
## The easiest way to make a thread

### PyPi (download module): https://pypi.org/project/easy-thread/



```sh
from easy_thread import EasyThread

def hello():
	while True:
		print('hello')

def goodbye():
	while True:
		print('bye')

thread = EasyThread(goodbye)
thread.run(10)

thread2 = EasyThread(hello)
thread2.run(5)
```

