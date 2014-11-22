"""Make combined histograms of the male and female articles, by birth year and first edit date."""
import wikibios
from matplotlib import pyplot, dates

figure = pyplot.figure()

axes1 = figure.add_subplot(2, 1, 1)
birth_years_male = wikibios.columns_male['birth_year']
birth_years_female =  wikibios.columns_female['birth_year']

# histogram shows the number of articles about females/males
# as a function of the subject's birth year.
# stacked=True means the two histograms will be plotted over each other.
axes1.hist([birth_years_female, birth_years_male], bins=50, stacked=True, range=[1514, 2014])
axes1.set_xlabel('Birth Year')
axes1.set_ylabel('Articles')

axes2 = figure.add_subplot(2, 1, 2)
# convert the timestamps to floats
firstedits_male = dates.date2num(wikibios.columns_male['firstedit'])
firstedits_female = dates.date2num(wikibios.columns_female['firstedit'])

# histogram shows the number of articles about females/males
# as a function of the first edit date.
axes2.hist([firstedits_female, firstedits_male], bins=50, stacked=True, label=['Female', 'Male'])

# this syntax allows us to ask matplotlib to figure out the best format
# and locations for the tick marks and timestamp values on the x axis.
axes2.xaxis.set_major_formatter(dates.AutoDateFormatter(dates.AutoDateLocator()))
axes2.legend()
axes2.set_xlabel('Article Year')
axes2.set_ylabel('Articles')

figure.savefig('histograms.pdf')
