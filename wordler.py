import jsonpickle
class Pattern():
    def __init__(self, pattern: list[int]):
        self.pattern = pattern
    def __eq__(self, value):
        return self.pattern == value.pattern
    def __hash__(self):
        return str(self.pattern).__hash__()
    def __repr__(self):
        return str(self.pattern)

def score(guess_str: str, answer_str: str) -> list[int]:
    GUESS_NULL = "+"
    ANS_NULL = "-"
    
    # green letters
    guess = list(guess_str)
    answer = list(answer_str)
    length = len(answer)
    assert length == len(guess)
    iterator = [i for i in range(length)]
    score = [0 for i in iterator]
    for i in iterator:
        if guess[i] == answer[i]:
            score[i] = 2
            guess[i] = GUESS_NULL
            answer[i] = ANS_NULL
    # yellow letters
    guess_set = set(guess)
    answer_set = set(answer)
    yellows = list(guess_set.intersection(answer_set))
    extras = []
    for letter in yellows:
        num = min(answer.count(letter), guess.count(letter))
        extras += [letter for i in range(num - 1)]
    for letter in yellows + extras:
        index = guess.index(letter)
        score[index] = 1
        guess[index] = GUESS_NULL
    return Pattern(score)

GUESS_LIST = "guesslist.txt"
ANSWER_LIST = "answerlist.txt"

with open(GUESS_LIST) as file:
    guess_list = file.readlines()
    guess_list = [x.strip() for x in guess_list]
with open(ANSWER_LIST) as file:
    answer_list = file.readlines()
    answer_list = [x.strip() for x in answer_list]

best_num_groups = 0
best_words = []
all_data = {}
for word in guess_list:
    groups = []
    patterns = {}
    for answer in answer_list:
        pattern = score(word, answer)
        if pattern not in patterns:
            groups.append(pattern)
            patterns[pattern] = [answer]
        else:
            patterns[pattern].append(answer)
    all_data[word] = patterns
    num = len(groups)
    if num > best_num_groups:
        best_num_groups = num
        best_words = [word]
    elif num == best_num_groups:
        best_words.append(word)

print(best_words)
print(best_num_groups)

try:
    with open("groupdata.json", "x") as f:
        f.write(jsonpickle.encode(all_data, indent=4))
except FileExistsError:
    with open("groupdata.json", "w") as f:
        f.write(jsonpickle.encode(all_data, indent=4))