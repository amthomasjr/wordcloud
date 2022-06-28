# %% All imports needed in this word cloud script
import numpy as np
from timeit import default_timer as timer
from datetime import timedelta
from PIL import Image
from pyparsing import Word
from wordcloud import ImageColorGenerator, WordCloud
from matplotlib import pyplot as plt

# %% read all contents of text file into variable named file_contents
with open('TheQuestoftheSilverFleece.txt', encoding = 'utf-8-sig') as f:
    file_contents = f.read()

# %% Function to compute frequencies of each word from the file
def compute_frequencies(file_contents):
    # Process text by removing punctuation marks and uninteresting words
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    # If your text file comes from Project Gutenberg, then you may want to
    # manually remove some of the extra information that is not part of the
    # actual story.
    uninteresting_words = [
        "the", "a", "to", "if", "is", "it", "of", "and", "or","an", "as", "i",
        "me", "my","we", "our", "ours", "you", "your", "yours", "he", "she",
        "him", "his", "her", "hers", "its", "they", "them", "their", "what",
        "which", "who", "whom", "this", "that", "am", "are", "was", "were",
        "be", "been","being", "have", "has", "had", "do", "does", "did", "but",
        "at", "by","with", "from", "here", "when", "where", "how", "all",
        "any", "both","each", "few", "more", "some", "such", "no", "nor",
        "too", "very", "can","will", "just"
    ]

    text = ""
    for char in file_contents.lower():
        if char == "-":
            text = text + " "
        if char not in punctuations:
            text = text + char
            
    # Make a list that does not contain any of the uninteresting words
    text_list = [i for i in text.split() if i not in uninteresting_words]
    
    # %% Compute frequencies of remaining words and store within dictionary
    result = {}
    for word in text_list:
        if word not in result:
            result[word] = 0
        result[word] += 1
    
    return dict(sorted(result.items(), key = lambda x: x[1], reverse = True))

# %% 
start = timer()

frequencies = compute_frequencies(file_contents)

mask = np.array(Image.open("dubois.png"))
image_colors = ImageColorGenerator(mask)
cloud = WordCloud(
    background_color = "white",
    max_words = 300,
    max_font_size = 100,
    mask = mask,
    mode = "RGBA",
)
cloud.generate_from_frequencies(frequencies)

plt.figure(figsize = [100, 100])
plt.axis("off")
plt.imshow(
    cloud.recolor(color_func = image_colors), 
    interpolation="nearest"
)

end = timer()
print(timedelta(seconds = end - start))

# %%
