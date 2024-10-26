def check():
    file=input("File name: ").lower().strip()
    if file.endswith(".gif"):
        return "image/gif"
    elif file.endswith(".jpg") or file.endswith(".jpeg"):
        return "image/jpeg"
    elif file.endswith(".png"):
        return "image/png"
    elif file.endswith(".pdf"):
        return "application/pdf"
    elif file.endswith(".txt"):
        return "text/plain"
    elif file.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"

def main():
    result=check(cd)
    print(result)

main()
