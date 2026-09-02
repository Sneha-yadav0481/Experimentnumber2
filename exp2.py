n = int(input("Enter no. of players:"))

for i in range(n):
    print("\nPlayer", i + 1)

    runs = int(input("Enter runscored: "))
    print(runs)

    Balls_faced = int(input("Enter Balls faced: "))
    print(Balls_faced)

    fours = int(input("Enter fours: "))
    print(fours)

    sixes = int(input("Enter sixes: "))
    print(sixes)

    Wickets = int(input("Enter wickets: "))
    print(Wickets)

    rn = int(input("Enter run conceded: "))
    print(rn)

    ov = int(input("Enter overs bowled: "))
    print(ov)

    ct = int(input("Enter total catches taken: "))
    print(ct)

    bsr = (runs / Balls_faced) * 100
    print("Batting Strike Rate is:", bsr)

    ber = rn / ov
    print("Bowling Economy rate is:", ber)

    if runs >= 50 and bsr >= 120:
        batter = "Excellent Batter"
    elif runs >= 30 and bsr >= 100:
        batter = "Good Batter"
    elif runs >= 20:
        batter = "Average Batter"
    else:
        batter = "Poor Batter"

    if Wickets >= 3 and ber <= 6:
        bw = "Excellent Bowler"
    elif Wickets >= 2 and ber <= 8:
        bw = "Good Bowler"
    elif Wickets >= 1:
        bw = "Average Bowler"
    else:
        bw = "Poor Bowler"

    if ct >= 2:
        fp = "Outstanding Fielders"
    elif ct == 1:
        fp = "Active Fielders"
    else:
        fp = "Needs Improvement"

    if batter == "Excellent Batter" and bw == "Excellent Bowler":
        overall = "Star All-Rounder"
    elif batter == "Good Batter" and bw == "Good Bowler":
        overall = "Strong All-Rounder"
    elif batter == "Good Batter" or bw == "Good Bowler":
        overall = "Supporting All-Rounder"
    else:
        overall = "Needs Improvement"

    print("\nBatting performance:", batter)
    print("Bowling performance:", bw)
    print("Fielding performance:", fp)
    print("Overall performance:", overall)
