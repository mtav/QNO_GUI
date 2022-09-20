#!/usr/bin/env python
try:
    import sys
    from random import shuffle

    from pygame_cards import enums, card, card_holder
except ImportError as err:
    print("Fail loading a module in file:", __file__, "\n", err)
    sys.exit(2)


class Deck(card_holder.CardsHolder):
    """ Deck of cards. Two types of deck available: short (6..ace) and full (2..ace)"""

    def __init__(self, type_, pos, offset, last_card_callback=None):
        """
        :param type_: int value that corresponds to enum from enums.DeckType class
        :param pos: tuple with coordinates (x, y) for bottom card in the desk
        :param last_card_callback: function that should be called when the last card is
            removed from the deck
        """
        card_holder.CardsHolder.__init__(self, pos, offset, False, last_card_callback)
        self.type = type_

        start = enums.Rank.two  # full deck type by default
        if type_ == enums.DeckType.short:
            start = enums.Rank.six

        card_pos = pos
        # for rank in range(start, enums.Rank.ace + 1):
        #     for suit in range(enums.Suit.hearts, enums.Suit.spades + 1):
        #         self.cards.append(card.Card(suit, rank, card_pos, True))
        #         card_pos = card_pos[0] + self.offset[0], card_pos[1] + self.offset[1]

        qno_deck = self.buildDeck()
        for c in qno_deck:
            state = c[0]
            value = c[1]
            self.cards.append(card.Card(state, value, card_pos, True))
            card_pos = card_pos[0] + self.offset[0], card_pos[1] + self.offset[1]

    def buildDeck(self):
        deck = []
        states = ["|00>", "|01>", "|10>", "|11>"]
        values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Draw Two", "Skip", "Reverse"]
        gateState = ["Gate"]
        gateVal = ["H", "X", "CNOT"]

        # tiny deck
        # values = [1, 2, 3, 4]
        # values = [0]
        # gateVal = ["H"]*10
        # gateVal = ["X", "CNOT"]
        Ncopies = 1

        for state in states:
            for i in range(Ncopies):
                for value in values:
                    cardVal = [state, value]
                    deck.append(cardVal)
                    if value != 0:
                        deck.append(cardVal)

        ##### add gates
        for i in range(4):
            for gate in gateState:
                for gatevalue in gateVal:
                    cardVal = [gate, gatevalue]
                    deck.append(cardVal)

        # # add extra testing cards
        # for state in states:
        #     for i in range(50):
        #         deck.append([state, "Reverse"])
        # for state in states:
        #     for i in range(50):
        #         deck.append([state, "Draw Two"])

        print('======')
        print('N cards: ', len(deck))
        print('======')
        # for i in deck:
        #     print(i)
        # print('======')
        return (deck)

    def shuffle(self):
        """ Shuffles cards in the deck randomly """
        shuffle(self.cards)
        self.update_position()
