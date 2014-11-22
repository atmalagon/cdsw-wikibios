"""Plot the fraction of articles that are female, by birth year and first edit date."""
import wikibios
from matplotlib import pyplot
from operator import itemgetter

figure = pyplot.figure()

# sort the data by column 'birth_year'
rows_by_birth_year = sorted(wikibios.rows, key=itemgetter('birth_year'))
birth_year_medians = []
fraction_female_by_birth_year = []
N = 1000
i = 0
while i + N <= len(rows_by_birth_year):
	# take chunks of data 1000 rows at a time
	chunk = rows_by_birth_year[i:i+N]
	i = i + N

	# the middle row of each chunk will be the median birth year
	birth_year_medians.append(chunk[N / 2]['birth_year'])

	# count the number of female biography articles in each chunk
	count_female = 0.0
	for row in chunk:
		if row['gender'] == 'female':
			count_female = count_female + 1

	# find the fraction of female bio articles in the chunk and
	# add that number to a list, fraction_female_by_birt_year
	fraction_female = count_female / N
	fraction_female_by_birth_year.append(fraction_female)

# make a 2 row, 1 column subplot array, and work on the first subplot.
axes1 = figure.add_subplot(2, 1, 1)
axes1.plot(birth_year_medians, fraction_female_by_birth_year)
axes1.set_xlabel('Birth Year')
axes1.set_ylabel('Fraction Female')

rows_by_firstedit = sorted(wikibios.rows, key=itemgetter('firstedit'))
fraction_female_by_firstedit = []
firstedit_medians = []
i = 0
while i + N <= len(rows_by_birth_year):
	chunk = rows_by_firstedit[i:i+N]
	i = i + N

	firstedit_medians.append(chunk[N / 2]['firstedit'])

	count_female = 0.0
	for row in chunk:
		if row['gender'] == 'female':
			count_female = count_female + 1
	fraction_female = count_female / N
	fraction_female_by_firstedit.append(fraction_female)
# NOTE: much of the code here is the same as the first
# half of the script. We could have defined a function once
# which got the median and fraction of female articles, and
# used that instead of writing the code twice.

#work on the second subplot
axes2 = figure.add_subplot(2, 1, 2)
axes2.plot(firstedit_medians, fraction_female_by_firstedit)
axes2.set_xlabel('Article Year')
axes2.set_ylabel('Fraction Female')

figure.savefig('fractions.pdf')
