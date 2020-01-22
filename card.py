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
        self.shoeLst = []
        self.numDecks = 1
        self.deck = Deck()
        self.askShoeSize()
        
    def createShoe(self):
        tempLst = []
        i = 0
        #add one deck of cards per iteration
        for i in range(self.numDecks):
            tempLst.append(self.deck.getCards())
            i += 1
        #combine decks together to create one big shoe for gameplay
        self.shoeLst.append(tempLst[0])
        
    def askShoeSize(self):
        #cast input to int
        self.numDecks = int(input("How many decks should be in the shoe?"))
        self.createShoe()
        
    def printShoe(self):
        i = 0
        for i in range(len(self.shoeLst)):
            print(self.shoeLst[i])
    

""" deck = Deck()
deck.getCard()
deck.printDeck() """
newGame = Game()
newGame.printShoe()
