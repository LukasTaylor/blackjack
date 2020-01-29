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
        #self.playersLst = []
        self.inPlay = True
        self.playersHandLst = []
        self.dealerHandLst = []
        self.numDecks = 1
        self.deck = Deck()
        self.shoeLst = []
        self.playGame()
        self.numPlayers = 0
        
        
        
    def createShoe(self):
        tempLst = []
        i = 0
        #add one deck of cards per iteration
        for i in range(self.numDecks):
            tempLst.append(self.deck.getCards())
            i += 1
        #combine decks together to create one big shoe for gameplay
        self.shoeLst.append(tempLst[0])
    
    def dealCards(self):
        playerDict = {}
        handLst = []
        firstDeal = True
        cardTuple = ()
        i = 0 
        j = 0
        if(firstDeal):
            #loop range will be the number of players + dealer
            for i in range(2):
                for j in range(self.numPlayers):
                    #grab random cards from the shoeLst
                    cardTuple = self.shoeLst[0][random.randint(0, len(self.shoeLst)%2)]
                    #set an empty list @ each key and append a card to the list
                    playerDict.setdefault(j, []).append(cardTuple)
                    #remove card from the shoe so it's not in play anymore
                    self.shoeLst[0].remove(cardTuple)
                    #deal one card to dealer at a time
                    if (j < 1 ):
                        #grab random cards from the shoeLst
                        cardTuple = self.shoeLst[0][random.randint(0, len(self.shoeLst)%2)]
                        #add the card to the dealers hand
                        self.dealerHandLst.append(cardTuple)
                        #remove the card from the shoe
                        self.shoeLst[0].remove(cardTuple)
                    j += 1  
                i += 1
            firstDeal = False
        else:
            cardTuple = self.shoeLst[0][random.randint(1, len(self.shoeLst))]
            self.playersHandLst.append(cardTuple)
            self.shoeLst[0].remove(cardTuple)
            cardTuple = self.shoeLst[0][random.randint(1, len(self.shoeLst))]
            self.dealerHandLst.append(cardTuple)
        
        print(playerDict)
        
        """ print('player')
        print(self.playersHandLst) """
        print('dealer')
        print(self.dealerHandLst)

    def checkWinner(self):
        print("in checkWinner()")
        
        self.inPlay = False

    def userPrompt(self):
        #cast input to int
        self.numDecks = int(input("How many decks should be in the shoe?"))
        self.numPlayers = int(input("How many players are going to play?"))
        self.createShoe()
    
    def playGame (self):
        self.userPrompt()
        while(self.inPlay):
            self.dealCards()
            self.checkWinner()

        

    """ def printShoe(self):
        i = 0
        for i in range(len(self.shoeLst)):
            print(self.shoeLst[i]) """
    

""" deck = Deck()
deck.getCard()
deck.printDeck() """
newGame = Game()

#newGame.printShoe()
