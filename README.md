# easy_thread
## The easiest way to make a thread


```sh
from easy_thread import easy_thread

def hello():
	while True:
		print('Hello!')

def goodbye():
	while True:
		print('goodbye!')

easy_thread(hello)
easy_thread(goodbye)
```

This program adds thread with function hello() and function goodbye()
