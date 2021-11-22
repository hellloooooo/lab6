import requests
from bs4 import BeautifulSoup
from replaceall import replaceall


def print_dict(dictionary):
    keys = sorted(dictionary.keys())
    for frequency in keys:
        print("%-32s %d" % (frequency, dictionary[frequency]))


url = 'https://rozetked.me/news/20461-sony-skoro-mozhet-vypustit-oficial-nye-smennye-paneli-dlya-playstation-5'

page = requests.get(url)  

soup = BeautifulSoup(page.text, "html.parser")  

words = soup.get_text()
words = words.split(' ')
out_words = []
for word in words:
    out_word = replaceall(word, '\n', '')
    if out_word != '':
        out_words.append(out_word)

frequencies = {}
for out_word in out_words:

    if out_word not in frequencies:
        frequencies[out_word] = 1
    else:
        frequencies[out_word] = frequencies[out_word] + 1

print_dict(frequencies)

tag_frequencies = {}
link_frequencies = {}
img_frequencies = {}
for tag in soup.find_all():

    if tag.name not in tag_frequencies:
        tag_frequencies[tag.name] = 1
    else:
        tag_frequencies[tag.name] = tag_frequencies[tag.name] + 1

    if tag.name == 'a':
        if tag.name not in link_frequencies:
            link_frequencies[tag.name] = 1
        else:
            link_frequencies[tag.name] = link_frequencies[tag.name] + 1

    if tag.name == 'img':
        if tag.name not in img_frequencies:
            img_frequencies[tag.name] = 1
        else:
            img_frequencies[tag.name] = img_frequencies[tag.name] + 1

print("Tags \n")
print_dict(tag_frequencies)
print("Links \n")
print_dict(link_frequencies)
print("Images \n")
print_dict(img_frequencies)