import analytics

#Please modify the below functions so they fulfill the described process.
#You must use a function from analytics.py in each question to receive credit.
#There is no provided test file. You must make and submit one yourself. (check older test files for reference)


# Modify the below function such that it takes in a list of prices and returns that list with 15% added value
def process_expenses(rawPrices):
    processedPrices = [round(n * 1.15, 2) for n in rawPrices]
    return processedPrices


# Modify the below function such that it asks the user for n scores and then returns the highest score and the average score of the list.
def analyze_scores(n):
    if n <= 0:
        raise ValueError("Number of scores must be greater than zero.")

    scores = []

    for i in range(n):
        score = float(input(f"Enter score {i + 1}: "))
        scores.append(score)

    highest_score = max(scores)
    average_score = sum(scores) / n

    return highest_score, average_score


# Modify the below function such that it takes in a list of strings and returns that list with all spaces removed
#and all letters lower case.
def sanitize_usernames(strings):
    return [s.replace(" ", "").lower() for s in strings]


# Modify the list such that it takes in a list as an argument and returns a version of the list with all values over 100.
def identify_outliers(li):
    returnlist = []
    for i in li:
        if i > 100:
            returnlist.append(i)
        else:
            continue
    return returnlist


# Modify the below function such that it takes in a list of items and asks the user for an item to search for.
#Sanitize the list to only be lower case worsd with no extra spaces
#Then return the location of the word using binary search if the list is in order and linear search if it is not.
#example items = ["  Apple", "Banana ", "  CHERRY  ", " date "]
def search_and_report(items):
    sanitized_items = [item.strip().lower() for item in items]

    target = input("Enter item to search for: ").strip().lower()

    is_sorted = sanitized_items == sorted(sanitized_items)

    if is_sorted:
        left, right = 0, len(sanitized_items) - 1

        while left <= right:
            mid = (left + right) // 2

            if sanitized_items[mid] == target:
                return mid
            elif sanitized_items[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
    else:
        for index, item in enumerate(sanitized_items):
            if item == target:
                return index

        return -1