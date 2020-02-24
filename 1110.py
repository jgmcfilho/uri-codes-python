def perform_op(cards):
    discarded = []
    while len(cards) > 0:
        if len(cards) == 1:
            last = cards.pop()
            continue        
        discarded.append(cards.pop(0))
        cards += [cards.pop(0)]
    # Returning a tuple    
    return ', '.join([str(card) for card in discarded]), last

            
if __name__ == '__main__':
    
    while True:
        cards = []
        number_of_cards = int(input())
        if number_of_cards == 0:
            break
        for i in range(number_of_cards):
            cards.append(i+1)
        result = perform_op(cards)         
        print('Discarded cards: {}'.format(result[0]))
        print('Remaining card: {}'.format(result[1]))