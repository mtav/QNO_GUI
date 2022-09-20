#!/usr/bin/env python
try:
    import sys
    from pygame_cards import card_sprite
    from pygame_cards import game_object
except ImportError as err:
    print("Fail loading a module in file:", __file__, "\n", err)
    sys.exit(2)

class color:
   BLUE = '\033[44m'
   GREEN = '\033[42m'
   YELLOW = '\033[43m'
   RED = '\033[41m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class Card(game_object.GameObject):
    """ This class represents a card. """

    def __init__(self, suit, rank, pos, back_up=False):
        game_object.GameObject.__init__(self)
        self.suit = suit
        self.rank = rank
        self.sprite = card_sprite.CardSprite(suit, rank, pos, back_up)
        self._back_up = back_up

    @property
    def state(self):
        return self.suit
    @state.setter
    def state(self, value):
        self.suit = value

    @property
    def value(self):
        print('VALUE CALLED:', self.rank, self.suit)
        self.printInfos()
        return self.rank
    @state.setter
    def value(self, val):
        self.rank = val

    @property
    def bobby(self):
        print('VALUE CALLED:', self.rank, self.suit)
        raise
        self.printInfos()
        return self.rank
    @state.setter
    def bobby(self, val):
        self.rank = val

    def printInfos(self):
        print('state', self.getState())
        print('value', self.getValue())
        print('suit', self.suit)
        print('rank', self.rank)
        # print('state', self.state)
        # print('value', self.value)
        # print('bobby', self.bobby)
        # print('bobby', self.bobby)

    def __str__(self):
        s = f'{self.getState()}-{self.getValue()}'
        if self.getState()=="|00>":
            col = color.RED
            # s="[" ,  , color.BOLD , players[playerTurn][-1][0] , "  " , players[playerTurn][-1][1] , color.END , "]"
        elif self.getState()=="|01>":
            col = color.YELLOW
            # print("You drew: " ,  "[" , color.YELLOW , color.BOLD , players[playerTurn][-1][0] ,"  ", players[playerTurn][-1][1] , color.END , "]" )
        elif self.getState()=="|10>":
            col = color.GREEN
            # print("You drew: " ,  "[" , color.GREEN , color.BOLD , players[playerTurn][-1][0] ,"  ", players[playerTurn][-1][1] , color.END , "]" )
        elif self.getState()=="|11>":
            col = color.BLUE
            # print("You drew: " ,  "[" , color.BLUE , color.BOLD , players[playerTurn][-1][0] ,"  ", players[playerTurn][-1][1] , color.END , "]" )
        else:
            col = None
            # s=["[" , color.BOLD , players[playerTurn][-1][1] , color.END , color.RED , color.BOLD , "G" , color.END, color.YELLOW , color.BOLD , "A" ,color.END, color.GREEN , color.BOLD , "T", color.END, color.BLUE , color.BOLD , "E" , color.END , "]" ]
            L = [color.RED , color.BOLD , "G" , color.END,
                 color.YELLOW , color.BOLD , "A" ,color.END,
                 color.GREEN , color.BOLD , "T", color.END,
                 color.BLUE , color.BOLD , "E" , color.END]

            colored_gate_string = ''.join(L)
            s = f'{colored_gate_string}-{self.getValue()}'

        if col:
            s = col + color.BOLD + s + color.END
        return s

    def getState(self):
        return self.suit
    def setState(self, state):
        self.suit = state
    def getValue(self):
        return self.rank
    def setValue(self, value):
        self.rank = value

    @property
    def back_up(self):
        return self._back_up

    @back_up.setter
    def back_up(self, value):
        self._back_up = value
        self.sprite.back_up = self._back_up

    def get_sprite(self):
        """ Returns card's spite object
        :return: card's sprite object
        """
        return self.sprite

    # def get_back_sprite(self):
    #     return self.back_sprite

    def render(self, screen):
        """ Renders the card's sprite on a screen passed in argument
        :param screen: screen to render the card's sprite on
        """
        self.sprite.render(screen)

    def flip(self):
        """ Flips the card from face-up to face-down and vice versa """
        self.back_up = not self.back_up

    def is_clicked(self, pos):
        """ Checks if mouse click is on card
        :param pos: tuple with coordinates of mouse click (x, y)
        :return: True if card is clicked, False otherwise
        """
        return self.sprite.is_clicked(pos)

    def check_collide(self, card_=None, pos=None):
        """ Checks if current card's sprite collides with other card's sprite, or with
        an rectangular area with size of a card. Parameters card and pos are mutually exclusive.
        :param card_: Card object to check collision with
        :param pos: tuple with coordinates (x,y) - top left corner of area to check collision with
        :return: True if cards/card and area collide, False otherwise
        """
        if card_ is not None:
            return self.sprite.check_card_collide(card_.sprite)
        elif pos is not None:
            return self.sprite.check_area_collide(pos)

    def get_pos(self):
        return self.sprite.pos

    def set_pos(self, pos):
        """ Sets position of the card's sprite
        :param pos: tuple with coordinates (x, y) where the top left corner of the card
                    should be placed.
        """
        self.sprite.pos = pos
        #self.back_sprite.set_pos(pos)

    def offset_pos(self, pos):
        """ Move the card's position by the specified offset
        :param pos: tuple with coordinates (x, y) of the offset to move card
        """
        self.sprite.offset_pos(pos)
        #self.back_sprite.offset_pos(pos)
