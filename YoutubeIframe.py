import re

def main():
    print(parse(input("HTML: ")))

def parse(iframe):
    pattern = r"^<iframe .*src=\"https?://(www\.)?youtube\.com/embed/(?P<URL>\w+)\"[^>]*></iframe>$"

    match = re.search(pattern, iframe)

    if match:
        URL = match.group("URL")
        return f"https://youtu.be/{URL}"
    else:
        return None

if __name__ == "__main__":
    main()
