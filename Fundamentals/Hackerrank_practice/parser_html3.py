# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class HTML_class(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            for attr in attrs:
                print(f"-> {attr[0]} > {attr[1]}")


html = ""
for _ in range(int(input())):
    html = html + input()
    html += "\n"

parser = HTML_class()
parser.feed(html)
