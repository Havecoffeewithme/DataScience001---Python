# author  : Percy Ratheko

# Pandas provides a high-performance tools for data manipulation and analysis. Furthermore, it
# is very effective at converting data formats and querying data out of
# databases. The two main data structures of Pandas are the series and the
# data frame. To work with Pandas, we need to import the module

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# A series in Pandas is a one-dimensional array which is labeled. You can
# imagine it to be the data science equivalent of an ordinary Python
# dictionary

series = pd.Series([10, 20, 30, 40], ['A', 'B', 'C', 'D'])

print(series['C'])
# print(series[1])
print(series.iloc[0])
print()

# converting dictionaries

my_dict = {"A" : 10,
           "B" : 22,
           "C" : 33,
           "D" : 44}

series = pd.Series(my_dict)

print(series["D"])


# the series is one dimensional , but the data frame it is NOT

data = {"name" : ["Anna", "wick", "John"],
        "Age" : [24, 33, 55],
        "Height" : [122, 140, 201]}

df = pd.DataFrame(data)

for k,v in data.items():
    print(k,v)

print()

# As you can see, without any manual work, we already have a structured
# data frame and table.
print(df)
print()

# to get a value directly
print(df["name"][2])

# just to get names only
print(df["name"])

data1 = { 'Name' : [ 'Anna' , 'Bob' , 'Charles' ,
        'Daniel' , 'Evan' , 'Fiona' ,
        'Gerald' , 'Henry' , 'India' ],
        'Age' : [ 24 , 32 , 35 , 45 , 22 , 54 , 55 , 43 , 25 ],
        'Height' : [ 176 , 187 , 175 , 182 , 176 ,
        189 , 165 , 187 , 167 ]}



dff = pd.DataFrame(data1)


print()
print(dff)
print()
# just names and age only but in a table form
print(dff[["Name","Age"]])
print()

# statistical functions


print("Prints the respective count : \n", dff.count())
print()
print("The max for our data\n", dff.max())
print()
print("The minimum age\n", dff["Age"].min())

print()
print("The max for age\n", dff["Age"].max())

print()
print("The mean for AGE and HEIGHT \n", dff[["Age", "Height"]].mean())


# APPLYING NUMPY FUNCTIONS
# Instead of using the built-in Pandas functions, we can also use the methods
# we already know. For this, we just use the apply function of the data frame
# and then pass our desired method.

print()
print(dff["Age"].apply(np.sqrt))
print()

# Iterating over data-frame types , two ways to do this.

print("Our Age : ")
for k in dff["Age"]:
    print(k)

# second way method , using iteritems()

for k , v in dff.items():
    print(k,v)

print()
print("printing iterrows : ")
for index, value in dff.iterrows():
    print(index, value)


# sorting out data - frames
# When we use functions that manipulate our data frame, we don’t actually
# change it but we return a manipulated copy.

dd = pd.DataFrame(np.random.rand(10,2),
                  index  = [1,3,5,6,2,8,9,0,4,7],
                  columns=["A","B"])

print("Sorting the index : ")
print(dd.sort_index())
print()

data_k = { 'Name' : [ 'Anna' , 'Bob' , 'Charles' ,
       'Daniel' , 'Evan' , 'Fiona' ,
       'Gerald' , 'Henry' , 'India' ],
       'Age' : [ 24 , 24 , 35 , 45 , 22 , 54 , 54 , 43 , 25 ],
       'Height' : [ 176 , 187 , 175 , 182 , 176 ,189 , 165 , 187 , 167 ]}

# with the "inplace" parameter allows us to apply the changes to the original data
kk = pd.DataFrame(data_k)
kk.sort_index()
kk.sort_values(by=["Age", "Height"],
               inplace=True)
print(kk)


# Merging two data frames

names = pd.DataFrame({
      'id' : [ 1 , 2 , 3 , 4 , 5 ],
      'name' : [ 'Anna' , 'Bob' , 'Charles' , 'Daniel' , 'Evan' ],
      })

ages = pd.DataFrame({
      'id' : [ 1 , 2 , 3, 4 , 5 ],
      'age' : [ 20 , 30 , 40 , 50 , 60 ]
      })

# Now when we have two separate data frames which are related to one
# another, we can combine them into one data frame. It is important that we
# have a common column that we can merge on. In this case, this is id .


mm = pd.merge(names, ages , on="id")
mm.set_index("id", inplace=True)

print(mm)

# It is not necessarily always obvious how we want to merge our data frames.
# This is where joins come into play. We have four types of joins.

names1 = pd.DataFrame({
'id' : [ 1 , 2 , 3 , 4 , 5 , 6 ],
'name' : [ 'Anna' , 'Bob' , 'Charles' ,
'Daniel' , 'Evan' , 'Fiona' ],
})

ages1 = pd.DataFrame({
     'id' : [ 1 , 2 , 3 , 4 , 5 , 7 ],
     'age' : [ 20 , 30 , 40 , 50 , 60 , 70 ]
})

xx = pd.merge(names1,ages1, on = 'id' , how = 'inner' )
xx.set_index( 'id' , inplace = True )
print()
print("xx-------")
print(xx)
print()

xx = pd.merge(names1, ages1, on='id', how="outer")
xx.set_index("id",inplace=True)

print(xx)
print()

# QUERYING DATA
# Like in databases with SQL, we can also query data from our data frames in
# Pandas. For this, we use the function loc , in which we put our expression.

print("Quering:\n")
print(xx.loc[xx["age"] == 30])

print("AGE GREATER THAN 20 \n", xx.loc[xx["age"] > 20])

print()
print("ONLY NAMES OF THOSE OLDER THAN 30 : \n", xx.loc[xx[ 'age' ] > 30 ][ 'name' ])

# READ DATA FROM FILES
# converting csv to data-frame
"""
df = pd.read_csv("data.csv")
df.set_index("id", inplace=True)
print(df)

"""

# converting data-frame to csv
# df = pd.DataFrame(data)
# df.to_csv("mydf.csv")

# PLOTTING THE DATA

data_o = { 'Name' : [ 'Anna' , 'Bob' , 'Charles' ,
'Daniel' , 'Evan' , 'Fiona' ,
'Gerald' , 'Henry' , 'India' ],'Age' : [ 24 , 24 , 35 , 45 , 22 , 54 , 54 , 43 , 25 ],
'Height' : [ 176 , 187 , 175 , 182 , 176 ,
189 , 165 , 187 , 167 ]}

zx = pd.DataFrame(data_o)
zx.sort_values(by=["Age","Height"])
zx.hist()
plt.show()









