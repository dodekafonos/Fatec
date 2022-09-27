
# Gere uma lista de palavras deste texto com split () , a seguir crie uma lista com as palavras
# que começam ou terminam com uma das letras “ python ” . Imprima a lista resultante.
# Não se esqueça de remover antes os caracteres especiais e cuidado com maiúsculas e minúsculas.

st = "The Python Software Foundation and the global Python community welcomes and encourages participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."
st = st.lower()
st = st.replace(",", "")
st = st.replace(".", "")
st = st.replace(":", "")

frase = st.split(" ")
pythonwords = []

for word in frase:
    if word[0] in "python" or word[-1] in "python":
        pythonwords.append(word)
print(pythonwords)