from wordcloud import WordCloud
import matplotlib.pyplot as plt

#text = "C++ Java JavaScript Go Swift Assembly Mathematica Bash C# Pascal C Python HTML CSS PHP SQL Kotlin MATLAB "

text = input('Enter your string: ')

cloud = WordCloud(background_color = "white" ).generate(text)

plt.imshow(cloud)
plt.axis("off")
plt.show()
