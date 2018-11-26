import os,time
disk = os.getcwd()
def wirte_txt():
	print ('run')
	num = [a+'/'+n for a,b,c in os.walk(disk) for n in c]
	print (len(num))
	#with open(disk+'name.txt','a') as f:
	#	for i in num:
	#		f.write(i+'\n')
	return num
def main(num):
	chuan = list(set([a+'/'+n for a,b,c in os.walk(disk) for n in c]) - set(num))
	if chuan:
		for i in chuan:
			print ('rename    --'+i)
			rena = i.replace('.','x')
			os.rename(i,rena)
			num.append(rena)
	else:
		print ('no updata!')
txt = wirte_txt()
while True:
	main(txt)
	time.sleep(3)



