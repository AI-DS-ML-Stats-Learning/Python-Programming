from html.parser import HTMLParser
import re

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        data_check  = data.split("\n")
        index = 0
        for i in data_check:
            index += 1
        if index == 1:
            print(">>> Single-line Comment")
            print(data)
        else:
            print(">>> Multi-line Comment")
            for i in data_check:
                print(i)
        
    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)
  

html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()