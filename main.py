'''
read precatórios from text file
'''
import csv
import sys
import re

class Precatorio():
    def __init__(self, num):
        self.code = num
        self.value = -1
        self.description = ''
    
    def set_description(self, desc:str):
        self.description = desc
    
    def set_value(self, val:int):
        self.value = val

    def has_description(self):
        return self.description != '' and self.description is not None

    def __str__(self):
        return '[{}] {} (R$ {})'.format(
            self.code,
            self.description,
            self.value
        )

def is_precatorio(text:str):
    m = re.search('\d{20}', text)
    return m is not None

def is_money_value(text:str):
    m = re.search('[^\d\.]', text)
    return m is None

text_file = open(sys.argv[1], 'r', encoding='utf-8')
previous_line = ''
precatorios = []
valores = []
reading_values = False

silent = '-s' in sys.argv

for line in text_file:
    line = line.replace('\n', '')
    if line == '':
        continue
    if is_precatorio(line):
        # significa que temos o código do precatório, então
        # a linha anterior é a descrição dele
        p = Precatorio(line)
        precatorios.append(p)
    else:
        if precatorios and not reading_values and not precatorios[len(precatorios) - 1].has_description():
            precatorios[len(precatorios) - 1].set_description(line)
        
        if 'VALOR (R$)' in line:
            reading_values = True

        if is_money_value(line) and reading_values:
            valores.append(int(line.replace('.', '')))

if len(precatorios) == len(valores):
    with open(sys.argv[2], mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        for p, v in zip(precatorios, valores):
            p.set_value(v)
            if not silent:
                print(p)
            writer.writerow([p.code, p.description, p.value])
else:
    print('Lista de valores e lista de precatórios não batem.')
