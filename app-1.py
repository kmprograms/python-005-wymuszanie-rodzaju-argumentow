# Umieszczenie znaku / po nazwie zmiennej x oznacza ze x jest
# POSITIONAL ONLY ARGUMENT
# Argument y moze byc przekazywany zarowno z jego nazwa jak i poprzez
# pozycje

# Tego rodzaju zabieg moze sie przydac kiedy zalezy nam na przekazywaniu argumentow
# w odpowiedniej kolejnosci lub kiedy trudno jest nadac "dobra" nazwe dla argumentu
# Kolejna zaleta to dzieki temu ze zabraniamy przekazywac argument z nazwa pozniej kiedy
# chcemy zmienic nazwe argumentu nie ma koniecznosci zmiany w innych miejscach w kodzie.
def add_values(x, /, y=0):
    return x + y


# W kolejnym przykladzie pokazemy jak mozemy dodatkowo definiowac jeszcze keyword-only
# arguments stosujac znak *
def add_values_2(x, /, y=0, *, z=0):
    return x + y + z


def positional_only_arguments():
    # realizowane jest za pomoca /
    print(f'1 ---> {add_values(10)}')
    print(f'2 ---> {add_values(10, 20)}')
    print(f'3 ---> {add_values(10, y=20)}')
    # print(f'4 ---> {add_values(x = 10, y = 20)}')  # blad

    print(f'4 ---> {add_values_2(10)}')
    print(f'5 ---> {add_values_2(10, 20, z=30)}')
    print(f'6 ---> {add_values_2(10, y=20, z=30)}')
    # print(f'4 ---> {add_values_2(x = 10, y = 20, z=30)}')


if __name__ == '__main__':
    positional_only_arguments()
