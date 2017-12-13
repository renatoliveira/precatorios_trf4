# from bs4 import BeautifulSoup
import sys
import re

class Precatorio():
    def __init__(self, document_code):
        self.document_code = document_code # código do documento
        self.parent_document = None # documento originário
        self.notice_date = None # data de autuação
        self.reporter_name = None # relator
        self.judicial_body_name = None # órgão julgador
        self.situation = None # situação
        self.cause_value = None # valor da causa
        self.competence = None # competência
        self.applicant = None # requerente
        self.deprecating = None # deprecante
        self.required_person = None # requerido
        self.persons = [] # nome de pessoas envolvidas (advogados e procuradores, por ex.)
        self.activities = []

    def __str__(self):
        return '''Documento: {}
Documento de origem: {}
Situação: {}
Data de autuação: {}
Relator: {}
Órgão Julgador: {}
Valor da causa: R$ {}
Competência: {}
Requerente: {}
Deprecante: {}
Requerido: {}
Envolvidos: \n{}
Atividades: \n{}
        '''.format(
            self.document_code,
            self.parent_document,
            self.situation,
            self.notice_date,
            self.reporter_name,
            self.judicial_body_name,
            self.cause_value,
            self.competence,
            self.applicant,
            self.deprecating,
            self.required_person,
            ''.join(['- ' + p + '\n' for p in self.persons]),
            ''.join([a + '\n' for a in self.activities])
        )

html_file = open(sys.argv[1], 'r')
lines = html_file.readlines()
lines = ''.join(lines)
document = Precatorio(sys.argv[1])
involved_persons_retrieved = False
for el in lines.split('<br>'):
    if 'Precatório Nº ' in el:
        document.document_code = el.split(' ')[2].replace('.', '').replace('-', '')
    if 'Originário: ' in el:
        document.parent_document = el.split(' ')[5].replace('.', '').replace('-', '')
    if 'Situação: ' in el:
        document.situation = el.split('>')[-1]
    if 'Data de autuação: ' in el:
        document.notice_date = el.split('>')[-1]
    if 'Relator: ' in el:
        document.reporter_name = el.split('>')[-1]
    if 'Órgão Julgador: ' in el:
        document.judicial_body_name = el.split('>')[-1]
    if 'Valor da causa:' in el:
        document.cause_value = el.split('>')[-1]
    if 'Competência:' in el:
        document.competence = el.split('>')[-1]
    if 'REQUERENTE: ' in el:
        m = re.search('>.{1,}<', el)
        if m:
            document.applicant = m.group(0)[1:len(m.group(0))-1]
    if 'DEPRECANTE: ' in el:
        m = re.search('>.{1,}<', el)
        if m:
            document.deprecating = m.group(0)[1:len(m.group(0))-1]
    if 'REQUERIDO: ' in el:
        m = re.search('>.{1,}<', el)
        if m:
            document.required_person = m.group(0)[1:len(m.group(0))-1]
    if 'Nome: ' in el:
        person = el.split('>')[-1]
        document.persons.append(person)
        involved_persons_retrieved = True
    elif involved_persons_retrieved:
        m = re.search('(\\d{2}\\/){2}\\d{4} \\d{1,}:\\d{1,}', el)
        if m:
            activity = el.split('  ')
            date_time = m.group(0)
            description = activity[1].replace('- ', '')
            document.activities.append(date_time + ' ===> ' + description)

print(document)
