def minion_game(string):
    glas = 'AEIOU'
    Kevin = 0
    Stuart = 0
    for i in range(len(string)):
        if string[i] in glas:
            Kevin += len(string)-i
        else: 
            Stuart += len(string)-i
    if Kevin>Stuart:
        print("Kevin {}".format(Kevin))
    elif Stuart>Kevin:
        print("Stuart {}".format(Stuart))
    else:
        print("Draw")
