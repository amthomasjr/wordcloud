# %% read contents of text file into variable named file_contents
with open('flatland.txt', encoding = 'utf-8-sig') as f:
    file_contents = f.read()

# %% Remove punctuations from the text
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

text = ""
for char in file_contents.lower():
    if char not in punctuations:
        text = text + char
    else:
        if char == '-':
            text = text + ' '

# %% Rempve uninteresting words from the text
uninteresting_words = [
    "the", "a", "to", "if", "is", "it", "of", "and", "or","an", "as", "i", 
    "me", "my","we", "our", "ours", "you", "your", "yours", "he", "she", "him",
    "his", "her", "hers", "its", "they", "them", "their", "what", "which",
    "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been",
    "being", "have", "has", "had", "do", "does", "did", "but", "at", "by",
    "with", "from", "here", "when", "where", "how", "all", "any", "both",
    "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can",
    "will", "just"]

text = text.split()

for word in uninteresting_words:
    while word in text:
        text.remove(word)

# %% Compute frequencies of remaining words and store within dictionary
frequencies = {}
for word in text:
    if word not in frequencies:
        frequencies[word] = 0
    frequencies[word] += 1

# %%
