if __name__ == '__main__':

    food = ['rice','beans']
    food.append('broccoli')
    food.extend(['bread','pizza'])
    print(food[0:2])
    print(food[4])
    
    ingredients = "eggs,fruit,orange juice"
    breakfast = ingredients.split(',')
    print(breakfast)
    print(len(breakfast))
    
    request = ''
    floating_point_values = []
    while not request == 'stop':
        print('enter a floating point value.')
        value = float(input())
        floating_point_values.append(value)
        print('great! now type "stop" if you want to stop, or else hit "enter" to continue.')
        request = input()
    print(f'average: {sum(floating_point_values) / len(floating_point_values)}')
    print(f'min: {min(floating_point_values)}')
    print(f'max: {max(floating_point_values)}')
