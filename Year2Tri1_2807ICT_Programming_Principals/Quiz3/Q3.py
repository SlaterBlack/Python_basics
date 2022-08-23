lst = ["Your Honours degree is a direct pathway into a PhD or other research degree at Griffith",
"A research degree is a postgraduate degree which primarily involves completing a supervised project of original research",
"Completing a research program is your opportunity to make a substantial contribution to",
"and develop a critical understanding of",
"a specific discipline or area of professional practice",
"The most common research program is a Doctor of Philosophy",
"or PhD which is the highest level of education that can be achieved",
"It will also give you the title of Dr"]

word_count=dict()
for i in range(len(lst)):
    strings=lst[i].split(' ')
    for line in strings:
        if line in word_count:
            word_count[line]+=1
        else:
            word_count[line]=1
print(word_count)