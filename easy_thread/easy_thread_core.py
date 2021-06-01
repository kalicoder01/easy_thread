from .easy_thread_utils import *



class EasyThread():
	def __init__(self, func):
		self.func = func
		self.threads_name = []
		self.stoppable = False

	def run(self, amount = 1):
		for i in range(amount):
			easy_thread_util = EasyThreadUtils(self.func)	

			easy_thread_util.start()
			self.threads_name.append(easy_thread_util)	

	def stop(self):
		self.stoppable = True

	def get_names(self) -> str:
		return threads_name	
		
