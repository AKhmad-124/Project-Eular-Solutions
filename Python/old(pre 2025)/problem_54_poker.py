file_of_hands = open("0054_poker.txt","r")

list_of_hands = file_of_hands.readlines()
clean_list = []
for i in list_of_hands :
    i = i.replace("C","")
    i = i.replace("H","")
    i = i.replace("S","")
    i = i.replace("D","")
    i = i.replace("\n","")
    i = i.replace(" ","")
    clean_list.append(i)

player_1_hand = []
player_2_hand = []


for i in clean_list:
 
    player_1_hand.append(i[0:5]) 
    
    player_2_hand.append(i[5:10])
    

list_of_cards = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]


def highest_card(hand):
    max_score =0

    for i in hand:
        if max_score < list_of_cards.index(i):
            max_score = list_of_cards.index(i)
    return max_score
win1 = 0
tie = 0
for i in range(1000):


    if highest_card(player_1_hand[i]) >  highest_card(player_2_hand[i]):
        win1 += 1

    if highest_card(player_1_hand[i]) == highest_card(player_2_hand[i]):
        tie  += 1

print(player_1_hand)



