"""

  There's an algorithms tournament taking place in which teams of programmers
  compete against each other to solve algorithmic problems as fast as possible.
  Teams compete in a round robin, where each team faces off against all other
  teams. Only two teams compete against each other at a time, and for each
  competition, one team is designated the home team, while the other team is the
  away team. In each competition there's always one winner and one loser; there
  are no ties. A team receives 3 points if it wins and 0 points if it loses. The
  winner of the tournament is the team that receives the most amount of points.


  Given an array of pairs representing the teams that have competed against each
  other and an array containing the results of each competition, write a
  function that returns the winner of the tournament. The input arrays are named
  competitions and results, respectively. The competitions array has elements in the form of [homeTeam, awayTeam]

"""

# O(n) time | O(k) space where k is the number of teams.
from itertools import chain


def tournamentWinner(competitions, results):
    # Write your code here.
    mAx = -1
    res = ""

# 	Getting list of teams from competitions list
    teams = []
    for i in competitions:
        # it appends each team name to the teams list
        teams = chain(teams, i)
    # print(list(teams))
    teams = list(set(teams))
    print(teams)  # debugging

# 	Initializing the scores map
    scores = {i: 0 for i in teams}
    # print(scores) - debugging

# 	Adding scores based on results and storing the maximum score
    for i in range(len(results)):
        if (results[i] == 1):
            # print(competitions[i][0]) - debugging
            scores[competitions[i][0]] += 3
            if (scores[competitions[i][0]] > mAx):
                mAx = scores[competitions[i][0]]
        else:
            # print(competitions[i][1]) - debugging
            scores[competitions[i][1]] += 3
            if (scores[competitions[i][1]] > mAx):
                mAx = scores[competitions[i][1]]

# 	Retrieving the team with maximum score from the map
    # for key,value in scores.items():
    # 	if(value ==mAx):
    # 		print(key)
    # 		res = key
    # return (res)

#   Shorthand - using max with key paramater.
#   Only works for 1 maximum score and not with multiple teams having same maximum score.
    return max(scores, key=scores.get)
