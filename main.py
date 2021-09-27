import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

#plotting the graph
fig = ff.create_distplot([data],["Math Scores"], show_hist= False)
fig.show()

###############################################################################################################################


#calculating the mean and standard deviation of the population data



###############################################################################################################################

##  code to find the mean of 100 data points 1000 times 
#function to get the mean of the given data samples
# pass the number of data points you want  as counter



# Pass the number of time you want the mean of the data points as a parameter in range function in for loop



## calculating mean and standard_deviation of the sampling distribution.





###############################################################################################################################

## findig the standard deviation starting and ending values


# plotting the graph with traces



# finding the mean of the first data(STUDENTS WHO GOT TABLET WITH LEARNING MATERIAL) and plotting it on the plot.



# finding the mean of the SECOND data (STUDENTS WHO HAD EXTRA CLASSES ) and plotting it on the plot.


# finding the mean of the THIRD data (STUDENTS WHO GOT FUNSHEET) and plotting it on the plot.



#finding the z score using the formula

