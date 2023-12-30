
def write_text(filename, text):
    with open(filename,mode="w",encoding="UTF-8") as file:
        file.write(text)

def get_text(filename):
    with open(filename,mode="r",encoding="UTF-8") as file:
        return file.read()
  

text = get_text("text.txt")
write_text("nums.txt", text)
print("you copy text") 