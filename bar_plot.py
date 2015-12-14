import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

def plotBar(lst, title, ylabel, topN):
    x_points = list()
    y_points = list()

    for item in lst:
        x_points.append(item[0])
        y_points.append(item[1])

    ## necessary variables
    ind = np.arange(topN)             # the x locations for the groups
    width = 0.35                      # the width of the bars
    
    ## the bars
    rects1 = ax.bar(ind, y_points, width, color='blue', edgecolor = 'yellow')
    
    # axes and labels
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(ind+width/2)
    xtickNames = ax.set_xticklabels(x_points)
    plt.setp(xtickNames, rotation=45, fontsize=10)    
    plt.show()
