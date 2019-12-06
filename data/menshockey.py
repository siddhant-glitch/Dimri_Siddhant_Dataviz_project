import csv
import matplotlib.pyplot as plt

golds = []
silvers = []
bronzes = []


categories = []


with open('menshockey.csv') as csvfile:
	reader = csv.reader(csvfile)

	line_count = 0

	for row in reader:
		if line_count is 0:
			#parse thtafirst row of text data out of the file
			categories.append(row)
			line_count += 1
		else:
			if row[7] == "Gold":
				print("won gold!")
				golds.append(row[7])

			elif row[7] == "Silver":
				print("won silver!")
				silvers.append(row[7])

			elif row[7] == "Bronze":
				print("won bronze!")
				bronzes.append(row[7])

			line_count += 1;

print("Gold Medals: ", len(golds))
print("Silver Medals: ", len(silvers))
print("Bronze Medals: ", len(bronzes))

#plota pie chart

labels = ("Gold", "Silver", "Bronze")

sizes = [len(golds), len(silvers), len(bronzes)]
colors = ['red', 'green', 'darkgoldenrod']
explode = (0.1, 0.1, 0)
plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Medals For Men's hockey")
plt.xlabel("Medals since 1924")
plt.show()