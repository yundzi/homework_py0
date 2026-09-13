import sys

def scounter(string):
    try:
        dmg = float(string[1].replace(',', '.'))
    except (ValueError, IndexError):
        dmg = 0
        
    # Защита от отсутствия элемента
    if len(string) > 2:
        wep = string[2]
    else:
        wep = 'Broken'
        
    output = 0
    try:
        buf = int(string[3])
    except (ValueError, IndexError):
        buf = 0

    if wep == 'Broken':
        output = dmg * 0.5 * (1 + 0.15 * buf)
    elif wep == 'Active':
        output = dmg * 1.5 * (1 + 0.15 * buf)

    return round(output, 2)

def nickname(string):
    # Защита от пустого списка или пустой строки
    s = string[0] if string else ''
    if not s or s[0] != '[':
        return '0', s
        
    if string[0].count(']') >= 1:
        guild, name = s[1:].split(']', 1)

        if name[0] == ']':
            return guild[1::], name[1::]
        else:
            return guild, name
    return '0', s

def main(path: str):
    new_file = []
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            file = f.readlines()
    except FileNotFoundError:
        print(f"Файл {path} не найден.")
        return

    for i in range(3, len(file)):
        line = file[i].replace(' ', '').replace('\n', '')

        if len(file[i].split('|')) == 2:
            new_file.append((line + '|Broken|0').split('|'))
        elif len(file[i].split('|')) == 3:
            new_file.append((line + '|0').split('|'))
        else:
            new_file.append(line.split('|'))

    len_file = len(new_file)

    for j in range(len_file):
        print(f'Игрок {nickname(new_file[j])[1]} из гильдии {nickname(new_file[j])[0]} нанес {scounter(new_file[j]):.2f} по воротам')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Ошибка: укажите путь к файлу лога.")
        print("Пример запуска: python3 siege.py siege_log.txt")