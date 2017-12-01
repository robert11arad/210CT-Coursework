#Title: Doubly Linked Lists Implementation
#Author: Hintea, D.
#Date: 2017
#Availability: http://moodle.coventry.ac.uk

import re

class Node(object):
      def __init__(self, value):
          self.value=value
          self.next=None
          self.prev=None
 
class List(object):
      def __init__(self):
          self.head=None
          self.tail=None
      def insert(self,n,x):
          #Not actually perfect: how do we prepend to an existing list?
          if n!=None:
              x.next=n.next
              n.next=x
              x.prev=n
              if x.next!=None:
                  x.next.prev=x              
          if self.head==None:
              self.head=self.tail=x
              x.prev=x.next=None
          elif self.tail==n:
              self.tail=x
      def display(self):
          values=[]
          n=self.head
          while n!=None:
              values.append(str(n.value))
              n=n.next
          print (", ".join(values))
         
if __name__ == '__main__':
      #Reading the file and saving the content.
      file = open('inputfile.txt', 'r')
      text = file.read().lower()
      file.close()
      text = re.sub('[^a-z\ \']+', " ", text)
      words = list(text.split())

      #Removing words that appear more than once
      for i in words:
            times=0
            for j in words:
                  if i==j and times==0:
                        times+=1
                  elif i==j and times>=1:
                        words.remove(i)

      #Creating a dictionary where the key is the lenght of the words and the value is the word with said lenght.
      Dict={}
      for i in words:
            if (len(i) in Dict) == False:
                  Dict[len(i)]=[i]
            elif (len(i) in Dict) == True:
                Dict[len(i)].append(i)
      dictkeys=list(Dict)#Dictionary index, to be able to move easier through it.


      #Adding the elements to the Doubly Linked List and displaying them.
      for i in sorted(dictkeys):
            Dict[i]=sorted(Dict[i])
            globals()["lst"+str(i)]=List()
            for j in Dict[i]:
                  if j==Dict[i][0]:
                        globals()["lst"+str(i)].insert(None, Node(j))
                  else:
                        globals()["lst"+str(i)].insert(globals()["lst"+str(i)].tail, Node(j))
            print(str(i)+": ",end="")
            globals()["lst"+str(i)].display()
