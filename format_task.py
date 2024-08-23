team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

team1_num_str = 'В команде Мастера кода участников: %s' % team1_num
two_teams_str = 'Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num)
score_2 = 42
score_2str = 'Команда Волшебники данных решила задач: {}!'.format(score_2)
team1_time_str = 'Волшебники данных решили задачи за {}с !'.format(team1_time)
two_teams_score = f'Команды решили {score_1} и {score_2} задач.'
challenge_result = f'Результат битвы: {result}'
total_str = f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!'

print(challenge_result)