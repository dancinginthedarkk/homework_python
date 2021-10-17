def formatting(arr, position, n, mark):

    text = ""
    if position == "center":
        position = "^"
    elif position == "right":
        position = ">"
    elif position == "left":
        position = "<"
    for i in arr:
            text += (("{0:" + mark + position + str(n) + "s}").format(i))
            text += "\n"
    return text

arr = input("enter the text: ").split()
position = input("center, left or right? ")
n = int(input("enter the page size: "))
mark = input("enter a mark: ")

print(formatting(arr, position, n, mark))
