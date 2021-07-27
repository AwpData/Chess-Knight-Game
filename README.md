# Chess-Knight-Game
Knight's Tour Challenge programmed using <a href="https://en.wikipedia.org/wiki/Knight%27s_tour#Warnsdorff's_rule">Warnsdorff's Rule</a>
<h1> Knight's Tour Challenge </h1>
<li> Set a custom board size (At least 5 x 5 for guarenteed win)</li>
<li> Try to have the knight touch every space with no backtracking! </li>
<li> Use the auto-solver to find a solution to the puzzle </li>

<h2> Guide </h2>
An <b>X</b> denotes the current knight position <br>
<b>Asterisks (*)</b> denote already visited places <br>
<b>Numbers</b> denote the possible places you can move and the number of valid spots there are from that place

<h2>Example</h2>

```
 ------------------
5| __ __ __ __ __ |
4|  * __  5 __ __ |
3| __ __  *  5 __ |
2| __  X __ __ __ |
1| __ __ __  1 __ |
 ------------------
    1  2  3  4  5
Good moves (#): [[4, 3], [4, 1], [3, 4]]
Visited squares (*): [[3, 3], [1, 4], [2, 2]]
Current Player Pos (X): [2, 2]
 ```

<h2>Auto-Solver</h2>
<b>WARNING:</b> Anything above 5x5 may take a very long time depending on your computing power <br>

```
Enter your board dimensions
6 6
Enter the knight's starting position
1 2
Do you want to see a solution to the puzzle? (y/n) y

Found solution in 51.98 seconds!
 ---------------------
6|  9  6  11  22  25  4 |
5|  12  21  8  5  32  23 |
4|  7  10  33  24  3  26 |
3|  20  13  2  29  16  31 |
2|  1  34  15  18  27  36 |
1|  14  19  28  35  30  17 |
 ---------------------
    1  2  3  4  5  6
```
