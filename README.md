# BonusBetApi
Why lose money when it's so easy to win.

If you feel good about the team with the lowest odds then I suggest you use this endpoint  
http://ec2-3-134-244-81.us-east-2.compute.amazonaws.com/:5000/bet

If you want to be sure to win a medium amount of money regardless if the team with lowest odds or highest odds win then I suggest you use this endpoint  
http://ec2-3-134-244-81.us-east-2.compute.amazonaws.com/:5000/safebet

To use this system you always bet the bonus*2 on X, the X will give you your money back.  
  
Input:  
{  
  "1": odds_for_1 (FLOAT),  
  "X": odds_for_X (FLOAT),  
  "2": odds_for_2 (FLOAT),  
  "bonus": bonus_to_bet (INT)  
}  
