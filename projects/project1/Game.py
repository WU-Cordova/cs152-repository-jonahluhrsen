from Multideck import Multideck
from Card import Card
import random


class Game:
    def __init__(self):
        self.num_decks = random.choice([2,4,6,8])
        self.deck = Multideck(self.num_decks)
        self.player_hand = []
        self.dealer_hand = []

    def deal_initial_cards(self):
        # Method to deal the initial two cards to the player and dealer
        self.player_hand.append(self.deck.deal_card())
        self.player_hand.append(self.deck.deal_card())
        self.dealer_hand.append(self.deck.deal_card())
        self.dealer_hand.append(self.deck.deal_card())

    def show_hands(self, hide_dealer_card = None):
        # Method to display the player's and dealer's hands
        # If hide_dealer_card is True, the dealer's second card is hidden
        print(f"Players deck is: {str(self.player_hand[0]), str(self.player_hand[1])}")
        if hide_dealer_card == True:
            print(f"Dealers hand is: {str(self.dealer_hand[0]), 'HIDDEN'}")
        else:
            print(f"Dealers hand is: {str(self.dealer_hand[0]), str(self.dealer_hand[1])}")
    
    

    def calculate_hand_value(self, hand):
        # Method to calculate the total value of a hand (accounting for Aces)
        total = sum(card.value for card in hand)
        num_aces = sum(1 for card in hand if card.rank == 'A')

        # Adjust Aces from 11 to 1 if total exceeds 21
        while total > 21 and num_aces > 0:
            total -= 10  # Convert one Ace from 11 to 1
            num_aces -= 1
        
        return total
    def player_turn(self):
    # Method to handle the player's turn (hitting or staying)
        while True:
            player_decision = input("Do you want to (H)it or (S)tay?: ").upper()
            if player_decision == "H":
                self.player_hand.append(self.deck.deal_card())
                player_sum = self.calculate_hand_value(self.player_hand)
                print(f"Player's hand: {[str(card) for card in self.player_hand]}, total: {player_sum}")
                if player_sum > 21:
                    print("Bust! You exceeded 21.")
                    self.determine_winner()
                    return  # Ends the player's turn immediately
                elif player_sum == 21:
                    print("21! Let's see what the dealer has.")
                    self.dealer_turn()
                    return  # Ends the player's turn immediately
            elif player_decision == "S":
                self.show_hands(hide_dealer_card=False)
                self.dealer_turn()
                return  # Ends the player's turn and moves to dealer's turn
            else:
                print("Not a valid answer. Please enter 'H' to hit or 'S' to stay.")


    def dealer_turn(self):
        # Method to handle the dealer's turn (drawing until reaching at least 17)
        dealer_sum = self.calculate_hand_value(self.dealer_hand)
        while self.calculate_hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.deal_card())
            dealer_sum = self.calculate_hand_value(self.dealer_hand)
            print(f"Dealers hand is: {str(self.dealer_hand[0]), str(self.dealer_hand[1]), str(self.dealer_hand[2])}, total {dealer_sum}")
        else:
            print(f"Dealers hand is: {str(self.dealer_hand[0]), str(self.dealer_hand[1])}, total {dealer_sum}")
        self.determine_winner()

    def determine_winner(self):
    # Method to determine the winner of the round (player, dealer, or tie)
        player_total = self.calculate_hand_value(self.player_hand)
        dealer_total = self.calculate_hand_value(self.dealer_hand)

        print(f"\nFinal Results:")
        print(f"Player's Hand: {[str(card) for card in self.player_hand]} - Total: {player_total}")
        print(f"Dealer's Hand: {[str(card) for card in self.dealer_hand]} - Total: {dealer_total}")

        if player_total > 21:
            print("Player busts! Dealer wins.")
        elif dealer_total > 21:
            print("Dealer busts! Player wins.")
        elif player_total > dealer_total:
            print("Player wins!")
        elif dealer_total > player_total:
            print("Dealer wins!")
        else:
            print("It's a tie!")

    def play_round(self):
        # Method to play a single round of the game
        pass

    def play_game(self):
    # Loop to allow multiple rounds
        while True:
            # Reset hands before each round
            self.player_hand = []
            self.dealer_hand = []
            self.deck = Multideck(self.num_decks)  # Optional: reshuffle the deck
            
            self.deal_initial_cards()
            self.show_hands(True)
            self.player_turn()

            # Ask if the player wants to play again
            play_again = input("\nDo you want to play again? (Y)/(N): ").upper()
            if play_again != "Y":
                print("Thanks for playing! Goodbye.")
                break  # Exit the loop to end the game