print("amogh")

def maxValue(n, rounds):
    investments=[0]*n+1  # convert long[] investments = new long[n + 1];//index starting from 1
    print(investments)
    maxInvest=0
    for contribution in rounds:
        sIndex,eIndex,amnt=contribution[0],contribution[1],contribution[2]

        i=sIndex
        while i<=eIndex:
            investments[i]=investments[i]+amnt
            max(maxInvest,investments[i])
            i=i+1

    return maxInvest



public static long maxValue(int n, List<List<int>> rounds)
{
    long[] investments = new long[n + 1];//index starting from 1
long maxInvestment = 0;

    foreach (List<int> contribution in rounds)
    {
    int startingIndex = contribution[0];
    int endingIndex = contribution[1];
    int amount = contribution[2];

        for(int start = startingIndex; start <= endingIndex; start++)
        {
            investments[start] += amount;
        maxInvestment = Math.Max(maxInvestment, investments[start]);
        }
    }

return maxInvestment;
}



