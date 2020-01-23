# Importujemy naszą bibliotekę obsługi plików
from libs.FancyCryptoTextFile import FancyCryptoTextFile

haslo = input('Podaj hasło> ')
# Tworzymy obiekt notesu
notes_file = FancyCryptoTextFile('crypted_notes.txt', haslo)

try:
    # Odczyt danych
    data_in_notest = notes_file.get_content()

    print('In Your notes:')
    # enumerate(kolekcja) - zwraca pary [numer], [element_z_kolekcji]
    # pozwala to na pozyskanie elementu ale i jego numeru W kolekcji
    # Aby odczytać te elemenenty należy w forze podać po przecinku dodatkową
    # zmienną(tak naprawdę jest to rozłżenie krotki ;) )
    for line_no, line in enumerate(data_in_notest.splitlines()):
        print('{: 3}>'.format(line_no + 1), line)

except FileNotFoundError as e:
    # Jeśli plik nie istnieje to spokojnie możemy poinformaować użytkownika
    print('Your notes in empty!')

# Teraz odczytajmy nową zawartość
new_content = '' # bufor danych
print('Give Your content. To finish press CTRL+C on empty line')
line_no = 1 # Numer linijki
try:
    while True:
        line = input('{: 3}>'.format(line_no))
        line_no += 1
        new_content += line + "\n"
except KeyboardInterrupt as e:
    # wyjątek `KeyboardInterrupt` oznacza wciśnięcie CTRL+C
    pass
except EOFError as e:
    # wyjątek `EOFError` oznacza tu wciśnięcie CTRL+D
    pass

notes_file.put_content(new_content)
