from html.parser import HTMLParser

# 1. Create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for attr in attrs:
            # attrs is a list of tuples: (attribute_name, value)
            print(f"-> {attr[0]} > {attr[1]}")

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        # This handles self-closing tags like <br /> automatically!
        print(f"Empty : {tag}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

# 2. Read the input code
n = int(input())
html_code = ""
for _ in range(n):
    html_code += input() + "\n"

# 3. Instantiate your parser and feed it the code
parser = MyHTMLParser()
parser.feed(html_code)

