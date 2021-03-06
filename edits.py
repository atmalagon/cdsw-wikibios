"""Plot the number of edits vs. article creation date, for male and female bios."""
import wikibios
from matplotlib import pyplot
from operator import itemgetter

figure = pyplot.figure()

# sort the data about female articles by the first edit date.
rows_female_by_firstedit = sorted(wikibios.rows_female, key=itemgetter('firstedit'))

# create empty lists, which we will fill with the median first edit dates and
# the average number of edits.
firstedit_female_medians = []
mean_edits_female_by_firstedit = []
N = 1000
i = 0
while i + N <= len(rows_female_by_firstedit):
	# take a chunk of the sorted data N rows long.
	chunk = rows_female_by_firstedit[i:i+N]
	i = i + N

	# append the median value to the holder list.
	firstedit_female_medians.append(chunk[N / 2]['firstedit'])

	# find the average number of edits by first counting
	# the total number of edits and then dividing by N
	total_edits = 0.0
	for row in chunk:
		total_edits = total_edits + row['edits']
	mean_edits = total_edits / N
	mean_edits_female_by_firstedit.append(mean_edits)

rows_male_by_firstedit = sorted(wikibios.rows_male, key=itemgetter('firstedit'))
firstedit_male_medians = []
mean_edits_male_by_firstedit = []
i = 0
while i + N <= len(rows_male_by_firstedit):
	chunk = rows_male_by_firstedit[i:i+N]
	i = i + N

	firstedit_male_medians.append(chunk[N / 2]['firstedit'])

	total_edits = 0.0
	for row in chunk:
		total_edits = total_edits + row['edits']
	mean_edits = total_edits / N
	mean_edits_male_by_firstedit.append(mean_edits)

axes = figure.gca()
axes.plot(firstedit_female_medians, mean_edits_female_by_firstedit, label='Female')
axes.plot(firstedit_male_medians, mean_edits_male_by_firstedit, label='Male')
axes.set_xlabel('First Edit Date')
axes.set_ylabel('Mean Number of Edits')
axes.legend()

figure.savefig('edits.pdf')
