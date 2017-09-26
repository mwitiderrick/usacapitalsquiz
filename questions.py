import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
                'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
                'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
                'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
                'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
                'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
                'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
            'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
                'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
                'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
states = list(capitals.keys())
for quiz_num in range(35):
    random.shuffle(states)
    quiz_file = open('quiz{}'.format(quiz_num+1), 'w')
    answer_file = open('answer{}'.format(quiz_num+1), 'w')
    quiz_file.write('Name\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write(("  " * 20) + ' Quiz number ({})\n'.format(quiz_num + 1))
    for key, state in enumerate(states):
        quiz_file.write('\n')
        quiz_file.write('{} . What is the capital city of {}?\n'.format(key+1, state))
        letters = ['A', 'B', 'C', 'D']
        right_answer = capitals[state]
        wrong_answers = list(capitals.values())
        wrong_answers.remove(right_answer)
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = [right_answer] + wrong_answers
        random.shuffle(answer_options)
        for i in range(4):
            if right_answer == answer_options[i]:
                answer_file.write('{} . {}\n'.format(key + 1, letters[i]))
            quiz_file.write('{}. {}\n'.format(letters[i], answer_options[i]))
