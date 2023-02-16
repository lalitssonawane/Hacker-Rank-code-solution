#A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.




from collections import Counter

S = input()
S = sorted(S)

FREQUENCY = Counter(list(S))

for k, v in FREQUENCY.most_common(3):
    print(k, v)