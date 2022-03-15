a = open('tester2.txt','w+')
a.write('hola mundo')
a.close()


lines = []
with open('tester2.txt') as file:
    for line in file:
        lines.append(line.rstrip())
print(lines)

for line in lines:
    if line[0].isdigit():
        i = int(line[0])
        if i % 2 == 0:
            print(line)


#archivo = open('tester.txt','r')
#print(archivo.read())