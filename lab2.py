import sys
from math import sqrt
#Zad 1. Napisz skrypt, w którym tworzysz listę ulubionych sportów, odwróć ją a następnie dodaj mniej lubiane sporty na sam koniec.
# lista = ['Smolarek', 'Lewandowski', 'Małysz']
# lista.reverse()
# print(lista)
# lista.append('siatkówka')
# lista.append('koszykówka')
# print(lista)

#Zad 2. Stwórz słownik skrótów powszechnie używanych w gazetach lub artykułach internetowych. Jako klucz przyjmij skrót danego słowa, wartość to rozwinięcie tego skrótu.
# slowa = {'cb': 'ciebie', 'itp': 'i tak dalej', 'cd': 'ciąg dalszy'}
# print(slowa)

#Zad 3. Stwórz słownik z ulubionymi grami komputerowymi. Pomyśl, co może być kluczem a co wartością w takim słowniku. Policz liczbę elementów w słowniku.
# gry = {'fps': 'cs:go', 'mmorpg': 'margonem', 'moba': 'League of Legends'}
# print(len(gry))

#Zad 4. Napisz skrypt, który pobiera od użytkownika zdanie i liczy wystąpienia litery a. Użyj funkcji input
# sl = input('podaj slowo: ')
# print('Liczba \'a\' w slowie \'{}\': {}'.format(sl, sl.count('a')))

#Zad 5. Napisz skrypt gdzie pobierzesz trzy liczby całkowite, gdzie wykonasz obliczenia: ab + c. Użyj instrukcji readline() i write()).
# sys.stdout.write('Podaj trzy liczby całkowite: ')
# a = sys.stdin.readline()
# b = sys.stdin.readline()
# c = sys.stdin.readline()
# w = int(a) * int(b) + int(c)
# sys.stdout.write('a * b + c = %s' % w)

#Zad 6. Wczytaj trzy liczby całkowite a,b,c i sprawdź, która z nich jest największa. W zależności od wyniku wyświetl odpowiedni komunikat. Użyj zagnieżdżeń.
# a = int(input('Podaj a: '))
# b = int(input('Podaj b: '))
# c = int(input('Podaj c: '))
#
# if a >= b:
#     if a >= c:
#         print('Największe: %d' % a)
#     else:
#         print('Największe: %d' % c)
# elif b >= c:
#     print('Największe: %d' % b)
# else:
#     print('Największe: %d' % c)

#Zad 7. Napisz skrypt, gdzie stworzysz listę składającą się z liczb typu int i float. Następnie za pomocą użycia pętli for podnieś każdą liczbę do kwadratu.
# lista_l = [1, 2, 4, 3.5, 3.66666666666, 7.67]
#
# for elem in lista_l:
#     print(elem * elem)

#Zad 8. Napisz skrypt, który za pomocą pętli while pobiera 10 liczb, następnie dodaje do listy tylko parzyste liczby.
# lista_parz = []
# i = 0
# while i < 10:
#     a = int(input('Podaj liczbę: '))
#     if a % 2 == 0:
#         lista_parz.append(a)
#     i += 1
# print(lista_parz)

#Zad 9. Napisz skrypt, który rysuje następującą literę

# EEEEEE
#
# E
#
# EEEEEE
#
# E
#
# EEEEEE
#
# Etapy wykonania ćwiczenia:
#
# Deklarujemy jedną następującą listę [1,2,3,4,5,6]. Następnie za pomocą pętli i instrukcji warunkowej wykonujemy odpowiednie działania. Trzeba wykorzystać zagnieżdżenia.
# l = [1, 2, 3, 4, 5, 6]
# test = True
# for i in range(1, 11):
#     if i % 2 == 1:
#         if test:
#             print('EEEEE')
#             test = False
#         else:
#             print('E')
#             test = True
#     else:
#         print('')

#Zad. 10 Napisz skrypt, który liczy pierwiastek z liczby podanej przez użytkownika jeśli użytkownik poda wartość ujemną to powinien być wyłapany błąd.
# try:
#     liczba = int(input('Podaj liczbe: '))
#     print(sqrt(liczba))
#
# except:
#     print(sys.exc_info()[0])
#     print('Tylko liczby nieujemne!')