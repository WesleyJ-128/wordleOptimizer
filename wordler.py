answer = "tryst"

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
    return score

while True:
    print(score(input(), answer))
    print(answer)
