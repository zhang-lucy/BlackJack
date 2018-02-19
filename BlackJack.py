from random import *
class Deck:
    deck=[] #empty deck, to be initialized
    hasCard=[] #list of booleans, indicates if associated card is in deck
    values=["Ace","King","2","3","4","5","6","7","8","9","10","Jack","Queen"]
    suits=["Spades","Hearts","Diamonds","Clubs"]
    def __init__(self):
        for suit in Deck.suits:
            for value in Deck.values:
                card=value+" of "+suit
                Deck.deck.append(card)

        for x in range(52):
            Deck.hasCard.append(True)
            
    def print(self):
        for x in range(52):
            if Deck.hasCard[x]:
                print(Deck.deck[x])
                
    def in_deck(self,pos):
        return Deck.hasCard[pos]
    
    def draw(self):
        pos=randint(0,51)
        while(not(Deck.in_deck(self,pos))):
              pos=randint(0,51)
        Deck.hasCard[pos]=False
        return Deck.deck[pos]

    def reset(self):
        print("Reshuffling deck")
        for x in range(len(Deck.hasCard)):
            Deck.hasCard[x]=True
            
    def is_empty(self):
        for x in Deck.hasCard:
            if x==True:
                return False
        return True
    
###########TESTS###########
"""myD=Deck()
for x in range(52):
    print(myD.deck[x])
    print(x)
print(myD.is_empty())

for x in range(52):
    myD.draw()
print(myD.is_empty())
print("************")
myD.print()
print("reset")
myD.reset()
myD.print()
print(myD.is_empty())"""
#########TESTS############


class blj:
    myD=Deck()
    bank=1000
    bet=0
    cardno=3
    gameover=False
    player_total=0
    dealer_total=0
    player_ace=0
    dealer_ace=0
    player_bust=False
    dealer_bust=False
    def __init__(self):
        pass

    def check_number(self,num):
        for x in num:
            if (not x.isdigit()):
                return False
        else:
            return True
    
    def how_much_bet(self):
        bet=input("How much do you bet? ")
        bet_okay=False
        while(not bet_okay):
            if (blj.check_number(self,bet)):
                bet=int(bet)
                if(bet<=blj.bank):
                    bet_okay=True
                else:
                    bet=input("Invalid bet. How much do you bet? ")
            else:
                bet=input("Invalid bet. How much do you bet? ")
        blj.bet=bet #bet is okay
        return blj.bet

    def check_ace(self,person):
        if person=="player":
            if blj.player_ace>0:
                blj.player_total=blj.player_total-10
                blj.player_ace=blj.player_ace-1
        elif person=="dealer":
            if blj.dealer_ace>0:
                blj.dealer_total=blj.dealer_total-10
                blj.dealer_ace=blj.dealer_ace-1
    
    def check_player_bust(self):
        if blj.player_total>21:
            blj.check_ace(self,"player")
        if blj.player_total>21:
            blj.player_bust=True
            print("You bust!")
            
    def check_dealer_bust(self):
        if blj.dealer_total>21:
            blj.check_ace(self,"dealer")
        if blj.dealer_total>21:
            blj.dealer_bust=True
            print("Dealer bust!")

    def add_to_total(self,person,pos):
        if(person=="player"):
            if(pos%13<=10 and pos%13>=2):
                value=pos%13
            elif(pos%13==0):
                value=11
                blj.player_ace=blj.player_ace+1
            else:
                value=10
            blj.player_total=blj.player_total+value
        elif(person=="dealer"):
            if(pos%13<=10 and pos%13>=2):
                value=pos%13
            elif(pos%13==0):
                value=11
                blj.dealer_ace=blj.dealer_ace+1
            else:
                value=10
            blj.dealer_total=blj.dealer_total+value
    

    def dealer_first(self):
        card1=blj.myD.draw()
        print("Dealer Card 1: "+card1)
        blj.add_to_total(self,"dealer",blj.myD.deck.index(card1))
        print("Dealer Total: "+str(blj.dealer_total))


    def dealer_play(self):
        print()
        print("Dealer's Turn:")
        cardno=2
        while blj.dealer_total<17:
            card=blj.myD.draw()
            print("Dealer Card "+str(cardno)+": "+card)
            cardno=cardno+1
            blj.add_to_total(self,"dealer",blj.myD.deck.index(card))
            blj.check_dealer_bust(self)
        print("Dealer's Total: "+str(blj.dealer_total))

    
    def deal_first_two(self):
        print("Your hand:")
        card1=blj.myD.draw()
        print("Card 1:", card1)
        blj.add_to_total(self,"player",blj.myD.deck.index(card1))
        card2=blj.myD.draw()
        print("Card 2:", card2)
        blj.add_to_total(self,"player",blj.myD.deck.index(card2))
        if(blj.player_total==21):
            print("You got blackjack!")
        print("Total: "+str(blj.player_total))

    def hit(self):
        card=blj.myD.draw()
        print("Card "+str(blj.cardno)+": "+card)
        blj.cardno=blj.cardno+1
        blj.add_to_total(self,"player",blj.myD.deck.index(card))

    def dd(self):
        blj.bet=2*blj.bet
        print("Your bet: "+str(blj.bet))
        card3=blj.myD.draw()
        print("Card 3: "+card3)
        blj.add_to_total(self,"player",blj.myD.deck.index(card3))
        print("Total: "+str(blj.player_total))
        blj.check_player_bust(self)
        
    def hit_stand_dd(self):
        key=input("Hit(1),Stand(2), or Double Down(3)? ")
        while True:
            if key=="1":
                blj.hit(self)
                blj.check_player_bust(self)
                print("Total: "+str(blj.player_total))
                if blj.player_bust:
                    return 0                    
                while True:
                    key=input("Hit(1) or Stand(2)? ")
                    if key=="1":
                        blj.hit(self)
                        blj.check_player_bust(self)
                        print("Total: "+str(blj.player_total))
                        if blj.player_bust:
                            return 0
                    elif key=="2":
                        return 0
            elif key=="2":
                return 0
            elif key=="3":
                blj.dd(self)
                return 0
            else:
                print("Please print a value between 1-3")
                key=input("Hit(1),Stand(2), or Double Down(3)? ")
                
    def win_or_lose(self):
        if blj.player_bust:
            blj.bank=blj.bank-blj.bet
        elif blj.dealer_bust:
            print("You win!")
            blj.bank=blj.bank+blj.bet
        else:
            if(blj.dealer_total>blj.player_total):
                print("You lose!")
                blj.bank=blj.bank-blj.bet
            elif(blj.dealer_total==blj.player_total):
                print("Tie!")
            else:
                print("You win!")
                blj.bank=blj.bank+blj.bet
        blj.bet=0
        print("Bank: "+str(blj.bank))

    def reset(self): #resets everything except bank
        blj.bet=0
        blj.myD=Deck()
        blj.cardno=3
        blj.player_total=0
        blj.dealer_total=0
        blj.player_ace=0
        blj.dealer_ace=0
        blj.player_bust=False
        blj.dealer_bust=False               

def run_blackjack():
    print("Welcome to BlackJack! Your starting bank balance is $1000")
    game=blj()
    while (not blj.gameover):
        game.how_much_bet()
        game.dealer_first()
        print()
        game.deal_first_two()
        game.hit_stand_dd()
        if game.player_bust:
            game.win_or_lose()
            if(blj.bank<=0):
                print("Game Over! Thanks for playing")
                blj.gameover=True
            game.reset()
        else:
            game.dealer_play()
            game.win_or_lose()
            game.reset()
        

############"TESTS################
run_blackjack()





