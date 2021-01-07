import base64
import re
import hashlib

pass_txt = sys.argv[1]
passlist=[]


for i in open(pass_txt):
	i=i.replace('\n','')
	baselist.append(i)

#base64  encode
def basecode():
	t=open('base_return.txt','w')
	for i in passlist:
		base=str(base64.b64encode(i.encode("utf-8")),"utf-8")
		t.write('%s\n' %base)
	print('ok')
	t.close()


#小写转大写
def azcode():
	t=open('azAZ_return.txt','w')
	for i in passlist:
		i=i.upper()
		t.write('%s\n' %i)
	print('ok')
	t.close()


#大写转小写
def AZcode():
	t=open('AZaz_return.txt','w')
	for i in passlist:
		i=i.lower()
		t.write('%s\n' %i)
	print('ok')
	t.close()

#md5
def md5code():
	t=open('md5pass.txt','w')
	md5pay=hashlib.md5() 
	for i in passlist:
		md5pay.update(i.encode("utf8"))
		i=md5pay.hexdigest()
		t.write('%s\n' %i)
	print('ok')
	t.close()	

if __name__ == '__main__':
	while 1:
		
		show = '''
		1.base
		2.小写转大写
		3.大写转小写
		4.32位md5
		'''
		print(show + '\n')
		cho = int(input('输入：'))
		if cho == 1:
			basecode()
			break
		elif cho == 2:
			azcode()
			break
		elif cho == 3:
			AZcode()
			break
		elif cho == 4:
			md5code()
		else:
			print('输入无效')