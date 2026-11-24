totalscore = []

for i in range (0,5):
    score = int(input(f"Enter quiz {i+1} score: "))
    totalscore.append(score)

totalledscore = sum(totalscore)
averagescore = totalledscore / 5
highestscore = max(totalscore)
lowestscore = min(totalscore)
ascendingscore = sorted(totalscore)
descendingscore = sorted(totalscore, reverse = True)
print('''QUIZ SCORE REPORT''')
print(f'Quiz scores: {totalscore}')
print(f'number of quizzes: {len(totalscore)}')
print(f'total score: {totalledscore}')
print(f'average score: {averagescore}')
print(f'highest score: {highestscore}')
print(f'lowest score: {lowestscore}')
print(f'ascending score: {ascendingscore}')
print(f'descending score: {descendingscore}')
print(f'original score: {totalscore}')
