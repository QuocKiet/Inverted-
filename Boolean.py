
import re
import os


path_doc ='Docs'
path_data = './Data'
file_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(file_path,path_doc)
print(file_path)
allfiles = os.listdir(path_doc)
all_words = []
inverted_index = {}
for i in allfiles:
	filename = os.path.join(file_path,i)
	file = open(filename,'r')
	text = file.read().lower()
	file.close()

	non_words = re.compile(r"[^A-Za-z0-9]+")
	text = re.sub(non_words, ' ',text)
	words = list(text.split())
	for key in words:
		all_words.append(key)
		if inverted_index.get(key, None) is None:
			inverted_index[key] = {filename}
		else:
			inverted_index[key].add(filename)


dic_file = os.path.join(path_data, 'dictionary.txt')
inverted_index_file = os.path.join(path_data,'inverted_index.pickle')

with open(dic_file , 'w') as f:
	for word in inverted_index.keys():
		f.write(word + '\n')



loop = True

while loop:
	check = input("Nhap: exit() de thoat\nNhap tu can tim kiem: ")
	if check == 'exit()':
		break
	check.lower()
	if inverted_index.get(check, None) is None:
		print("khong co tu can tim\n")
	else:
		for i in inverted_index.get(check):
			print( i + "\n")



