Evan Roncevich

Quick details:
R = MAX
D = Min
smallNeighborhoods.txt - 4x1 or 2x2
largeNeighborhoods.txt - 8x1 or 4x2

Republicans and Democrats tie if R goes first

Details:
This simulates gerrymandering for both district sizes.
The size of the boards are provided as mxn rectangles

The options are choosing a straight verticle line,
or some square/rectangle shape.

In the small 4x4 block, players can choose 4x1 verticle lines
or 2x2 squares.
In the large 8x8, players can choose 8x1 or 4x2.

These blocks must fit together, leaving not square sans district
The goal of the game is to get one team as many victories as
possible. I chose Republicans because they offer a more interesting
strategy than the Democrats when run.

Some features is that if a 4x2 block is chosen, we can assume
that entire column is only 4x2 blocks otherwise the board
could not be completely filled. This saves computation time.

Another feature is alpha beta pruning. The program will output
if it realizes a branch is impossible to use. This speeds it up
enormously. this will also print out the pruned branch.

To run it, do python gerrymander.py largeNeighborhood.txt.
