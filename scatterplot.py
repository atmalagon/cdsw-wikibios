"""Make a scatterplot of male and female articles."""
import wikibios
from datetime import datetime
from matplotlib import pyplot

figure = pyplot.figure()
axes = figure.gca()

firstedits_male = wikibios.columns_male['firstedit']
birth_years_male = wikibios.columns_male['birth_year']
axes.scatter(firstedits_male, birth_years_male, alpha=0.1, c='green', linewidths=(0,), label='Male')

firstedits_female = wikibios.columns_female['firstedit']
birth_years_female = wikibios.columns_female['birth_year']
axes.scatter(firstedits_female, birth_years_female, alpha=0.1, c='orange', linewidths=(0,), label='Female')
axes.set_xlabel('Article Date')
axes.set_ylabel('Birth Year')
axes.legend()
figure.savefig('scatter.png')
