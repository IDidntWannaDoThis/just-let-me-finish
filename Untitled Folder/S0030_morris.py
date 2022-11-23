"""
Exercise "Morris The Miner":

As always, read the whole exercise description carefully before your start to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

Initial situation:
Morris has the attributes: sleepiness, thirst, hunger, whisky, gold.
All attributes have the starting value 0.

Rules:
If sleepiness, thirst or hunger goes above 100, Morris the miner dies.
Morris can’t store more than 10 bottles of whisky.
No attribute may go below 0.

Possible moves for a turn:
sleep:      sleepiness-=10, thirst+=1,  hunger+=1,  whisky+=0, gold+=0
mine:       sleepiness+=5,  thirst+=5,  hunger+=5,  whisky+=0, gold+=5
eat:        sleepiness+=5,  thirst-=5,  hunger-=20, whisky+=0, gold-=2
buy_whisky: sleepiness+=5,  thirst+=1,  hunger+=1,  whisky+=1, gold-=1
drink:      sleepiness+=5,  thirst-=15, hunger-=1,  whisky-=1, gold+=0

Your task:
Write a program that gets Morris as much gold as possible in 1000 turns.

if you have no idea how to begin, open S0031_morris.py and start from there
if you get stuck, ask google, the other pupils or the teacher (in this order).

When your program is complete, push it to your GitHub repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""





def new_turn(stats):
    print(f"turn: {stats['turn']}.")
    print(f"you have {stats['energy']} energy.")
    print(f"you have {stats['wisky']} wisky, and you are {stats['hangover']}% drunk.")
    print(f"thirst: {stats['thirst']}")
    print(f"gold: {stats['gold']}")
    print(f"hunger: {stats['hunger']}")
    print()
    print("you can:")
    print("sleep")
    print("mine")
    print("eat")
    print("buy_whisky")
    print("drink")

    print("what will you do:")
    action = CP(stats)
    if action == "sleep":
        stats['energy'] += 10
        stats['thirst'] += 1
        stats['hunger'] += 1
        stats['gold'] = 0

        print("you had a good nights sleep")
    elif action == "mine":
        stats['energy'] -= 5
        stats['gold'] += 5
        stats['thirst'] += 5
        stats['hunger'] += 5
        print("you went mining and found some gold")
    elif action == "eat":
        if stats['gold'] >= 2:
            stats['energy'] -= 5
            stats['gold'] -= 2
            stats['hunger'] -= 20
            stats['thirst'] -= 5
            print("you ate some food")
        else:
            print("you don't have Enough gold")
    elif action == "buy_whisky":
        if stats['gold'] >= 1:
            stats['energy'] -= 5
            stats['gold'] -= 1
            stats['wisky'] += 1
            stats['thirst'] += 1
            print("you bought a bottle of whisky")
        else:
            print("you don't have Enough gold")

    elif action == "drink":

        if stats['wisky'] >= 1:
            stats['energy'] -= 5
            stats['wisky'] -= 1
            stats['thirst'] -= 15
            stats['hunger'] -= 1
            print("you drank a bottle of whisky")
        else:
            print("you don't have any whisky")
    else:
        return
    if stats['hunger'] < 0:
        stats['hunger'] = 0

    if stats['thirst'] < 0:
        stats['thirst'] = 0

    if not stats['hangover'] <= 0:
        stats['hangover'] = - 10
    stats['turn'] += 1
    return stats
def deathcheck(stats):
    if stats['thirst'] >= 100:
        print("you died of thirst")
        death = True
    elif stats['hunger'] >= 100:
        print("you died of starvation")
        death = True
    elif stats['hangover'] >= 100:
        print("you drank too much alcohal")
        death = True
    elif stats['energy'] <= 0:
        print("you died of exaustion")
        death = True
    else:
        death = False

    return death


def CP(stats):
    if stats['turn'] == 1000:
        return "mine"

    elif stats['wisky'] < 1 and stats['gold'] > 0:
        return "buy_whisky"
    elif stats['thirst'] > 70:
        if stats['hunger'] > 70 and stats['gold'] > 1:
            return "eat"
        elif stats['wisky'] >= 1:
            return "drink"
        else:
            return "mine"
    elif stats['hunger'] > 70 and stats['gold'] > 1:
        return "eat"
    elif stats['energy'] < 20:
        return "sleep"
    else:
        return "mine"

def life(stats):
    while stats['turn'] <= 1000 and not deathcheck(stats):
        stats = new_turn(stats)

    print(f"you died with {stats['gold']} gold")


life({"turn": 1,"energy":100, "thirst": 0, "wisky": 0, "gold": 0, "hunger":0 ,"hangover": 0,})