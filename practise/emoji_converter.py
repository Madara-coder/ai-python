#Emoji Converter

message = input(">")
words = message.split(" ") # helps to split the message.
emojis = {
    ":)": "😂",
    ":(": "😔"
    }
output = ""

for word in words:
    output += emojis.get(word,word) + " "

print(output)