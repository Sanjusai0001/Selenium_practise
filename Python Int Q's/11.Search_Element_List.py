
# How To Search an Element in a List

#   1

players = ["dhoni", "kohli", "rohit", "chahal", "sachin"]
dummy = "chahal"   # "pant"
centuries = 0
print(players)

for player in players:
    if (player == dummy):
        centuries = 10
        print("player found")
        break

if (centuries == 0 ):
    print("player not found")

#   2  (in)

if dummy in players:
    print('player is not a batsmen')

li = [2,3,4,14]
if 14 in li:
    print("yes")
else:
    print("no")