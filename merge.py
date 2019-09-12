from random import shuffle


class Card:
    suits = ["spades",
             "diamonds",
             "hearts",
             "clubs"]

    values = [None, None, "2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace"]

    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
        return False
        # 此处注意最后return否则小于时无返回值！！！

    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        # 若需要在赋值时换行可以使用"\"
        return v


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    # random模块中的shuffle函数随机排列模拟洗牌

    def rm_card(self):
        if len(self.cards) == 0:
            return
        else:
            return self.cards.pop()
        # pop()方法，返回列表中的最后一个元素，并将其删除


class Player:
    def __init__(self, name):
        self.name = name
        self.win = 0
        self.card = None


class Game:
    def __init__(self):
        name1 = input("Please enter p1's name")
        name2 = input("Please enter p2's name")
        self.p1 = Player(name1)
        self.p2 = Player(name2)
        self.deck = Deck()

    def wins_out(self,winner):
        w="{} wins this round, Congratulations!".format(self.winner)
        print(w)

    def draw(self,pl1,pc1,pl2,pc2):
        d="{} drew {}   {} drew {}".format(pl1,pc1,pl2,pc2)
        print(d)

    def winner(self,p1,p2):
        if self.p1.win>self.pw.win:
            return self.p1.name
        if self.p1.win < self.pw.win:
            return self.p2.name
        print("It was a tie")
        return "Nobody"

    def play_game(self):
        cards=self.deck.cards
        print("War begins now!")
        while len(cards)>2:
            m="q to quit"
            response=input(m)
            if m=="q":
                break
            pc1=self.deck.rm_card()
            pc2=self.deck.rm_card()
            if pc1>pc2:
                self.p1.win+=1
                self.wins_out(self.p1.name)
            else:
                self.p2.win += 1
                self.wins_out(self.p2.name)
        win = self.winner(self.p1, self.p2)
        print("War is over, {} wins the game".format(win))





game=Game()
game.play_game()





