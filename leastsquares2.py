# -*- coding: utf-8 -*-
"""LeastSquares2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18_EIgpOiqkoI9GE9dlW7WpxShm2bZnUX

#**Lab 7 - Least squares II**

Enter your code in the spaces provided. Do not change any of the variable names or function names that are already provided for you. In places where we specify the name of the return value, make sure that your code produces the a value with the correct name.
"""

# Do not edit this cell.

LabID="Lab7"

try:
  from graderHelp import ISGRADEPLOT
except ImportError:
  ISGRADEPLOT = True

from matplotlib import pyplot as plt
import numpy as np

def plot_transformation(mat):
    plt.cla()
    e1=np.array([1,0])
    e2=np.array([0,1])
    v3=e1+e2
    plot_lims=abs(np.array([[0,1],mat@e1,mat@v3,mat@e2])).max()
    trans_square=plt.Polygon([mat@e1,mat@v3,mat@e2,[0,0]],ec=(0,0,1,1),fc=(0,0,1,0.5))
    orig_square=plt.Polygon([e1,v3,e2,[0,0]],fc=(1,0,0,0.5),ec=(1,0,0,1))
    plt.gca().add_patch(trans_square)
    plt.gca().add_patch(orig_square)
    plt.axis('scaled')
    plt.ylim(-1.05*plot_lims,1.05*plot_lims)
    plt.xlim(-1.05*plot_lims,1.05*plot_lims)
    ax=plt.gca()
    ax.spines['top'].set_position(('data',0))
    ax.spines['right'].set_position(('data',0))
    ax.spines['bottom'].set_position(('data',0))
    ax.spines['left'].set_position(('data',0))
    plt.show()
    return

m=np.array([[2,1],[-2,4]])
b=plot_transformation(m)
print(b)
A=np.array([[4, 3], [2, 6]])
b=np.linalg.det(A)
print(b)

"""**Enter your name, section number, and BYU NetID**"""

# Enter your first and last names in between the quotation marks.

first_name="Miaja"

last_name="Coombs"

# Enter your Math 215 section number in between the quotation marks.

section_number="001"

# Enter your BYU NetID in between the quotation marks.  NOT YOUR BYU ID NUMBER!

BYUNetID="miajac"

"""**Import the data set**

The simplest way to load the data into Colab is to first download it as a .csv file to your local computer by clicking the link

https://drive.google.com/uc?export=download&id=1iFTaBmnv1X66BO9cV_RP7OxvUr9dNJ-l

This will allow you to download the data as a .csv file.  In the top left corner of this screen you should see a little file folder icon.  Selecting it opens a new window to the left of the notebook with three tabs: "Upload", "Refresh", and "Mount Drive".  Select "Upload". This should bring up a window that allows you to select the file "Lab7data" from your local machine, which will upload the file to your notebook. You will need to do this again if you decide to close your notebook and reopen it at a later time.

Once you've uploaded your file, convert it to a NumPy array called "signal_data" by executing the following cell.
"""

import numpy as np
import pandas as pd

df = pd.read_csv('Lab7data.csv')
signal_data=df.values
signal_data

"""**Problem 1**"""

T=signal_data[:,0]         # Replace the value of 0 with the NumPy vector that contains all of the time values in the array signal_data (the first column).

Y=signal_data[:,1]          # Replace the value of 0 with the NumPy vector that contains all of the signal amplitude values in the array signal_data (the second column).

import matplotlib.pyplot as plt

plt.plot(T, Y)
plt.show()

"""**Problem 2**"""

# This function returns the row [1,cos(t),sin(t), cos(2*t), sin(2*t) , ... , cos(n*t), sin(n*t)] of our matrix X.

def row_func(t, n):
  L = [1]  # Start with 1 as the first element
  for k in range(1, n + 1):
    L.append(np.cos(k * t))
    L.append(np.sin(k * t))
  return L
row_func(2,5)

"""**Problem 3**"""

# This function returns the matrix X, which we call the design matrix.

def design_matrix(n):
  matrix = [row_func(t, n) for t in T]
  matrix_array = np.array(matrix)
  return matrix_array
design_matrix(2)

"""**Problem 4**"""

X2=design_matrix(2)

"""**Problem 5**"""

# Replace all of the 0 values with the NumPy matrices and vectors requested in Problem 5.
transX2=np.transpose(X2)
normal_coef2=np.matmul(transX2,X2)
normal_vect2=np.matmul(transX2,Y)
beta2=np.linalg.solve(normal_coef2,normal_vect2)
print(beta2)

"""**Problem 6**"""

# This is our function which approximates the signal strength when n=2.

def f2(t):
  rf=np.array(row_func(t,2))
  dotp= np.dot(beta2,rf)
  return dotp
f2(0.75)

"""**Problem 7**"""

# Create your plot here.
vf2=np.vectorize(f2)
plt.plot(T,Y,'r.')
plt.plot(T,vf2(T),'b-')
plt.show()

"""**Problem 8**"""

a=np.matmul(X2,beta2)
b=a-Y
c=np.linalg.norm(b)
d=c**2
e=(1/629)*d
MSE2=e
print(e)   # Replace the 0 value with the mean square error you compute in Problem 8.

"""**Problem 9**"""

X1000=design_matrix(1000)
transX1000=np.transpose(X1000)
normal_coef5=np.matmul(transX1000,X1000)
normal_vect5=np.matmul(transX1000,Y)
beta1000=np.linalg.solve(normal_coef5,normal_vect5)
a1000=np.matmul(X1000,beta1000)
b1000=a1000-Y
c1000=np.linalg.norm(b1000)
d1000=c1000**2
e1000=(1/629)*d1000
MSE4=e1000
def f1000(t):
  rf=np.array(row_func(t,1000))
  dotp= np.dot(beta1000,rf)
  return dotp
f1000(0.105)

# Replace the 0 values with the values requested in Problem 9.  Remember to copy the decimal values from your practice notebook, not the formulas you used to compute them.

MSE10=0.009348751458203415

pred10=0.5087757565416515

"""**Problem 10**"""

# Replace the 0 values with the values requested in Problem 10.  Remember to copy the decimal values from your practice notebook, not the formulas you used to compute them.

MSE100=0.0014547562364331283

pred100=0.5089902472113171

"""**Problem 11**"""

# Replace the 0 values with the values requested in Problem 11.  Remember to copy the decimal values from your practice notebook, not the formulas you used to compute them.

MSE1000=1.9961406113768612e-28

pred1000=-14.192461430169898

"""**STOP!  BEFORE YOU SUBMIT THIS LAB:**  Go to the "Runtime" menu at the top of this page, and select "Restart and run all".  If any of the cells produce error messages, you will either need to fix the error(s) or delete the code that is causing the error(s).  Then use "Restart and run all" again to see if there are any new errors.  Repeat this until no new error messages show up.

**You are not ready to submit until you are able to select "Restart and run all" without any new error messages showing up.  Your code will not be able to be graded if there are any error messages.**

To submit your lab for grading you must first download it to your compute as .py file. In the "File" menu select "Download .py". The resulting file can then be uploaded to http://www.math.byu.edu:30000 for grading.
"""