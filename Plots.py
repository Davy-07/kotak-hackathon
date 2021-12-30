# Code For Ploting Histogram

import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('review2.csv')
print(data)

  
# initializing the data
x = data['Rating']
  
# plotting the data
plt.hist(x)
  
# Adding title to the plot
plt.title("Rating")
  
# Adding label on the y-axis
plt.ylabel('Frequency')
  
# Adding label on the x-axis
plt.xlabel('Rating')
plt.hist(x, bins=25, color='green', edgecolor='blue',
         linestyle='--', alpha=0.5)

plt.savefig('hist.png')
  
plt.show()



  
