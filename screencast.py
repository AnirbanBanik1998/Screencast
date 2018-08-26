import time
import pyscreenshot
import threading
from queue import Queue, Empty
class Screenshot:
	def __init__(self, RUNTIME, PROCESS=[]):
		self.r=RUNTIME
		self.start=time.time()
		self.stop=time.time()
		self.k=0
		self.process=PROCESS
		
	def capture(self, output_q):
		evt=threading.Event()
		im=pyscreenshot.grab(childprocess=False)
		output_q.put((im, evt))
		evt.wait()
	
	def save(self, k, input_q):
		s="./Screenshots/Screenshot"+str(k)+".png"
		data, evt=input_q.get()
		data.save(s)
		evt.set()
		
	def join(self, q):
		a, b=q.get()
		a.join()
		b.join()
		
	def scr(self, q):
		q1=Queue()
		p=threading.Thread(target=self.capture, args=(q1, ))
		o=threading.Thread(target=self.save, args=(self.k, q1))
		p.start()
		o.start()
		q.put((p,o))
		
	def begin(self):	
		while True:
			q2=Queue()
			m=threading.Thread(target=self.scr, args=(q2,))
			n=threading.Thread(target=self.join, args=(q2, ))
			m.start()
			n.start()
			m.join()
			n.join()
			self.stop=time.time()
			self.k+=1
			if int(self.stop-self.start)>int(self.r):
				break
				
obj=Screenshot(1)
obj.begin()
