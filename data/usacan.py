import csv
import matplotlib.pyplot as plt

usa = []
can = []



categories = []


with open('usacan.csv') as csvfile:
	reader = csv.reader(csvfile)

	line_count = 0

	for row in reader:
		if line_count is 0:
			#parse thtafirst row of text data out of the file
			categories.append(row)
			line_count += 1
		else:
			if row[4] == "USA":
				print("usa won")
				usa.append(row[4])

			elif row[4] == "CAN":
				print("can won")
				can.append(row[4])

			line_count += 1;

print("Medals for USA: ", len(usa))
print("Medals for CAN: ", len(can))

#plota pie chart

labels = ("USA", "CAN")

sizes = [len(usa), len(can)]
colors = ['blue', 'pink']
explode = (0.1, 0.1)
plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("USA vs. CAN")
plt.xlabel("Medals since 1924")
plt.show()