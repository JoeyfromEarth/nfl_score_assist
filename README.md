# nfl_score_assist
Simulate approximate outcomes of NFL games to assess the risk behind your wager!

Grade each team's offense as you see fit (A-D). 
Set whether the team will have a costly turnover, including whether the team will create a defensive takeaway of their own!
Finally, set which team will control the time of possesion. This will finalize your prediction and simulate the outcome!

Please Note:
- this equation was established using Super Bowl era begining in 1970 to 2020
- this equation was trained on NFL games dated 2020-2024
- Consider 85% of the league offensive grades to be B or C; 
-- Reserve A, D, grade offense for noticeable outliers in PPG, Morale, and Talent Experience; these are true anomolies.

Examples:
If AWAY: Offense = B, Turnover = YES, Takeaway = NO, Win Time of Possession = NO == 22.18 points
If HOME Offense = A, Turnover = YES, Takeaway = YES, Win Time of Possision = YES == 32.77 points
-- The prediction is AWAY 22.185 | HOME 32.775
-- Real Game Final: Kansas City 22 | Philadelphia 40

If AWAY: Offense = B, Turnover = YES, Takeaway = NO, Win Time of Possession = USNSURE == 23.49 points
If HOME Offense = B, Turnover = YES, Takeaway = YES, Win Time of Possision = UNSURE == 26.45 points
-- The prediciton is AWAY 23.49 | HOME 26.45
-- Real Game Final: San Francisco 22 | Kansas City 25

