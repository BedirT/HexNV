# HexNV

---

### What is it?

HexNV (Hex Notation Verifier) is a Python software for testing the Hex strategies written formally using Ryan Haywards compact stategy notations. This format uses only one player moves to specify a winning strategy (the goal). The HexNV  has two functionality; is the given strategy **Complete**, is the given strategy a **Winning** strategy. Here are some examples for the formal notations;

- b2 {b1, c1} {a3, b3} *(3x3 winning strategy)*
- a3 {a2 {a1, b1}, c1 {b2, c2 {b3, c3}}} *(3x3 winning strategy)*

The language has three components;

- **a3 a2 b1 ...** - The nodes; specifying the board coordinates
- **{ ... }** - And operator; specifying the relation in the curly bracelets to be 'and'. If **{x {y}}**, x and y gives us the strategy, meaning if player plays **x** the next move will be **y**. 
- **,** - Or operator; specifying the relation between the given nodes being 'or'. This means that the move will be either x or y in a given syntax **x, y** according to the strategy.

### Functionality, How?

*What stage is the software in, what it can and can't do.*

- **Postfix Conversion:** We first convert the given strategy to postfix. Using a modified version of Shunting-Yard.
- **Parsing Expression Tree & Converting it to Strategy:** We convert the given syntax to a strategy tree. These resulting trees are kind of tedious and huge, and since we want every possible move to be tested it makes us trouble when the board gets bigger and bigger.
- **Play:** Our agent plays the game with an opponent that tries every possible action against it. If there is an action provided in response to any opponent move until the terminal state, the given notation is **complete**. If the terminal state is a win no matter what, then the given notation is a **winning strategy**.

### Done

- Take a notation and determine if it's in valid form or not.
- Ignoring virtual connections and verify the notation if it's a win or complete. In most cases this will result in a funky conclusion because *move ordering must be specific to virtual connections which is not implemented yet.*

### How does it fail?

Since we are not accounting for virtual connections, the move ordering is making us fail. i.e. 'b2 {a1, b1} {b3, c3}' is a 3x3 winning strategy. But here the agent who follows the strategy will lose;

STG Agent - X, Arbitrary Agent - O

​		. . .

​	. X .	

. . .

​		. . .

​	. X O	

. . .

​		X . .

​	. X O	

. . .

​		X . .

​	. X O	

. . O

Here we lost the connection because the ordering was wrong (since we didn't have proper priority)

### To do and so on

- Implement VC - 1 step
- Implement VC - 2,3 steps
- Further documentation
- Use benzene and adapt for it