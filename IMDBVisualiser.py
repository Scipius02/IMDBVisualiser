import matplotlib
from IMDBScrapy import showratingaggregate as list(epdicts)

#showratingaggregate will be of form list[season(list[episode(dictionary)])]
#print(showratingaggregate)

print(type(epdicts))
xvals = []
yvals = []
i = 0

"""for season in showratingaggregate:
    for episode in season:
        i += 1
        xvals.append(i)
        yvals.append(episode["aggregateRating"]["ratingValue"])"""

print(xvals)
print(yvals)
