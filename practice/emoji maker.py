def emoji_maker(message):
    words = message.split(' ')
    emojis = {
        ":)": "mood 😊",
        ":(": "mood ☹",
        "?": "mood'not sure' "
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_maker(message))
