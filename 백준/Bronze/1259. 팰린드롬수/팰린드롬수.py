while True:
    try:
        number = input()
        if number[0] != "0":
            test = 0
            for i in range(len(number)):
                if number[i] == number[len(number)-i-1]:
                    test += 1
                    
            if test == len(number):
                print("yes")

            else:   
                print("no")

    except:
        break