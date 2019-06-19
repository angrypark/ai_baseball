''
import numpy as np
from itertools import combinations, permutations


score_dict = {(0, 0): 0,
              (0, 1): 1,
              (0, 2): 2,
              (0, 3): 3,
              (0, 4): 4,
              (1, 0): 5,
              (1, 1): 6,
              (1, 2): 7,
              (1, 3): 8,
              (2, 0): 9,
              (2, 1): 10,
              (2, 2): 11,
              (3, 0): 12,
              (4, 0): -1,
             }


def is_valid_format(input_string):
    if len(input_string) != 4:
        return False
    if (not input_string[0].isdigit()) | (not input_string[2].isdigit()):
        return False
    return True


def get_score(guess, answer):
    strikes = len([1 for g, a in zip(guess, answer) if g == a])
    balls = len(set(guess) & set(answer)) - strikes

    return {'guess': guess,
            'answer': answer,
            'strikes': strikes,
            'balls': balls,
            'stringify': "{}S{}B".format(strikes, balls)}

def load_tree(algo_type='crush'):
    if algo_type == 'crush':
        fname = 'treeCrush5o.txt'
    elif algo_type == 'average':
        fname = 'treeAvg5.txt'
    else:
        raise ValueError('{} is not supported'.format(algo_type))

    with open('Desktop/bcMastermind30jan2017ver3.1/bcw/{}'.format(fname), 'r') as f:
        _ = f.readline()
        data = [line.split() for line in f]
        tree = [{'id': line[0],
                 'layer': line[1],
                 'min_turns': line[2],
                 'estimate': line[3],
                 'turn': line[4] if len(line[4]) == 4 else '0' + line[4],
                 'parent_id': line[5],
                 'child': line[6:-7] + line[-6:-3] + line[-1:]} for line in data]
    return tree


def get_all_candidates():
    candidates = []
    for comb in combinations(range(10), 4):
        candidates.extend([''.join(num) for num in permutations([str(i) for i in comb])])
    return candidates


def reduce_candidates(candidates, guess, strikes, balls):
    candidates = set(candidates)
    possible = [num for num in candidates if
                get_score(guess, num)['stringify'] == '{}S{}B'.format(strikes, balls)]
    candidates = candidates & set(possible)
    return candidates


def reduce_candidates_with_multiple_answers(candidates, answers):
    for guess, (strikes, balls) in answers:
        candidates = reduce_candidates(candidates, guess, strikes, balls)
    return candidates


class Bot:
    def __init__(self):
        self.start_game()

    def start_game(self):
        self.number = np.random.choice(get_all_candidates(), 1)[0]
        self.candidates = get_all_candidates()
        self.solved = False
        self.tree = load_tree()
        self.current = self.tree[0]
        self.answers = []

    def save_answer(self, guess, strikes, balls):
        if strikes == 4:
            return False

        self.answers.append([guess, (strikes, balls)])
        next_question = self.current['child'][score_dict[(strikes, balls)]]
        try:
            self.current = self.tree[int(next_question)]
            return next_question
        except:
            return False
        return True

    def get_next_question(self):
        return self.current['turn']

    def get_final_answer(self):
        return reduce_candidates_with_multiple_answers(self.candidates, self.questions)

