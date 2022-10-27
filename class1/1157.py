word = input().upper()
word_dict = {}


for alpha in word:
    if alpha in word_dict:
        word_dict[alpha] += 1
    else:
        word_dict[alpha] = 1

word_dict_rev = {v:k for k, v in word_dict.items()}
max_cnt = max(word_dict.values())

if len(list(filter(lambda x: x[1] == max_cnt, word_dict.items()))) > 1:
    print("?")
else:
    print(word_dict_rev[max_cnt])

