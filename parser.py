file = open('homework0.txt').readlines()

new_file = []

for i in range(3, len(file)):
    line = file[i].replace(' ', '').replace('\n', '')

    if len(file[i].split('|')) == 2:
        new_file.append((line + '|Broken|0').split('|'))
    elif len(file[i].split('|')) == 3:
        new_file.append((line + '|0').split('|'))
    else:
        new_file.append(line.split('|'))


len_file = len(new_file) - 1

def scounter(string):
    try:
        float(string[1].replace(',', '.'))
    except ValueError:
        dmg = 0
    else:
        dmg = float(string[1].replace(',', '.'))
    wep = string[2]
    output = 0
    try:
        int(string[3])
    except ValueError:
        buf = 0
    else:
        buf = int(string[3])

    if wep == 'Broken':
        output = dmg * 0.5 * (1 + 0.15 * buf)
    elif wep == 'Active':
        output = dmg * 1.5 * (1 + 0.15 * buf)

    return output

def nickname(string):
    if string[0].count(']') == 1:
        guild, name = string[0][1::].split(']')
        return guild, name
    else:
        return '0', string[0]


for j in range(len_file):
    print(f'Игрок {nickname(new_file[j])[1]} из гильдии {nickname(new_file[j])[0]} нанес {scounter(new_file[j])} по воротам')
    #print(new_file[j][0])

#print(new_file[3])
#print(len_file)