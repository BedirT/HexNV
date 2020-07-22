# HexNV
Hex Notation Verifier for Ryan Hayward's simple one player notations

### FORMAL DEFINITIONS

#### Strategy Tree

- Some set of nodes, containing the values of a player strategy, with given properties;
  - A node must have a value, each value representing;
    - An action in the game that the tree represents the strategy for.
    - Or, a pass gate (can be assumed a boolean true value) which allows the moves that are connected to it to be considered.
  - A node must have a parent node if it is not the root node.
  - If there is no valid action to take for any opponent move, then the tree is **incomplete**. 
  - If there is at least one move until the game is in a win or loss condition, then the tree is **complete**.
  - If the given strategy is resulting in a win no matter what opponent strategy is, then the tree is called a **winning strategy tree**.

#### Game Specific And/Or Tree

- Some set of nodes, containing operands and operators of certain types, with given properties;
  - Each node is;
    - Either an operand, meaning the node represents an action for the game for the player that the tree represents the strategy for.
    - Or, an operator, which has exactly two children, each of which might be an operand or an operator that continues expanding. There are two different types of operators;
      - <u>Or:</u> Meaning the children have the or relationship in between. Gives the player the chance to act either continuing from child 1 or child 2, without any superiority between the actions. One child has no obligations upon another (Once played one, the other branch is not needed to complete the game)
      - <u>And:</u> Meaning the children have the and relationship in between. Gives the player the meaning that one of the children branches must follow the other to complete the sequence, and reach the end game. No children have superiority again.
    - Have a parent, if the node is not the root node.
  - If there is no valid action to take for any opponent move, then the tree is **incomplete**. 
  - If there is at least one move until the game is in a win or loss condition, then the tree is **complete**.

