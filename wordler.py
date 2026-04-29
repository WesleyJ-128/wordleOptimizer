import jsonpickle
from copy import copy
import Pattern

def score(guess_str: str, answer_str: str) -> Pattern:
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
    return Pattern.Pattern(score)

GUESS_LIST = "guesslist.txt"
ANSWER_LIST = "answerlist.txt"

def generate_word_data(guess_list, answer_list):
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
        print(word)
    
    return (all_data, best_num_groups, best_words)

# with open(GUESS_LIST) as file:
#     guess_list = file.readlines()
#     guess_list = [x.strip() for x in guess_list]
# with open(ANSWER_LIST) as file:
#     answer_list = file.readlines()
#     answer_list = [x.strip() for x in answer_list]

# all_data = generate_word_data(guess_list, answer_list)[0]

# with open("guessdata.json", "x") as f:
#         f.write(jsonpickle.encode(copy(all_data), indent=4))




with open("groupdata2.json", "r") as f:
    word_dict = jsonpickle.decode(f.read())

while True:
    guess = input("Enter your guess: ")
    raw_pattern = input("Enter colors (g for green, y for yellow, x for none): ")
    if len(guess) != 5 or len(raw_pattern) != 5 or set(raw_pattern) != {"g", "y", "x"}:
        print("Invalid guess or clue pattern")
        continue
    pattern = str(list(raw_pattern.replace("g", 2).replace("y", 1).replace("x", 0)))
