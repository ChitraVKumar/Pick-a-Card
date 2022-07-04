from jovian.pythondsa import evaluate_test_cases, evaluate_test_case


def locate_cards(cards, query):
    # Create a variable position with value 0
    position = 0

    print("Cards: ", cards)
    print("Query: ", query)
    # Set up a loop for iteration
    while position < len(cards):

        print("position: ", position)
        # Check if the element at the current position matches the query
        if cards[position] == query:
            # Answer found
            return position

        # If not increment the position and check next value
        position += 1

        # check if we have reached the end of array
        # if position == len(cards):
        # Number not found, return -1
    return -1


cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3

test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

tests = []

result= locate_cards(test['input']['cards'], test['input']['query'])
print(result)

print(result == output)

# query occurs somewhere in the middle
tests.append(test)
tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

# query is the first element in the cards
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

# query is the last element is the cards
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

# cards contain only one element which is the query
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0
})

# cards do not contain number query
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

# cards are empty
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

# numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

# query occurs multiple times. in this case returns the first occurrence of the query
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})
evaluate_test_case(locate_cards, test)

evaluate_test_cases(locate_cards, tests)
# print(tests)
card6 = tests[6]['input']['cards']
query6 = tests[6]['input']['query']

locate_cards(card6, query6)
for test in tests:
    print(locate_cards(**test['input']) == test['output'])