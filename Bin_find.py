def bin_finder(list, item):
    # бинарный aлгоритм по поиску в списке сокращает число проверок с О(n) до O(log n)

    low = 0 
    high = len(list) - 1 
        
    while low <= high:
        mid = (low + high) // 2    # питон округлит до меньшего 
        guess = list[mid]      
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1   # если число загаданное больше, то сужаем предел поиска от середины к концу
        else: 
            high = mid - 1  # если число загаданное меньше, то сужаем предел поиска от начала к середине
    return None

mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]
print(bin_finder(mylist, 19))    # вызов функции выводит индекс числа, найденый алгоритмом бинарного поиска
