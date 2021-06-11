words_len = int(input())
right_stress = {}
for i in range(words_len):
    word = input()
    if word.lower() in right_stress:
        right_stress[word.lower()].add(word)
    else:
        tmp = set()
        tmp.add(word)
        right_stress[word.lower()] = tmp

text = input()
# print(right_stress)
if text:

    mistakes = len(text.split(" "))
    # print(mistakes)
    # print(text.split(" "))
    for word in text.split(" "):
        stresses = 0
        # print("word = ", word)
        # print("word.lower = ", word.lower())
        if word.lower() in right_stress:
            # print("word in dict")
            if word in right_stress[word.lower()]:
                # print("not a mistake")
                mistakes -= 1

        else:
            # print("word not in a dict")
            for ch in word:
                if ch.istitle():
                    stresses += 1
            if stresses == 1:
                # print("not a mistake")
                mistakes -= 1

    print(mistakes)
else:
    print(0)
