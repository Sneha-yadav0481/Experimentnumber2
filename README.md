AIM: Write a program to implement control flow statements and looping statements in python

ALGORITHM: Cricket Players Performance Analysis

1.Start

2.Read the number of players n.

3.Repeat the following steps for each player from 1 to n:
Display the player number.

Read the runs scored.

Display the runs scored.

Read the balls faced.

Display the balls faced.

Read the number of fours.

Display the fours.

Read the number of sixes.

Display the sixes.

Read the number of wickets taken.

Display the wickets.

Read the runs conceded.

Display the runs conceded.

Read the overs bowled.

Display the overs.

Read the total catches taken.

Display the catches.

4.Calculate the Batting Strike Rate using:
bsr = (runs / Balls_faced) × 100
Display the batting strike rate.

5.Calculate the Bowling Economy Rate using:
ber = rn / ov
Display the bowling economy rate.

6.Check the batting performance:
If runs are greater than or equal to 50 and strike rate is greater than or equal to 120, assign "Excellent Batter".
Else if runs are greater than or equal to 30 and strike rate is greater than or equal to 100, assign "Good Batter".
Else if runs are greater than or equal to 20, assign "Average Batter".
Otherwise, assign "Poor Batter".

7.Check the bowling performance:
If wickets are greater than or equal to 3 and economy rate is less than or equal to 6, assign "Excellent Bowler".
Else if wickets are greater than or equal to 2 and economy rate is less than or equal to 8, assign "Good Bowler".
Else if wickets are greater than or equal to 1, assign "Average Bowler".
Otherwise, assign "Poor Bowler".

8.Check the fielding performance:
If catches are greater than or equal to 2, assign "Outstanding Fielders".
Else if catches are equal to 1, assign "Active Fielders".
Otherwise, assign "Needs Improvement".
Determine the overall performance:
If the batter is Excellent Batter and the bowler is Excellent Bowler, assign "Star All-Rounder".
Else if the batter is Good Batter and the bowler is Good Bowler, assign "Strong All-Rounder".
Else if the batter is Good Batter OR the bowler is Good Bowler, assign "Supporting All-Rounder".
Otherwise, assign "Needs Improvement".

9.Display the Batting Performance.

10.Display the Bowling Performance.

11.Display the Fielding Performance.

12.Display the Overall Performance.

13.Repeat the process until all n players have been processed.

14.Stop.
