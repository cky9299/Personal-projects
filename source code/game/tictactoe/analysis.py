tictactoe problems

else if (ItemColumnNo == 1)//to account for boards of all sizes using
if (ItemColumnNo>0 || ItemColumnNo<noColumns-1).
#prob 1: ttt board is always 3x3
sol 1: imp a more efficient algo to det win/draw. method: access index to det playerturn directly.

#prob 2: EndGame(PlayerTurn);//prob: if endgame here, still need check endgame for the rest so inefficient and repetitive.
sol 2: imp sol1 using or

implementation stage
methods:
    1. assigning a value to denote playerturn and det if win via sum
    2. use if else and logical operators to det if consec row/c/d =pt
goal: choose to more efficient method.
given: 2darr  = 2d arr cont o/x/'' ie state of board innerhtml

1.
1.1 loop the 2darr, check if playerturn is o,x,'' and gen another 2d arr with corres value 1,2,0
1.2 to cal sum of each row eg new2darr[1][0]+new2darr[1][1]+new2darr[1][2], column
1.3 use switch 
to chceck win
given: 3x3 board
win con: 3 consec horizpntal,vertical or diagonal / or \ consisting of playerturn
p1=1;p2=2;empty=0
algo:
for each row:
    add em
    switch(sum):
    case 3:
        winner=p1
    case 6:
        winner=p2

2.
2.1 if 2darr[1][0]+2darr[1][1]+2darr[1][2] == 'O' || 2 more rows || 3 columns || \ || /:
    endgame('O')
total no OR used = 8

conclusion: method 2 is more efficient.
prob: gotta break the or comparison when a winner is det to avoid unnecessary comparisons
sol: since the or operator is used, wouldnt the if statement exe upon det a condition is true?
hence no furhter actions needed.

function EndGame(PlayerTurn) //print playerturn wins, set iswon to true, play sound, remove el

implemented:
    method 2 and removed old method ie inf board
