
original = "The Python Software Foundation and the global Python community welcomes and encourages participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."

original = original.lower().replace(",", "").replace(".", "").replace(":", "")

frase = original.split(" ")

def select(frase):
    words = []
    for word in frase:
        if len(word) > 4:
            for letter in word:
                if letter in "python":
                    words.append(word)
                    break
    return words

print(select(frase))
print(len(select(frase)))
































