class Deck:
    def __init__(self):
        super().__init__()
        self.cardLst = []
        self.cardPair = ()
    
    def getCard(self):
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

    def printDeck(self):
        i = 0
        for i in range(52):
            print(i)
            print(self.cardLst[i])

deck = Deck()
deck.getCard()
deck.printDeck()