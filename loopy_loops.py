if __name__ == '__main__':

    pokemon = ('picachu','charmander','bulbasaur')
    print(pokemon[1])
    starter1 = pokemon[0]
    starter2 = pokemon[1]
    starter3 = pokemon[2]
    print(starter1)
    print(starter2)
    print(starter3)

    name = tuple('Mike')
    print(name)

    print('i' in name)
    for i in range(2, 11):
        print(i)

    current_value = 2
    while current_value < 11:
        print(current_value)
        current_value += 1
    
    simple_string = 'This is a simple string'
    split_string = tuple(simple_string)
    print(split_string)
    for i in split_string:
        print(i)

    original_string = ('this', 'is', 'a', 'simple', 'set')
    for i in original_string:
        for j in original_string[0:3]:
            print(i)