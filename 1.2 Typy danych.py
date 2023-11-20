print("Tomek")  # wypisuje dane

print(type("Tomek"))  # typ sprawdzenie danych
# ctr alt l formatuej ko wg zasad PEP8
# typowanie dynamiczne
# zmienna - pudełko na danie
wiek = 39
print(type(wiek))  #liczba całkowita
print("13" + "23")  ##konkatenacja
##print(13 + "23") ## nie działą różne stringi
# ctrl / szybkie komentowaine
print(int("13") + int("23")) ## nie działą różne stringi
print(5 * "Tomek")
print(0.1 + 0.7)
print(0.1 + 0.2)
# zapamiętywanie w postaci wykładniczej n*2^x
# z tego wynika błąd zaokrąglania floaty mają ograniczenie int nie mają zależą od pamięci / pieniądze liczymy decimal - wolniejszy.
# "" i '' możemy używać co chcemy ale konsekwetnie.
print(12, 13)
print(12, 13, sep=';')
print(12, 13, end='')
imie = "Tmek"
print("Twoje imie t %s"  % 39.7)
# print("Twoja liczba %d % imie)
print("Twoje imie  {}".format(imie))
#print("Sprawdzam zmienna temp i wiek {} {}").format(temp, wiek)
temp = 36.6
print(f"Sprawzdam zmienną temp {temp} i wiek {wiek}" )
print(f"\tZmienna temp {temp} \nwiek {wiek}")
print(imie[2]) #- są nie mutowalne bo to string który jest poindeksowany
#imie[2] ="T"
print(id(imie))  # podaje adres pamięci

