lines = []
with open('tester.txt') as file:
    for line in file:
        lines.append(line.rstrip())

for line in lines:
    i = int(line[0])
    if i % 2 == 0:
        print(line)

print(lines)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
archivo = open('tester.txt', 'r')
print(archivo.read())
