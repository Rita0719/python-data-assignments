list1=['/Users/Rita/Desktop/assignment0/trade-wars-news1.txt','/Users/Rita/Desktop/assignment0/trade-wars-news2.txt','/Users/Rita/Desktop/assignment0/trade-wars-news3.txt','/Users/Rita/Desktop/assignment0/trade-wars-news4.txt','/Users/Rita/Desktop/assignment0/trade-wars-news5.txt']
f=open(list1[0],'r')
strings=f.read()
words=strings.split()


from collections import Counter
print (Counter(words).most_common(15))