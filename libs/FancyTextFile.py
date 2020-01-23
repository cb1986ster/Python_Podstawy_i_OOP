'''
Klasa bazowa obsługująca operacje zapisu/odczytu z do pliku
'''
class FancyTextFile:
    '''
    Zmienna przechowująca nazwę pliku na którym operujemy zadeklarowana jako
    zmienna prywatna ponieważ po utworzeniu obiektu nie chcemy nagle zmienić
    w sposób przypadkowy(lub nie) na jakim pliku pracujemy.
    '''
    __file_name = None

    '''
    Zmienna przechowująca kodowanie pliku zmienna może sie zmienić, ale zawsze
    musi być poprawnym kodowaniem
    '''
    __encoding = None

    def __init__(self, file_name, encoding = 'utf-8'):
        '''
        Magiczna metoda którą poszukuje i uruchamia Python zaraz po utworzeniu
        obiektu, zwykle w celu ustawiania jakichś właściwości.
        Tutaj metoda wymaga podana nazwy pliku oraz opcjonalnie kodowania
        '''
        self.__file_name = file_name # Zapisanie nazwy pliku roboczoego
        self.encoding = encoding # Ustawienie kodowania

    def put_content(self, content):
        '''
        Funkcja zapisuje dane do pliku z zachowaniem odpowiedniego kodowania
        '''
        fp = open(self.__file_name,'wb') # Otwarcie pliku
        fp.write(str(content).encode(self.__encoding)) # Zapis do pliku
        fp.close() # Zamknięcie pliku
        return True # Zwrócenie informacji o poprawnym przebiegu zapisu

    def get_content(self):
        '''
        Funkcja odczytuje dane z pliku z zachowaniem odpowiedniego kodowania
        '''
        fp = open(self.__file_name,'rb') # Otwarcie pliku
        buffer = fp.read().decode(self.__encoding) # Odczytanie zawrtości
        fp.close() # Zamknięcie pliku
        return buffer # Zwrócenie odczytanej zawartości

    @property
    def encoding(self):
        '''
        Getter dla odczytywania kodowania
        '''
        return self.encoding

    @encoding.setter
    def encoding(self, encoding):
        '''
        Setter do zmiany kodowania - jego wywołanie skutkuje również zmianą
        zawartości pliku
        '''
        if self.__encoding != encoding: # Jeśli ustawiono tę samą warość to nic nie rób
            vaild_encodings = ('utf-8', 'iso-8859-2')
            if encoding in vaild_encodings:
                # Jeśli zadano poprawne kodowanie
                if self.__encoding == None:
                    # Jeśli jest to ustawienie pierwotne z __init__
                    self.__encoding = encoding
                else:
                    # Zmieniamy zawartość pliku
                    try:
                        # Odczytajmy obecną zawartość
                        data = self.get_content()
                    except FileNotFoundError as e:
                        # Jeśli plik nie istnieje wygenerowany zostanie wyjątek
                        data = None
                    # Zmieńmy kodowanie, ale zapamiętajmy obecne
                    old_encoding = self.__encoding
                    self.__encoding = encoding

                    if data != None:
                        # Jeśli mamy co zmieniać
                        try:
                            # Spróbujemy teraz zapisać zawartość z nowym kodowanie
                            self.put_content(data)
                        except Exception as e:
                            # Coś poszło nie tak, przywróćmy kodowanie
                            self.__encoding == old_encoding
                            # I zaznaczmy wyjątek
                            raise e
            else:
                raise ValueError('Encoding notsuppotred! Vaild values are:',', '.join(vaild_encodings))
