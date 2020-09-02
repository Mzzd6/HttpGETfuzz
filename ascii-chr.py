import sys

#use : py ascii-chr.py filename
filename = sys.argv[1]
str_list = []

for i in open(filename):
	str_list.append(i)

print('长度：%d' %len(str_list))


def ascii_chr():

	for i in str_list:
		i = i.replace('\n','')
		i = chr(int(i))
		print(i,end='')


def chr_ascii():
	for i in str_list:
		i = i.replace('\n','')
		print(i,end=' ')
	print('')
	for i in str_list:
		i = i.replace('\n','')
		j = ord(i)
		print(j,end=' ')


if __name__ == '__main__':

	while 1:
		show=r'''
			请选择
			1.ascii转字符
			2.字符转ascii

		'''
		print(show)
		i = int(input('请输入'))
		if i == 1:
			ascii_chr()
			break
		elif i == 2:
			chr_ascii()
			break
		else:
			print('输入有误')

