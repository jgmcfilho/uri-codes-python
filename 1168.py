# problem:
# https://www.urionlinejudge.com.br/judge/en/problems/view/1168

leds = {'1':2, '2':5, '3':5,
        '4':4, '5':5, '6':6,
        '7':3, '8':7, '9':6,
        '0':6}

for i in range(int(input())):
    number = input()
    leds_sum = 0
    for digit in number:
        leds_sum+=leds[digit]
    print('{} leds'.format(leds_sum))