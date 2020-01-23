# Python - Podstawy i OOP
## Słowo wstępu
Udało nam przebrnąć przez sporą cześć zagadnień związanych z podstawami programowania w Pythonie oraz pewnych zagadnień związanych z programowaniem obiektowym w Pythonie.

## Zawartość
W repozytorium znajdziesz:
- Pakiet libs:
  - `FancyTextFile` - klasa do obsługi zapisu i odczytu plików tekstowych z mocno rozbudowanym przykładem settera dla ustawiania kodowania,
  - `FancyCryptoTextFile` - klasa rozszerzająca `FancyTextFile` o szyfrowanie i deszyfrowanie w locie,
  - `CryptoHelpers` - funkcje pomocnicze do szyforwania i deszyfrowania napisów.
- `MySimpleNotes` - przykład programu notatnika, wykorzystujący klasę `FancyTextFile`,
- `MyNotesFromUtfToIso` - przykład programu konwertujący notatki z uft-8 do iso-8859-2, wykorzystujący klasę `FancyTextFile`,
- `MyNotesFromIsoToUtf` - przykład programu konwertujący notatki z iso-8859-2 do uft-8, wykorzystujący klasę `FancyTextFile`,
- `MySimpleCryptoNotes` - przykład programu notatnika, wykorzystujący klasę `FancyCryptedTextFile` do zapisu zabezpieczonego pliku tekstowego,
- `crypto` - program CLI do szyforwania i deszyfrowania plików,
- `cryptoGui` - program GUI do szyforwania i deszyfrowania plików wykorzystujący funkcje z programu w wersji tekstowej.

## Na co zwrócić uwagę
#### `libs.FancyTextFile`
W klasie tej znajduje się nieco bardziej złożony `setter`. Ma on za zadanie kontrolowanie kodowania ( [UTF-8](https://pl.wikipedia.org/wiki/UTF-8) lub
[ISO_8859-2](https://pl.wikipedia.org/wiki/ISO_8859-2) ) jakie używane jest do zapisu i odczytu pliku. Ogólnie algorytm prezentuje się następująco:
1. Jeśli kodowanie zmieniane jest na takie jakie już jest, nie rób nic,
2. Jeśli kodowanie nie jest obsługiwane wygeneruj wyjątek,
3. Jeśli możliwe jest odczytanie zawartości z pliku to odczytaj ją i zapamiętaj,
4. Zmień kodowanie,
5. Zapisz stosując nowe kodowanie.

#### `libs.FancyCryptoTextFile`
Tu natomiast znajdziemy przykład dziedziczenia z nadpisywaniem metod. Metody nadpisane są w taki sposób, aby ich użycie przypominało metody rodzica tj. wywołanie ich jest takie samo. Dodatkowo metody używają logiki metod rodzica do zapisu i odczytu z respektowaniem obsługi kodowania.

#### `libs.CryptoHelpers`
Znajdziemy tu przykład bardzo prostych implementacji algorytmu szyfrującego znanego jako [Szyfr Vigenère’a](https://pl.wikipedia.org/wiki/Szyfr_Vigen%C3%A8re%E2%80%99a) (rozwinięcie szyfru Cezara). Z naszego punktu widzenia interesujące może być tu w jaki sposób wykonywana jest matematyka na literach i jak możliwe jest "przesuwanie liter".

#### `MySimpleNotes`
Przykładowe wykorzystanie klasy `libs.FancyTextFile` do stworzenia notatnika. Warto przeanalizować obsługę wyjątków przy wpisywaniu przez operatora treści i wykrywanie wciśnięca CTRL+C i CTRL+D.

#### `MyNotesFromUtfToIso` i `MyNotesFromIsoToUtf`
Użycie logiki setter'a dla `encoding` z `libs.FancyTextFile`

#### `MySimpleCryptedNotes`
Przykładowe wykorzystanie klasy `libs.FancyCryptoTextFile` oraz przeniesienie logiki `MySimpleNotes`

#### `crypto`
Program do szyforwania i deszyfrowania plików z użyciem `libs.FancyTextFile` i `libs.FancyCryptoTextFile` . Uruchomienie wymaga przekazanie parametrów do programu tj. np. tak:
```
$ python3 crypto.py -p haslo -i plik_wejsciowy.txt -o zakodowany.txt
```
lub odszyfrowanie:
```
$ python3 crypto.py -p haslo -d -i zakodowany.txt -o plik_odkodowany.txt
```
aby zobaczyć pomoc do obsługi:
```
$ python3 crypto.py -h
```
Warto zapoznać się z obsługą parsowania parametrów.

#### `cryptoGui`
Przy spełnieniu kilku warunków program konsolowy łatwo może stać się programem z graficznym interfejsem. Ten program importuje kluczowe funkcje z programu/modułu `crypto` i dodaje GUI.
