import json


def main():
    # main loop
    actionQueue = []
    running = True
    while running:
        try:
            # get hands
            with open('hands.json', 'r') as file:
                hands = json.loads(file.read())

            # print hud info
            printHUD(hands)

            # wait for new info paste
            updateHands(hands, actionQueue, input(''))

            # write hands
            with open('hands.json', 'w') as file:
                file.write(json.dumps(hands))
        except IOError:
            firstTimeSetup()
        except KeyboardInterrupt:
            print()
            running = False


def printHUD(hands):
    pass


def updateHands(hands, actionQueue, info):
    if info != "":
        isHS = isHandStart(info)
        isHE = isHandEnd(info)
        
        actionQueue.append(info)


def isHandStart(info):
    re


def firstTimeSetup():
    print('performing first time setup')
    with open('hands.json', 'w') as file:
        file.write(json.dumps([]))
    

main()
