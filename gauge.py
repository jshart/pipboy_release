import random


def moveGauge(state):
    flip=random.randrange(-1,2)
    #print(flip)
    state+=flip
    if (state<0):
        state=0
    if (state>3):
        state=3
    return(state)

def testApp():
    state=0
    for x in range(200):
        state=moveGauge(state)
        print("#"*state)
