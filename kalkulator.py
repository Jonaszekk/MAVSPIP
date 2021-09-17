print("Witaj w Kalkulatorze")
print("| 1 - dodawanie | 2 - odejmowanie | 3 - mnożenie | 4 - dzielenie | 5 - potęgowanie | ")
wyb=int(input("Wybierz co chcesz obliczyć: "))

if wyb==1:
    a=int(input("Podaj Liczbę A: "))
    b=int(input("Podaj liczbę B: "))
    c=a+b
    print("Wynik: ", c )
elif wyb==2:
    a=int(input("Podaj Liczbę A: "))
    b=int(input("Podaj liczbę B: "))
    c=a-b
    print("Wynik: ", c )
elif wyb==3:
    a=int(input("Podaj Liczbę A: "))
    b=int(input("Podaj liczbę B: "))
    c=a*b
    print("Wynik: ", c )
elif wyb==4:
    a=int(input("Podaj Liczbę A: "))
    b=int(input("Podaj liczbę B: "))
    c=a/b
    print("Wynik: ", c )
elif wyb==5:
    a=int(input("Podaj Liczbę A: "))
    b=int(input("Podaj liczbę B: "))
    c=a**b
    print("Wynik: ", c )
else:
    print("Podano złe wartości")


# ** = potęgowanie 
    