import random

def gen_code(length=8):
	"""
	将0~9,a~z,A~Z保存到list中，用random.sample从list中取固定位数
	"""
	code_list = []
	for i in range(10):
		code_list.append(str(i))
		#print i
	for i in range(65, 91):
		code_list.append(chr(i))
		#print chr(i)
	for i in range(97, 123):
		code_list.append(chr(i))
 
	myslice = random.sample(code_list, length)
	veri_code = ''.join(myslice)
	print (veri_code)
	return myslice

if __name__ == '__main__':
	for i in range(200):
		gen_code(length=8)