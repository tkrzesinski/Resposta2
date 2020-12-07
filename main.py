# Imprimir para cada numero de 1 ate 100 em uma nova linha

for item in range(99):
    if (((item + 1) % 3) + (((item + 1) % 5)) == 0) and item > 0:
        print ((item + 1), "FooBaa")
    else:
        if (((item + 1) % 3) == 0):
            print ((item + 1), "Foo")
        else:
            if (((item + 1) % 5) == 0):
                print ((item + 1), "Baa")
            else:
                print ((item + 1))
