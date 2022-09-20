# The game rules

While the name and gameplay of QNO resemble that of the popular card game UNO, there are a lot of key differences between the two games. The QNO game will walk you through what your options are on each turn, but it is still a good idea for everyone to thoroughly read through the rules before playing for the first time.

## Setup

The game is for 2-4 players. Each player starts with five cards. The rest of the cards are placed in a Draw Pile. The top card of the Draw Pile is automatically placed in the Discard Pile, and then the game begins!

## Game Play

Let's say we have n players, for an n value between 2 and 4. Choose an ordering for the players -- who is Player 1, who is Player 2, etc.. The turn order of the game starts off in ascending order based on each player's number. So, player 1 would go first, Player 2 will follow, and we continue this trend until after Player n goes -- when we will go back to Player 1. Each player looks at his/her cards and tries to match the top card in the Discard Pile. The play has to match either by number, Symbol/Action, or two qubit quantum basis state (|00>, |01>, |10>, and |11>). For instance, if the top card on the Discard Pile has basis state |00> and number 8, then you have to either place a card with basis state |00> or a card with an 8 on it. The player can also always play a quantum gate card, which can alter the current basis state of the card in play. The cards are colored based on their quantum basis state to help players detect matching states.

If the player has no matches, then the player must draw from the Draw Pile. If the player has a matching card or a quantum gate card, the player must play one of these cards.

**Note:** The game will never begin with a quantum gate card on top. If the game starts with an Action card on top of the discard pile, that Action from the card applies and is carried out automatically. At any time, if the Draw Pile becomes depleted and no one has yet to win, the Discard Pile is shuffled and turned over to generate a new Draw Pile.

The game continues until a player has one card left. When this player plays his/her penultimate card, the game prints out "QNO!." Once a player has no cards remaining, the game is over and that player has won the game.

* Action Cards: Besides the number cards, there are several other cards that help mix up the games. These are called action or symbol cards.

  * **Reverse:** If the order of gameplay is in ascending order based on player number (e.g., Player 1 to Player 2 to Player 3,) and the Reverse card is played, then switch to descending order or vice versa.

  * **Skip:** When a player places the Skip card, the next player has to skip their turn.

  * **Draw Two:** When a player places the Draw Two card, the next player will pick up two cards, but can play their turn normally afterward.

* Quantum gate cards:

  * **X Gate:** The X gate card will apply the Pauli-X gate to the quantum state of the card on top of the discard pile. The player is able to choose to which qubit they want to apply the Pauli-X gate.

  * **H Gate:** The H gate card will apply the Hadamard gate to the quantum state of the card on top of the discard pile. The player is able to choose to which qubit they want to apply the Hadamard qate. The Hadamard gate will put the basis state into a superposition of two states. The superposition is measured to be collapsed into the basis states and the player gets to guess into which of the basis states it has collapsed. If the player guesses correctly, then the next player draws four cards. If the player guesses incorrectly, then the player must draw a single card.

  * **CNOT Gate:** The CNOT gate card will apply the CNOT gate to the quantum state of the card on top of the discard pile. The player is able to choose which qubit will be the control qubit and thus which qubit will be the target qubit.

More information on basis states, quantum gates, and superpositions can be found in the next section.

# Information about the quantum computing involved in QNO

This section contains enough quantum computing background to explain what is going on in QNO. There is way way WAY more quantum computing out there than just what occurs in this game. I hope if you enjoy QNO and this section, you seek out more knowledge in this field that I love so much!

We will start off by discussing classical computing and then talk about quantum computing in comparison.

Classical bits are the fundamental building block of classical computers. A bit is capable of storing one piece of information. It either has value 0 or 1. A bit's value can be changed by classical gates. For example, the NOT gate sends bit value 0 to bit value 1 and vice versa. There are also gates that take in multiple bits and output a single bit of information. For example, the AND gate takes in two bits of information and outputs a single bit of information. If the two bit values inputed are 1 the AND gate outputs 1 and on all three other possible inputs the AND gate will output 0. A circuit consists of multiple gates that the inputed bits will go through. We will stop our discussion of classical computing here, but it is amazing to think that these bits, gates, and circuits are the building block to our powerful and complex computers, phones, and most other electronic devices.

Quantum bits -- or qubits -- are the quantum analog to classical bits. Whereas classical bits can either have value 0 or 1, qubits can be in a combination of 0 and 1. A qubit q can be given in the form q=a|0>+b|1>, where a and b are complex values such that the sum of the squares of the magnitudes of a and b must be 1.

What do these a and b values represent? The magnitude of a squared gives the probability that when we measure q we end up with state |0> and the magnitude of b squared gives the probability that when we measure q we end up with state |1>. Because the sum of these values add up to 1, we can see that when we measure q we must end up in state |0> or in state |1>. In this game, we will only be using real values and so when we take the magnitude of a value we are really just taking its absolute value. For example, if a=1 and b=0, we have |a|^2+|b|^2=1+0=1 and so 1|0>+0|1>=|0> is the qubit value. Similarly, for a=0 and b=1, we have |1> is the qubit value. This means that the pure states 0 and 1 are possible qubit values and so qubits can have the same values as classical bits. However, for a=1/sqrt(2) and b=1/sqrt(2), we have |a|^2+|b|^2=1/2+1/2=1. Here we have a qubit value that cannot be given as a classical bit. There are infinitely many such qubits of this sort.

When neither a nor b is a 0, we say that the qubit is in a superposition of |0> and |1>. In this case, the qubit is in some combination of the two states. Superpositions of information is one of the key quantum features that allows quantum algorithms to outperform classical algorithms on certain problems.

Now let's consider a two qubit system. If we have two qubits q=a|0>+b|1> and r=c|0>+d|1>, then we have that qr can be given by ac|00>+ad|01>+bc|10>+bd|11>. We again have that the sum of the magnitudes squared of these scalar values must be 1, and that these scalar values correspond to the probability that when we measure our system qr we end up in the state the scalar is multiplying. We call |00>, |01>, |10>, and |11> basis states -- for the computational or Z basis we will be working in, in this game.

Like classical gates, quantum gates can act on single qubits or on multiple qubits. We just need quantum gates to preserve the property that the sum of magnitudes squared of the scalars yields 1. QNO employs three of the most common quantum gates. We will discuss what these gates do on basis states. Note that we will follow Qiskit's convention of right indexing. This means for state |01> we have that qubit_0 is on the right and has value 1 and qubit_1 has value 0 is on the left.

The X gate: The X gate acts only on one qubit and sends |0> to |1> and |1> to |0>. So, for example, if we are in basis state |01> and we send qubit_0 -- the right-most qubit -- through the X gate, qubit_0 switches value from 1 to 0 and we end up in basis state |00>. If we instead send qubit_1 through the X gate, we would end up in basis state |11>.

The H gate: The H gate acts only on one qubit and sends |0> to 1/sqrt(2)|0> + 1/sqrt(2)|1> and |1> to to 1/sqrt(2)|0> - 1/sqrt(2)|1>. The sign of the operator between our two states will not affect our measurement. In each of these cases, we have a 50 percent chance of ending up in state |0> and a 50% chance of ending up in state |1> after measuring our qubit. If we are in basis state |01> and we send qubit_0 through the H gate, qubit_0 switches value from |1> to to 1/sqrt(2)|0> - 1/sqrt(2)|1> and we end up in the superposition 1/sqrt(2)|00> - 1/sqrt(2)|01>. This tells us we have a 50 percent chance of ending up in basis state |00> and a 50 percent chance of ending up in state |01>. Similarly, applying the H gate to qubit_1 will give us superposition 1/sqrt(2)|01> + 1/sqrt(2)|11>. In QNO, a player who plays an H gate gets to guess which basis state we end up in after measuring the resulting superposition. The player gets heavily rewarded for guessing correctly and a tiny punishment for guessing incorrectly. This risk/reward system is for gameplay purposes only and not to represent anything that goes on with the H gate.

The CNOT gate: The CNOT gates acts on two qubits. The CNOT gate has a control qubit and a target qubit. If the control qubit is a 1, then it applies the X gate to the target qubit. If the control qubit is a 0, then it does nothing to the target qubit. The control qubit is never changed. If we are in state |01> and we apply the CNOT gate with qubit_0 being the control, then we end up in state |11>, since the control qubit is a 1 and so the target qubit then gets flipped. If qubit_1 is the control, then we stay in state |01>, since the control qubit is a 0 and so we do not change the target qubit.

QNO builds a quantum circuit corresponding to each game. This circuit ha9s two wires. The top wire corresponds to qubit_0, which is the right qubit in our |> (ket) notation and the bottom wire corresponds to qubit_1, which is the left qubit in our ket notation. The game adds: quantum gates on the wires each time we play a quantum gate card, a measurement gate on the wires each time we measure the state of our system, and adds X gates that would lead to the desired state change each time we change the state by using matching card numbers. This circuit can be printed out at the beginning or end of each term.

This is where we will stop our discussion of quantum computing. If you want to learn more about quantum computing there are a lot of great sources out there. A good place to get started would be to look at IBM's Qiskit Textbook or at their Qiskit youtube channel.

# Credits
## Code
This game is a graphical implementation of this game:
* https://github.com/Q-Philia/QNO/

It uses a modified version of this pygame_cards engine:
* https://github.com/ZBlocker655/pygame_cards
* Which is itself forked from: http://www.pygame.org/project-pygame_cards-3008-.html

## Art
* Music:
    * Author: Brandon Morris (Submitted by HaelDB)
    * https://opengameart.org/content/loading-screen-loop
    * License: [CC0](http://creativecommons.org/publicdomain/zero/1.0/)

* Winning sound:
    * Author: Fupi
    * https://opengameart.org/content/win-jingle
    * License: [CC0](http://creativecommons.org/publicdomain/zero/1.0/)

* Losing sound:
    * Author: Oiboo
    * https://opengameart.org/content/game-over-bad-chest-sfx
    * License: [CC0](http://creativecommons.org/publicdomain/zero/1.0/)
