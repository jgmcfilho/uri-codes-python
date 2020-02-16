# problem:
# https://www.urionlinejudge.com.br/judge/en/problems/view/1367

while(True):
    number_of_submissions = int(input())
    line = ''
    problems_id = []
    time = 0
    corret_problems = 0
    if not number_of_submissions:
        break
    for i in range(number_of_submissions):
        line = input()        
        if line.split()[2] == 'incorrect':
            problems_id.append(line.split()[0])
        else:
            time += int(line.split()[1])
            corret_problems+=1
            for p_id in problems_id:
                if p_id == line.split()[0]:                            
                    time += 20
    print('{} {}'.format(corret_problems, time))