c = input().upper() # baaa
word_list = list(set(c)) # b,a
word_count = []
for i in word_list:  # b, a
   count = c.count(i) # 
   word_count.append(count) # 1, 3
if word_count.count(max(word_count)) > 1:
    print('?')
else:
    print(word_list[word_count.index(max(word_count))]) # word_list[word_count.index('a')] -> word_list[1]