import time


# def execute_swap(cards, number_of_cards):    
#     number_of_cards = int(number_of_cards/2)
#     cards = cards.split(',')
#     string = ''
#     for i in range(number_of_cards):
#         string+=str(cards[i+number_of_cards])+','+str(cards[i])+','        
#     return string[:len(string)-1]


# if __name__ == '__main__':
#     original_cards = ''
#     number_of_cards = int(input())    
#     for i in range(number_of_cards):
#         original_cards+=str(i+1)+','
#     original_cards=original_cards[:len(original_cards)-1]
#     aux = original_cards
#     counter = 1
#     # print(execute_swap(original_cards, number_of_cards))
#     while True:        
#         aux = execute_swap(aux, number_of_cards)
#         if original_cards[:2] == aux[:2]:
#             break
#         counter+=1        
#     print(counter)



def execute_swap(cards):
    _cards = []
    number_of_cards = int(len(cards)/2) 
    for i in range(number_of_cards):
        _cards.append(cards[i+number_of_cards])
        _cards.append(cards[i])
    return _cards

if __name__ == '__main__':
    original_cards = []        
    counter = 0    
    [original_cards.append(i+1) for i in range(int(input()))]    
    while True:
        counter+=1
        original_cards = execute_swap(original_cards)
        if original_cards[0] == 1:
            break        
    print(counter)