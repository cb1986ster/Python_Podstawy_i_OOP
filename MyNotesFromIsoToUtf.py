from libs.FancyTextFile import FancyTextFile

# Tworzymy obiekt notesu
notes_file = FancyTextFile('notes.txt','iso-8859-2')

notes_file.encoding = 'utf-8'
