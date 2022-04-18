import numpy as np

def random_pridict(number:int=1) -> int:
    number = np.random.randint(1, 101) #загадываем число

    count = 0

    random_number = 32

    step = 32

    while True:
    
        count += 1
    
        if number > random_number:
            random_number+=step
        
        elif number < random_number:
            step /= 2
            random_number-=step
    
        else:
            break
        
    return(count)

def score_game(random_pridict) -> int:
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for num in random_array:
        count_ls.append(random_pridict(num))
    
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм в среднем угадывает число за : {score} попыток')
    return(score)

score_game(random_pridict)



#print(f'Количество попыток : {random_pridict(10)}')