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
            #i = 0
            #j = 0
            """ 
            Need to create flag so the dealer doesn't get a new card everytime a player wants to hit
            """
            if(not self.dealerHit):
                cardTuple = self.shoeLst[0][random.randint(1, len(self.shoeLst[0]))]
                self.playerDict.setdefault(loopCounter, []).append(cardTuple)
                #self.playersHandLst.append(cardTuple)
                self.shoeLst[0].remove(cardTuple)
            else:     
                cardTuple = self.shoeLst[0][random.randint(1, len(self.shoeLst[0]))]
                self.dealerHandLst.append(cardTuple)
                self.shoeLst[0].remove(cardTuple)

        print(self.playerDict)
        
        """ print('player')
        print(self.playersHandLst) """
        print('dealer')
        print(self.dealerHandLst)

    def checkWinner(self):
        playerStillHitting = True
        #playerHitLst = []
        playerBust = False

        self.checkDealerBlackJack()
        
        #initialize loop counter
        i = 0
        #loop through players and ask if they want to hit
        while(self.inPlay):
            for i in range(self.numPlayers):
                while(playerStillHitting):
                    hitOrNah = input("Player " + str(i) + " Hit or Stay? Type 'H' or 'S'")
                    if(hitOrNah == 'H' or hitOrNah == 'h' ):
                        #playerHitLst.append('h')
                        self.dealCards(i)
                        #check if player has bust or not. Will return true if bust has occured
                        playerBust = self.checkBust(i)
                        #remove player from play if they bust
                        if(playerBust):
                            print("***BUST***")
                            playerStillHitting = False
                            removedVal = self.playerDict.pop(i)
                            print(removedVal)
                        else:
                            #reset to true so other players can hit
                            playerStillHitting = True
                            #need this to ask the player
                            hitOrNah = input("Player " + str(i) + " Hit or Stay: Type 'H' or 'S'" )
                            #check if the player has NOT busted and if they want to hit
                            if(not playerBust and hitOrNah == 'H' or hitOrNah == 'h'):
                                self.dealCards(i)
                                self.checkBust(i)
                    elif(hitOrNah == 'S' or hitOrNah == 's'):
                        playerStillHitting = False
                        #playerHitLst.append('s')
                        #self.inPlay = False
                    else:
                        print("Please type 'H' to Hit or 'S' to Stay")
                        print()
                playerStillHitting = True
                i += 1
                """
                    find a way to ensure dealer gets to hit when all the players
                    have finished hitting or staying.
                    Already have a list containing player hit or stay
                """
                #all players have hit or stayed now it's dealers turn
                if( i == self.numPlayers):
                    self.dealerHit = True
                    self.dealCards(0)
            self.inPlay = False
            
    def checkDealerBlackJack(self):
        #grab dealers down card and up card and save the rank
        dealerDownCard = self.dealerHandLst[0][0]
        dealerUpCard = self.dealerHandLst[1][0]

        print("Down card " + str(dealerDownCard))
        print("Up card " + str(dealerUpCard))
        
        #check if dealer has a blackjack. End the game if true
        if(dealerUpCard == 'A' and dealerDownCard == '10'):
            self.inPlay = False
        elif(dealerUpCard == 'A' and dealerDownCard == 'J'):
            self.inPlay = False
        elif(dealerUpCard == 'A' and dealerDownCard == 'Q'):
            self.inPlay = False
        elif(dealerUpCard == 'A' and dealerDownCard == 'K'):
            self.inPlay = False
        else:
            self.inPlay = True

    def checkBust(self, playerNum):
        """
            loop through players hand to determine if they have busted or not
        """
        playerHandValue = 0
        playerHandLst = self.playerDict.get(playerNum)
        i = 0
        for i in range(len(playerHandLst)):
            if(playerHandLst[i][0] == 'J'):
                playerHandValue += 10
            elif(playerHandLst[i][0] == 'Q'):
                playerHandValue += 10
            elif(playerHandLst[i][0] == 'K'):
                playerHandValue += 10
            else:
                playerHandValue += playerHandLst[i][0]
            if(playerHandValue > 21):
                return True
            i += 1

        """
            return true or false if the player has busted
        """

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
