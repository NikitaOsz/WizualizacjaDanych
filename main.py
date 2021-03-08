import math
# Zad1. Napisz pierwszy skrypt, w którym zadeklarujesz po dwie zmienne każdego typu a następnie wyświetl te zmienne
# a, b = 1, 2
# print(a, b)
# s1, s2 = 'ala', 'kot'
# print(s1, s2)
# f1, f2 = 0.5, 0.2
# print(f1, f2)
# c1, c2 = 1 + 2j, 3 + 5j
# print(c1, c2)

# Zad2. Stwórz skrypt kalkulator, w którym wykorzystać wszystkie podstawowe działania arytmetyczne
# def dodawanie(a, b):
#     return a + b
#
#
# def odejmowanie(a, b):
#     return a - b
#
#
# def mnozenie(a, b):
#     return a * b
#
#
# def dzielenie(a, b):
#     return a / b
#
#
# def potegowanie(a, b):
#     return a**b
#
#
# def pierwiastkowanie(a):
#     return math.sqrt(a)
#
#
# def menu():
#     a, b, wybor = 0, 0, 0
#     print('KALKULATOR')
#     print('-------------------')
#     print('1 - dodawanie')
#     print('2 - odejmowanie')
#     print('3 - mnozenie')
#     print('4 - dzielenie')
#     print('5 - potegowanie')
#     print('6 - pierwiastkowanie')
#     print('wybierz opcje wpisujac dana cyfre: ')
#     wybor = int(input())
#     if wybor == 6:
#         print('Podaj liczbe do pierwiastkowania: ')
#         a = int(input())
#         print(pierwiastkowanie(a))
#     else:
#         print('Podaj dwie liczby do policzenia: ')
#         a = int(input())
#         b = int(input())
#         if wybor == 1:
#             print(dodawanie(a, b))
#         elif wybor == 2:
#             print(odejmowanie(a, b))
#         elif wybor == 3:
#             print(mnozenie(a, b))
#         elif wybor == 4:
#             print(dzielenie(a, b))
#         elif wybor == 5:
#             print(potegowanie(a, b))
#
#
# menu()


#Zad3. Napisz skrypt, w którym stworzysz operatory przyrostkowe dla operacji: +, -, *, /, **, %
# a, b, c, d, e, f = 1, 2, 3, 4, 5, 6
# a += 1
# print(a)
# b -= 2
# print(b)
# c *= b
# print(c)
# d /= a
# print(d)
# e **= 1
# print(e)
# f %= 13
# print(f)

#Zad4. Napisz skrypt, który policzy i wyświetli następujące wyrażenia:
#print(math.exp(10))
# print(math.floor(3.55))
# print(math.ceil(4.80))
# result = (math.log(5 + (math.sin(8) ** 2))) ** 1 / 6
# print(result)
#Zad.5 Zapisz swoje imie i nazwisko w oddzielnych zmiennych wszystkie wielkimi literami. Użyj odpowiedniej metody by wyświetlić je pisane tak, że pierwsza litera jest wielka a pozostałe małe. (trzeba użyć metody capitalize)
# imie = 'NIKITA'
# nazwisko = 'OSZEJKO'
#
# print(imie.capitalize(), nazwisko.capitalize())


#Zad.6 Napisz skrypt, gdzie w zmiennej string zapiszesz fragment tekstu piosenki z powtarzającymi się słowami np. „la la la”. Następnie użyj odpowiedniej funkcji, która zliczy występowanie słowa „la”. (trzeba użyć metody count)
# string = 'bajojajobajojajo bajojajobajojajo'
# print(string.count('jo'))

#Zad.7 Do poszczególnych elementów łańcucha możemy się odwoływać przez podanie indeksu. Np. pierwszy znak zapisany w zmiennej imie uzyskamy przez imie[0]. Zapisz dowolną zmienną łańcuchową i wyświetl jej drugą i ostatnią literę, wykorzystując indeksy.
# wyraz = 'siema'
# print(wyraz[1], wyraz[len(wyraz) - 1])

#Zad.8 Zmienne łańcuchowe możemy dzielić wykorzystaj zmienną z Zad. 6 i spróbuj ją podzielić na poszczególne wyrazy. (trzeba użyć metody split)
# string = string = 'bajojajobajojajo bajojajobajojajo'
# print(string.split(' '))

#Zad.9 Napisz skrypt, w którym zadeklarujesz zmienne typu: string, float i szestnastkowe. Następnie wyświetl je wykorzystując odpowiednie formatowanie.
# s1, s2 = 'ala', 'kot'
# print('liczba s1 %s, liczba s2 %s' % (s1, s2))
# f1, f2 = 0.5, 0.2
# print('liczba f1 %f, liczba f2 %f' % (f1, f2))
# h1, h2 = 1, 2
# print('liczba h1 %#x liczba h2 %#x' % (h1, h2))
