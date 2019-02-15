import os
from collections import Counter

text_name=input("[+] Enter the text file name = ")
text_path = os.getcwd()+"\\"+text_name+".txt" # .txt's path value.
text_file = open(text_path,"r") # .txt's open object.
text_words_lines=[]
text_words_lines=text_file.readlines() # Equal everything to text_words_lines what does including .txt
text_final=[]

for i in range(len(text_words_lines)):
   text_file_line_temp=[]
   text_file_line_temp.append(text_words_lines[i].split())
   for j in text_file_line_temp[0]:
      text_final.append(j)

count=dict(Counter(text_final))
print(count)
word_line=[]
word_count=[]
for i in count:
    word_line.append(i)
    word_count.append(count.get(i))

text_file = open(text_name+".csv", "w")

for i in word_line:
    text_file.write(i+",")

text_file.write("\n")

for i in word_count:
    text_file.write(str(i)+",")


