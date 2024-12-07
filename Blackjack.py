import random

#Card Class
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def val(self):
        if self.rank == 14:
            return 11
        elif self.rank > 10:
            return 10
        else:
            return self.rank

#deck class        
class Deck:
    def __init__(self):
        self.cards = []
        suits = ['hearts', 'diamons', 'clubs', 'spades']
        ranks = [2,3,4,5,6,7,8,9,10,11,12,13,14]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))
        
        random.shuffle(self.cards)

    def shuffle(self):
        pass

    def deal(self):
        return self.cards.pop()
        
#player class
class Player:
    def __init__(self, is_dealer=False):
        self.hand = []
        self.is_dealer = is_dealer
    
    def hand_value(self):
        total = sum(card.value() for card in self.hand)
        num_aces = sum(1 for card in self.hand if card.rank == 'Ace')
        
        # Adjust for aces (either 1 or 11)
        while total > 21 and num_aces:
            total -= 10  # Treat Ace as 1 instead of 11
            num_aces -= 1
        
        return total

    def hit(self, deck):
        self.hand.append(deck.deal_card())

    def show_hand(self):
        return ', '.join(str(card) for card in self.hand)

    def is_busted(self):
        return self.hand_value() > 21

#blackjack game function
def play_blackjack():
    deck = Deck()

    player = Player(is_dealer=False)
    dealer = Player(is_dealer=True)

    # Initial dealing
    player.hit(deck)
    dealer.hit(deck)
    player.hit(deck)
    dealer.hit(deck)

    # Show hands
    print("Dealer's hand: [", dealer.hand[0], ", ? ]")
    print("Your hand:", player.show_hand())

    # Player's turn
    while player.hand_value() < 21:
        action = input("Do you want to 'hit' or 'stand'? ").lower()
        if action == 'hit':
            player.hit(deck)
            print("Your hand:", player.show_hand())
        elif action == 'stand':
            break
        else:
            print("Invalid input. Please choose 'hit' or 'stand'.")

    # Dealer's turn
    if not player.is_busted():
        print("Dealer's hand:", dealer.show_hand())
        while dealer.hand_value() < 17:
            print("Dealer hits.")
            dealer.hit(deck)
            print("Dealer's hand:", dealer.show_hand())

    # Determine the winner
    if player.is_busted():
        print("You busted! Dealer wins.")
    elif dealer.is_busted():
        print("Dealer busted! You win.")
    else:
        player_total = player.hand_value()
        dealer_total = dealer.hand_value()
        
        if player_total > dealer_total:
            print(f"You win with {player_total} against the dealer's {dealer_total}.")
        elif player_total < dealer_total:
            print(f"Dealer wins with {dealer_total} against your {player_total}.")
        else:
            print(f"It's a tie! Both have {player_total}.")


if __name__=="__main__":
    play_blackjack()