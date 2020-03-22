

if __name__ == '__main__':
    while True:
        swaps_count = 0
        initial_line = input()
        if initial_line.split()[0] == initial_line.split()[1] == '0':
            break
        cards_a = list(dict.fromkeys(input().split()))
        cards_b = list(dict.fromkeys(input().split()))
        if len(cards_a) <= len(cards_b):
            for card in cards_a:
                if not card in cards_b:
                    swaps_count += 1
        else:
            for card in cards_b:
                if not card in cards_a:
                    swaps_count += 1
        print(swaps_count)   

# 22 20
# 1 1 3 3 5 6 8 8 10 11 13 15 17 17 19 20 20 22 22 24 24 25
# 2 3 4 6 7 7 8 10 11 13 14 15 17 17 18 19 21 23 25 27