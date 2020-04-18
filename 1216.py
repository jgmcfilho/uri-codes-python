if __name__ == '__main__':
    distances = []
    while True:
        try:
            input()
            distances.append(float(input()))
        except:
            print(round(sum(distances)/len(distances), 1))
            break
