import time
#from kuttyPy import *
setReg('DDRD',255)

ca = [128+64,64+32+16,16+8+4,19,19,16+8+4,16+32+64,128+64]
ct = [1,1,1,255,255,1,1,1]
cj = [128+64+1,128+1,128+1,128+1,255,1,1,1]
ci= [0,0,129,255,255,129,0,0]
ch=[255,255,24,24,24,24,255,255]
cn=[255,3,14,24,16+32,64+32,64+128,255]
cv=[1+2,2+4+8,16+8+4,19,19,16+8+4,2+4+8,1+64]

while 1:
	for a in [cj,ci,ct,ch,ci,cn]: 
		for b in a:
			setReg('PORTB', b)
			time.sleep(0.001)
		time.sleep(0.008)
	time.sleep(0.01)

