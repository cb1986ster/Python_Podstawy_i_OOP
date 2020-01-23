from libs.FancyTextFile import FancyTextFile

# Tworzymy obiekt notesu
notes_file = FancyTextFile('notes.txt','utf-8')

notes_file.encoding = 'iso-8859-2'
