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
            info = []
            while True:
                line = input()
                if line:
                    info.append(line)
                else:
                    break
            updateHands(hands, info)

            # write hands
            with open('hands.json', 'w') as file:
                file.write(json.dumps(hands))
        except IOError:
            firstTimeSetup()
        except KeyboardInterrupt:
            print()
            running = False


def printHUD(hands):
    # get players
    players = {}
    for hand in hands:
        for line in hand[1:-1]:
            if not (isHandStart(line) or isHandEnd(line) or line[:5] == "board"):
                username = line.split(' ')[0]
                if username not in players.keys():
                    players[username] = {'hands': 0, 'VPIP': 0, 'PFR': 0}

    # go thru hands
    for hand in hands:
        handUsers = []
        handVPIP = []
        handPFR = []
        for line in hand:
            if line[:5] == "board":
                break
            elif isHandStart(line) or isHandEnd(line):
                pass
            else:
                username = line.split(' ')[0]
                if username not in handUsers:
                    handUsers.append(username)
                action = line.split(' ')[1]
                if action == "called":
                    if username not in handVPIP:
                        handVPIP.append(username)
                elif action == "bet" or action == "raised":
                    if username not in handVPIP:
                        handVPIP.append(username)
                    if username not in handPFR:
                        handPFR.append(username)

        # update stats
        for username in handUsers:
            players[username]['hands'] += 1
        for username in handVPIP:
            players[username]['VPIP'] += 1
        for username in handPFR:
            players[username]['PFR'] += 1

    for player in players.keys():
        print(f"{ player }: ({ players[player]['hands'] }) { int(players[player]['VPIP'] / players[player]['hands'] * 100) } / { int(players[player]['PFR'] / players[player]['hands'] * 100) }")


def updateHands(hands, info):
    if len(info) >= 2:
        if isHandStart(info[0]) and isHandEnd(info[-1]):
            for line in info:
                if isHandStart(line):
                    hands.append([line])
                else:
                    hands[-1].append(line)


def isHandStart(line):
    if line[-23:] == "players are in the hand":
        return True
    return False


def isHandEnd(line):
    if line[-5:] == "chips":
        return True
    return False


def firstTimeSetup():
    print('performing first time setup')
    with open('hands.json', 'w') as file:
        file.write(json.dumps([]))
    

main()
