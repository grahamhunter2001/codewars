def bowling_score(rolls):
    score = 0
    no_of_strikes = sum(rolls[i] == 10 for i in rolls)
    no_of_balls = len(rolls)
    game = 0
    i = 0
    while game != 10:
        _round = "not over"
        round_score = 0
        ball = 0
        while _round != "over":
            round_score += rolls[i]
            ball += 1
            if round_score == 10:
                if ball == 1:
                    round_score += rolls[i+1] + rolls[i+2]
                else:
                    round_score += rolls[i+1]
                _round = "over"
            if ball == 2:
                _round = "over"
            i += 1
        game += 1
        score += round_score
    return score
