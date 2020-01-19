#import random module
import random

class Card:
    
    def __init__(self):
        super().__init__()
        
    def getSuit(self):
        suitLst = ['S', 'C', 'D', 'H']
        #return random index in lst
        return suitLst[random.randint(0, 3)]
        
    def getRank(self):
        rankLst = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        #return random index in lst
        return rankLst[random.randint(0,8)]
    
    def getFace(self):
        faceLst = ['J', 'Q', 'K', 'A']
        #return random index in lst
        return faceLst[random.randint(0, 3)]

    def createCard(self):
        suit = self.getSuit()
        rank = self.getRank()
        face = self.getFace()
        #return tuple which represents single card
        return (rank, face, suit)

card = Card()
#two.printCard()
#cardTuple = card.createCard()