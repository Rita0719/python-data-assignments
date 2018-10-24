list1=['/Users/Rita/Desktop/assignment0/trade-wars-news1.txt','/Users/Rita/Desktop/assignment0/trade-wars-news2.txt','/Users/Rita/Desktop/assignment0/trade-wars-news3.txt','/Users/Rita/Desktop/assignment0/trade-wars-news4.txt','/Users/Rita/Desktop/assignment0/trade-wars-news5.txt']
f=open(list1[0],'r')
strings=f.read()
words=strings.split()
for word in words:
    print('{}-{}times'.format(word,words.count(word)))
    
from collections import Counter
print (Counter(words).most_common (15))
list2=Counter(words).most_common ()

headers = ['word','num']
from csv import*
import csv
with open('list.csv','w',newline='')as f:
 f_csv=csv.writer(f)
 if(headers):
    f_csv.writerow(headers)
    if(list2):
        f_csv.writerows(list2)