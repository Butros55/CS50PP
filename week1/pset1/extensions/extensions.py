def main():
    print("File name: ", end="")
    inputu = input().lower().strip()
    print(find(inputu))

def find(inputu):
    found = False
    images = [".gif", ".jpeg", ".jpg", ".png"]
    applications = [".zip", ".pdf"]

    for image in images:
        if inputu.endswith(image):
            if inputu.endswith("jpg" or "jpeg"):
                found = True
                return "image/jpeg"
            found = True
            return "image/" + image.strip(".")

    for application in applications:
        if inputu.endswith(application):
            found = True
            return "application/" + application.strip(".")

    if inputu.endswith(".txt"):
        found == True
        return "text/plain"


    if found == False:
        return "application/octet-stream"


main()
