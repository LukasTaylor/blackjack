import random

class Deck:
    def __init__(self):
        super().__init__()
        self.cardLst = []
        self.cardPair = ()
    
    def getCards(self):
        suitLst = ['S', 'C', 'D', 'H']
        rankLst = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        faceLst = ['J', 'Q', 'K', 'A']
        i = 0
        j = 0
        #pair ranks with suits
        for i in range(len(rankLst)):
            for j in range(len(suitLst)):
                self.cardPair = (rankLst[i], suitLst[j])
                self.cardLst.append(self.cardPair)
                j+=1
            i +=1
        #pair faces with suits
        for i in range(len(faceLst)):
            for j in range(len(suitLst)):
                self.cardPair = (faceLst[i], suitLst[j])
                self.cardLst.append(self.cardPair)
                j+=1
            i +=1
        return self.cardLst

class Game:
    def __init__(self):
        super().__init__()
        self.inPlay = True
        self.firstDeal = True
        self.dealerHit = False
        self.playerDict = {}
        self.dealerHandLst = []
        self.deck = Deck()
        self.shoeLst = []
        self.playGame()
        self.numPlayers = 0
        
    def createShoe(self, numDecks):
        tempLst = []
        i = 0
        #add one deck of cards per iteration
        for i in range(numDecks):
            tempLst.append(self.deck.getCards())
            i += 1
        #combine decks together to create one big shoe for gameplay
        self.shoeLst.append(tempLst[0])
    
    def dealCards(self, loopCounter):
        cardTuple = ()
        i = 0 
        j = 0
        if(self.firstDeal):
            #loop range will be the number of players + dealer
            for i in range(2):
                for j in range(self.numPlayers):
                    #grab random cards from the shoeLst
                    cardTuple = self.shoeLst[0][random.randint(1, len(self.shoeLst[0]))]
                    #set an empty list @ each key and append a card to the list
                    self.playerDict.setdefault(j, []).append(cardTuple)
                    #remove card from the shoe to remove from gameplay
                    self.shoeLst[0].remove(cardTuple)

                    #deal one card to dealer at a time
                    if (j < 1 ):
                        #grab random cards from the shoeLst
                        cardTuple = self.shoeLst[0][random.randint(1, len(self.shoeLst[0]))]
                        #add the card to the dealers hand
                        self.dealerHandLst.append(cardTuple)
                        #remove the card from the shoe
                        self.shoeLst[0].remove(cardTuple)
                    j += 1  
                i += 1
            self.firstDeal = False
        else:
            if(not self.dealerHit):
                cardTuple = self.shoeLst[0][random.randint(1, len(self.shoeLst[0]))]
                self.playerDict.setdefault(loopCounter, []).append(cardTuple)
                #self.playersHandLst.append(cardTuple)
                self.shoeLst[0].remove(cardTuple)
            else:     
                cardTuple = self.shoeLst[0][random.randint(1, len(self.shoeLst[0]))]
                self.dealerHandLst.append(cardTuple)
                self.shoeLst[0].remove(cardTuple)

        """ print(self.playerDict.get(loopCounter))
        print('dealer')
        print(self.dealerHandLst) """

    def checkWinner(self):
        playerStillHitting = True
        hitOrNah = ''
        #playerHitLst = []
        playerBust = False

        #check if dealer has blackjack
        self.checkDealerBlackJack()

        print("Dealer hand:")
        print(self.dealerHandLst)

        #initialize loop counter
        i = 0
        #loop through players and ask if they want to hit
        while(self.inPlay):
            for i in range(self.numPlayers): 
                while(playerStillHitting):
                    playerBlackJack = self.checkPlayerBlackJack(i)
                    print("Player " + str(i+1) + " hand")
                    self.printHand(i)
                    #end players opportunity to hit if they've got blackjack
                    if(not playerBlackJack):
                        hitOrNah = input("Player " + str(i+1) + " Hit or Stay? Type 'H' or 'S'")
                    else:
                        playerStillHitting = False
                        print("****BLACKJACK*****")
                    if(hitOrNah == 'H' or hitOrNah == 'h' ):
                        self.dealCards(i)
                        #check if player has bust or not. Will return true if bust has occured
                        playerBust = self.checkBust(i)
                        #remove player from play if they bust
                        if(playerBust):
                            print("Player " + str(i+1) + " hand")
                            self.printHand(i)
                            print("***BUST***")
                            playerStillHitting = False
                            self.playerDict.pop(i)
                    elif(hitOrNah == 'S' or hitOrNah == 's'):
                        playerStillHitting = False
                    else:
                        print("Please type 'H' to Hit or 'S' to Stay")
                        print()
                playerStillHitting = True
                i += 1

            #all players have hit or stayed now it's dealers turn
            if( i == self.numPlayers):
                self.dealerHit = True
                self.dealCards(0)
                dealerBust = self.checkBust(0)
                if(dealerBust):
                    print("***DEALER BUST***")
                    print("Everybody wins!!!")

                    self.inPlay = False
                else:
                    self.payDealer()
            print(self.playerDict)
            print(len(self.playerDict))
            #gameover
            self.inPlay = False
            
    def checkDealerBlackJack(self):
        #grab dealers down card and up card and save the rank
        dealerDownCard = self.dealerHandLst[0][0]
        dealerUpCard = self.dealerHandLst[1][0]

        #check if dealer has a blackjack. End the game if true
        if(dealerUpCard == 'A' and dealerDownCard == '10' or dealerUpCard == '10' and dealerDownCard == 'A'):
            self.inPlay = False
        elif(dealerUpCard == 'A' and dealerDownCard == 'J' or dealerUpCard == 'J' and dealerDownCard == 'A'):
            self.inPlay = False
        elif(dealerUpCard == 'A' and dealerDownCard == 'Q' or dealerUpCard == 'Q' and dealerDownCard == 'A'):
            self.inPlay = False
        elif(dealerUpCard == 'A' and dealerDownCard == 'K' or dealerUpCard == 'K' and dealerDownCard == 'A'):
            self.inPlay = False
        else:
            self.inPlay = True
    
    def checkPlayerBlackJack(self, playerNum):
        handValue = 0

        #retrieve player's hand
        handLst = self.playerDict.get(playerNum)
        
        #loop through players hand to determine if they have busted or not
        i = 0
        for i in range(len(handLst)):
            if(handLst[i][0] == 'J'):
                handValue += 10
            elif(handLst[i][0] == 'Q'):
                handValue += 10
            elif(handLst[i][0] == 'K'):
                handValue += 10
            elif(handLst[i][0] == 'A'):
                if(len(handLst) < 2):
                    handValue += 1
                else:
                    handValue += 11
            else:
                handValue += handLst[i][0]
            
            #return true if player has blackjack
            if(handValue == 21):
                return True
            
            i += 1
        return False
            
    def checkBust(self, playerNum):
        handValue = 0
        
        if(self.dealerHit):
            handLst = self.dealerHandLst
        else:
            handLst = self.playerDict.get(playerNum)
        
        #loop through players hand to determine if they have busted or not
        i = 0
        for i in range(len(handLst)):
            if(handLst[i][0] == 'J'):
                handValue += 10
            elif(handLst[i][0] == 'Q'):
                handValue += 10
            elif(handLst[i][0] == 'K'):
                handValue += 10
            elif(handLst[i][0] == 'A'):
                askUser = input("Should Ace = 1 or 11?")
                if(int(askUser) == 1):
                    handValue += 1
                else:
                    handValue += 11
            else:
                handValue += handLst[i][0]
            #return true if player busts
            if(handValue > 21):
                return True
            i += 1
        return False

    def payDealer(self):
        print("payDealer()")
        dealerWinTotal = 0
        i = 0
        for i in range(len(self.playerDict)):
            print("paid")
            i += 1



    def printHand(self, playerNum):
        if(self.dealerHit):
            print(self.dealerHandLst)
        else:
            print(self.playerDict.get(playerNum))

    def userPrompt(self):
        #cast input to int
        numDecks = int(input("How many decks should be in the shoe?"))
        self.numPlayers = int(input("How many players are going to play?"))
        self.createShoe(numDecks)
    
    def playGame (self):
        self.userPrompt()
        while(self.inPlay):
            #pass 0 and an empty list to satisfy parameter requirements
            self.dealCards(0)
            self.checkWinner()

""" deck = Deck()
deck.getCard()
deck.printDeck() """
newGame = Game()

#newGame.printShoe()
