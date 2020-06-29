'''
f3.txt()
id,name,gen
101,phani,M
102,Raji,F
103,Prasad,M


f4.txt()
id,gen,name
104,F,Lakshmi
105,M,Pramod
106,M,Krishna
'''

f1 = open('f3.txt', 'r')
file1_content = f1.readlines()

f2 = open('f4.txt', 'r')
h1 = f2.readline()
file2_content = f2.readlines()
print(file2_content)

file2_new = []

for line in file2_content:
    words = line.split(',')
    id = words[0]
    gen = words[1]
    name = words[2].split('\n')[0]
    rec = id + ',' + name + ',' + gen + '\n'
    file2_new.append(rec)
file3_content = file1_content + ['\n'] + file2_new


f = open('file_new.txt', 'w')
for line in file3_content:
    f.write(line)

f.close()
f2.close()
f1.close()
