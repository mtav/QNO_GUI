#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

class Opponent:
    def __init__(self, json_profile):
        self.name = json_profile["name"]
        self.methods = list(json_profile["methods"].items())

        # disable gate playing
        self.exclude_gates = False

    def try_select_card(self, cards, top_discard, current_state):
        """Try to select a card to play from hand.
        :param cards: Opponent's hand of cards (list)
        :param top_discard: Top card on discard pile.
        :param chosen_suit: Explicitly-chosen suit (if top card is 8).
        :return: Selected card to play, or None if there are no moves.
        """
        if len(cards)>10:
            print('--------------')
            for i in cards:
                print(i)
            print('--------------')
        methods = list(self.methods)
        selected_card = None
        # suit = current_state # if top_discard.rank == 8 else top_discard.suit

        while any(methods):
            method = self.choose_method(methods)
            methods.remove(method) # So we don't choose it again.

            if method[0] == "suit":
                selected_card = self.try_select_card_by_suit(cards, current_state)
            elif method[0] == "rank":
                selected_card = self.try_select_card_by_rank(cards, top_discard.rank)
            elif method[0] == "eight":
                selected_card = self.try_select_eight(cards)
            elif method[0] == "random":
                selected_card = self.try_select_card_at_random(cards, current_state, top_discard.rank)

            if selected_card is not None: return selected_card

        return selected_card # Which ought to be None by this point.

    def getTally(self, cards, states):
        '''
        cards: cards to consider
        states: states to tally
        '''
        # Tally cards by suit.
        tally = {i:0 for i in range(0,len(states))}

        for card_ in cards:
            # if card_.suit=='Gate':
            #     s=4
            # else:
            #     s=card_.suit
            if card_.suit in states:
                state_idx = states.index(card_.suit)
                tally[state_idx] += 1

        info = 'Player card tally: '
        for state_idx, state in enumerate(states):
            if state_idx==0:
                info += f'{state}: {tally[state_idx]}'
            else:
                info += f', {state}: {tally[state_idx]}'
        info = info.strip()

        suit_with_most_cards_idx = max(tally, key=tally.get)

        print(info)
        print('suit_with_most_cards: idx:', suit_with_most_cards_idx, '->', states[suit_with_most_cards_idx], ':', tally[suit_with_most_cards_idx])

        return (info, tally, suit_with_most_cards_idx)

    def choose_suit(self, cards, possible_states):
        """Having played a gate previously, make the necessary qbit choices."""
        all_states = ["|00>", "|01>", "|10>", "|11>", "Gate"]
        (all_info, all_tally, all_suit_with_most_cards_idx) = self.getTally(cards, all_states)
        (possible_info, possible_tally, possible_suit_with_most_cards_idx) = self.getTally(cards, possible_states)
        return possible_suit_with_most_cards_idx

    def try_select_card_by_suit(self, cards, suit):
        """Try to select a card with suit that matches that of top discard.
        :param cards: Opponent's hand of cards (list)
        :param suit: Suit to match.
        :return: Selected card to play, or None if there are no moves.
        """
        # matching_cards = [card_ for card_ in cards\
        #                     if card_.suit == suit\
        #                         and card_.rank != 8]
        if self.exclude_gates:
            matching_cards = [card_ for card_ in cards if card_.suit == suit and card_.getState()!='Gate']
        else:
            matching_cards = [card_ for card_ in cards if card_.suit == suit]
        if any(matching_cards):
            return random.choice(matching_cards)

    def try_select_card_by_rank(self, cards, rank):
        """Try to select a card with rank that matches that of top discard.
        :param cards: Opponent's hand of cards (list)
        :param rank: Rank to match.
        :return: Selected card to play, or None if there are no moves.
        """
        # matching_cards = [card_ for card_ in cards\
        #                     if card_.rank == rank\
        #                         and card_.rank != 8]
        if self.exclude_gates:
            matching_cards = [card_ for card_ in cards if card_.rank == rank and card_.getState()!='Gate']
        else:
            matching_cards = [card_ for card_ in cards if card_.rank == rank]
        if any(matching_cards):
            return random.choice(matching_cards)

    def try_select_eight(self, cards):
        """Try to select an 8 card.
        :param cards: Opponent's hand of cards (list)
        :return: Selected card to play, or None if there are no moves.
        """
        if self.exclude_gates:
            return None
        matching_cards = [card_ for card_ in cards if card_.getState() == "Gate"]
        # print('----------------')
        # print('TRYING GATES!!!!')
        # for i in matching_cards:
        #     i.printInfos()
        # print('----------------')
        if any(matching_cards):
            return random.choice(matching_cards)

    def try_select_card_at_random(self, cards, suit, rank):
        """Try to select a card at random that matches that of top discard.
        :param cards: Opponent's hand of cards (list)
        :param suit: Suit to match.
        :param rank: Rank to match.
        :return: Selected card to play, or None if there are no moves.
        """
        # matching_cards = [card_ for card_ in cards\
        #                     if card_.suit == suit\
        #                         or card_.rank == rank\
        #                         or card_.rank == 8]
        if self.exclude_gates:
            matching_cards = [card_ for card_ in cards if (card_.suit == suit or card_.rank == rank) and card_.getState()!='Gate']
        else:
            matching_cards = [card_ for card_ in cards if (card_.suit == suit or card_.rank == rank)]
        if any(matching_cards):
            return random.choice(matching_cards)

    @staticmethod
    def choose_method(methods):
        total_weight = sum(i[1] for i in methods)
        choice = random.randint(1, total_weight)
        accum = 0
        for method in methods:
            accum += method[1]
            if accum >= choice:
                return method
