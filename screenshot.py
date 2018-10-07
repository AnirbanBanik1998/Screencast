import os
import sys
import threading
import time
import threading
class Screenshot:
	def __init__(self, RUNTIME):
		self.r=RUNTIME
		self.start=time.time()
		self.stop=time.time()
		self.k=0
		
	def capture(self, k):
		#evt=threading.Event()
		s="./Screenshots/Screenshot"+str(k)+".png"
		os.system("scrot "+s)
		#evt.set()
		
	def begin(self):
		while True:
			time.sleep(0.1)
			p=threading.Thread(target=self.capture, args=(self.k, ))
			p.daemon = True
			p.start()
			self.stop=time.time()
			self.k+=1
			if int(self.stop-self.start)>int(self.r):
				break
if __name__=="__main__":
	obj=Screenshot(sys.argv[1])
	obj.begin()
