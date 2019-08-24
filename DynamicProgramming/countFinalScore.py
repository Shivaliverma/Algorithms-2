
def countFinalScoreWays(finalScore, individualPlayScores):
    """
    finalScore = Final Total Required
    individualPlayScore = [3,5,10]
    rtype: n (no of ways)
    """
    table = [0]*(finalScore+1)
    table[0] = 1
    for score in individualPlayScores:
        print 'Fill Table for %s'%(score)
        for i in range(score, finalScore+1):
            table[i] += table[i-score]
            print table[i]

    return table[finalScore]
