def bet_one(one_odds, cross_odds, two_odds, bonus):
    bonus = bonus/100
    cross_bet = bonus
    cross_total = cross_bet + bonus
    bets = []
    betting =  {
            "status": 301,
            "msg": "Test other odds"
            }


    for one_bet in range(200):
        for two_bet in range(200):
            winnings_on_one = (one_bet * one_odds) - cross_bet - two_bet - one_bet
            winnings_on_cross = (cross_total * cross_odds) - one_bet  - two_bet - cross_bet
            winnings_on_two = (two_bet * two_odds) - one_bet - cross_bet - two_bet

            if winnings_on_two >= 0 and winnings_on_one > 0 and winnings_on_cross == 0:
                bets.append([winnings_on_one, winnings_on_cross, winnings_on_two, one_bet, two_bet])
                

    if bets:
        bets = sorted(bets, key=lambda x: x[0])[-1]
        betting = {
            "oneBet": bets[3]*100,
            "crossBet": cross_bet*100,
            "twoBet": bets[4]*100,
            "bonus": bonus*100,
            "winningsOnOne": bets[0]*100,
            "winningsOnCross": bets[1]*100,
            "winningsOnTwo": bets[2]*100
        }

    return betting



def bet_two(one_odds, cross_odds, two_odds, bonus):
    bonus = bonus/100
    cross_bet = bonus
    cross_total = cross_bet + bonus
    bets = []
    betting =  {
        "status": 301,
        "msg": "Test other odds"
        }


    for one_bet in range(200):
        for two_bet in range(200):
            winnings_on_one = (one_bet * one_odds) - cross_bet - two_bet - one_bet
            winnings_on_cross = (cross_total * cross_odds) - one_bet  - two_bet - cross_bet
            winnings_on_two = (two_bet * two_odds) - one_bet - cross_bet - two_bet

            if winnings_on_one >= 0 and winnings_on_two > 0 and winnings_on_cross == 0:
                bets.append([winnings_on_one, winnings_on_cross, winnings_on_two, one_bet, two_bet])
                

    if bets:
        bets = sorted(bets, key=lambda x: x[2])[-1]
        betting = {
            "status" : 200,
            "oneBet": bets[3]*100,
            "crossBet": cross_bet*100,
            "twoBet": bets[4]*100,
            "bonus": bonus*100,
            "winningsOnOne": bets[0]*100,
            "winningsOnCross": bets[1]*100,
            "winningsOnTwo": bets[2]*100
        }

    return betting

def safe_bet_one(one_odds, cross_odds, two_odds, bonus):
    bonus = bonus/100
    cross_bet = bonus
    cross_total = cross_bet + bonus
    bets = []
    betting =  {
            "status": 301,
            "msg": "Test other odds"
            }


    for one_bet in range(200):
        for two_bet in range(200):
            winnings_on_one = (one_bet * one_odds) - cross_bet - two_bet - one_bet
            winnings_on_cross = (cross_total * cross_odds) - one_bet  - two_bet - cross_bet
            winnings_on_two = (two_bet * two_odds) - one_bet - cross_bet - two_bet

            if winnings_on_two > 0 and winnings_on_one > 0 and winnings_on_cross == 0:
                bets.append([winnings_on_one, winnings_on_cross, winnings_on_two, one_bet, two_bet])
                

    if bets:
        bets = sorted(bets, key=lambda x: x[0])[0]
        betting = {
            "status": 200,
            "one_bet": bets[3]*100,
            "cross_bet": cross_bet*100,
            "two_bet": bets[4]*100,
            "bonus": bonus*100,
            "winningsOnOne": bets[0]*100,
            "winningsOnCross": bets[1]*100,
            "winningsOnTwo": bets[2]*100
        }

    return betting


def safe_bet_two(one_odds, cross_odds, two_odds, bonus):
    bonus = bonus/100
    cross_bet = bonus
    cross_total = cross_bet + bonus
    bets = []
    betting =  {
        "status": 301,
        "msg": "Test other odds"
        }


    for one_bet in range(200):
        for two_bet in range(200):
            winnings_on_one = (one_bet * one_odds) - cross_bet - two_bet - one_bet
            winnings_on_cross = (cross_total * cross_odds) - one_bet  - two_bet - cross_bet
            winnings_on_two = (two_bet * two_odds) - one_bet - cross_bet - two_bet

            if winnings_on_one > 0 and winnings_on_two > 0 and winnings_on_cross == 0:
                bets.append([winnings_on_one, winnings_on_cross, winnings_on_two, one_bet, two_bet])
                

    if bets:
        bets = sorted(bets, key=lambda x: x[2])[0]
        betting = {
            "status": 200,
            "one_bet": bets[3]*100,
            "cross_bet": cross_bet*100,
            "two_bet": bets[4]*100,
            "bonus": bonus*100,
            "winningsOnOne": bets[0]*100,
            "winningsOnCross": bets[1]*100,
            "winningsOnTwo": bets[2]*100
        }

    return betting
