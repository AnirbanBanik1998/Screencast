import pyscreenshot 
import time
k=0
i=0
n=input("Enter Time: ")
type(n)
start=time.time()
if __name__=="__main__":
	
	while i<=int(n):
		im=pyscreenshot.grab()
		s="./Screenshots/Screenshot"+str(k)+".png"
		im.save(s)
		k=k+1
		i=time.time()-start
print(str(time.time()-start))
