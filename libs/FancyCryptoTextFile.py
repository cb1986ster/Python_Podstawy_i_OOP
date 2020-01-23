from .FancyTextFile import FancyTextFile
from .CryptoHelpers import simple_decoder,simple_encoder
'''
Klasa obsługująca operacje zapisu/odczytu do/z pliku z szyfrowaniem w locie
'''
class FancyCryptoTextFile(FancyTextFile):
    '''
    Zmienna do przchowywania klucza szyfrowania
    '''
    __password = None

    def __init__(self, file_name, password, encoding = 'utf-8'):
        super(FancyCryptoTextFile,self).__init__(file_name, encoding)
        self.__password = password

    def put_content(self, content):
        '''
        Funkcja zapisuje dane do pliku z szyfrowaniem
        '''
        encrypted = simple_encoder(content,self.__password)
        return super(FancyCryptoTextFile,self).put_content(encrypted)

    def get_content(self):
        '''
        Funkcja odczytuje dane z pliku z deszyfrowaniem
        '''
        encrypted = super(FancyCryptoTextFile,self).get_content()
        return simple_decoder(encrypted,self.__password)
