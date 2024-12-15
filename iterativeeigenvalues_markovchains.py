# -*- coding: utf-8 -*-
"""IterativeEigenvalues_MarkovChains

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZIM8bNFzaVKWHaiXMm43t3BoeYdu1jCG

#**Lab 9 - Iterative eigenvalues and Markov chains**

Enter your code in the spaces provided. Do not change any of the variable names or function names that are already provided for you. In places where we specify the name of the return value, make sure that your code produces the a value with the correct name.
"""

# Do not edit this cell.

LabID="Lab9"

try:
  from graderHelp import ISGRADEPLOT
except ImportError:
  ISGRADEPLOT = True

"""**Enter your name, section number, and BYU NetID**"""

# Enter your first and last names in between the quotation marks.

first_name="Miaja"

last_name="Coombs"

# Enter your Math 215 section number in between the quotation marks.

section_number="001"

# Enter your BYU NetID in between the quotation marks.  NOT YOUR BYU ID NUMBER!

BYUNetID="miajac"

"""**Import NumPy**"""

import numpy as np

"""**Problem 1**"""

# This function approximates the dominant eigenvector of our matrix A.

def evect_approx1(x_0,k):
  A = np.array([[1, 1], [2, 0]])
  x_k = x_0
  for _ in range(k):
    x_k = np.dot(A, x_k)
  return x_k
evect_approx1(np.array([1,9]),10)

"""**Problem 2**"""

# This function approximates the dominant eigenvalue of our matrix A.

def eval_approx1(x_0,k):
  A = np.array([[1, 1], [2, 0]])
  x_k = x_0
  for _ in range(k+1):
    x_k_plus_1 = np.dot(A, x_k)
    lambda_1_estimate = x_k_plus_1[0] / x_k[0]
    x_k = x_k_plus_1
  return lambda_1_estimate
eval_approx1(np.array([1,9]),10)

"""**Problem 3**"""

# This function approximates the dominant eigenvalue and eigenvector of our matrix A using the normalized iterative process.

def norm_evect_approx1(x_0,k):
  A = np.array([[1, 1], [2, 0]])
  x_k = x_0
  for _ in range(k):
    x_k_prev = x_k
    w_k = np.dot(A, x_k)
    x_k = w_k / np.linalg.norm(w_k)
  lambda_1_estimate = w_k[0] / x_k_prev[0]
  return x_k, lambda_1_estimate
norm_evect_approx1(np.array([1,9]),10)

"""**Problem 4**"""

# This function approximates the dominant eigenvalue and eigenvector of an arbitrary matrix using the process described in Problem 4.

def norm_approx_gen(M,x_0,k):
  x_k = x_0
  for _ in range(k):
    x_k_prev = x_k
    w_k = np.dot(M, x_k)
    x_k = w_k / np.max(np.abs(w_k))
  lambda_estimate = w_k[0] / x_k_prev[0]
  return x_k, lambda_estimate

"""**Problem 5**"""

# This function approximates the dominant eigenvalue and eigenvector of an arbitrary matrix using the Rayleigh quotiend as described in Problem 5.

def ray_quotient(M,x_0,k):
  x_k, _ = norm_approx_gen(M, x_0, k)
  lambda_estimate = np.dot(x_k, np.dot(M, x_k)) / np.dot(x_k, x_k)
  return lambda_estimate
ray_quotient(np.array([[2,4,6],[4,8,0],[1,2,9]]),np.array([1,5,-1]),10)

"""**Problem 6**"""

# Replace all of the 0 values with the vectors requested in Problem 6.
y = np.array([[3,2,-2],[-1,1,4],[3,2,-5]])
y0=np.array([1,1,1])
x_vect_3 = norm_approx_gen(y,y0,3)[0]

x_vect_4 = norm_approx_gen(y,y0,4)[0]

"""**Problem 7**"""

# This function returns the number of subscribers to the different streaming services after month k.

def subscriber_vals(x_0,k):
  P = np.array([[0.7, 0.2],
               [0.3, 0.8]])
  x_k = x_0.reshape((-1, 1))
  for _ in range(k):
    x_k = np.dot(P, x_k)
  return x_k.flatten()
subscriber_vals(np.array([95,102]),10)

"""**Problem 8**"""

# Replace all of the 0 values with the value requested in Problem 8.
result_6_months = subscriber_vals(np.array([0.6, 0.4]), 6)
netflix_subs6=result_6_months[1]

"""**Problem 9**"""

# Replace all of the 0 values with the matrix/vector/value requested in Problem 9.

trans_matrix=np.array([[0.8, 0.5, 0.3, 0.2],
                       [0.05, 0.2, 0.1, 0.1],
                       [0.1, 0.1, 0.3, 0.1],
                       [0.05, 0.2, 0.3, 0.6]])

"""**STOP!  BEFORE YOU SUBMIT THIS LAB:**  Go to the "Runtime" menu at the top of this page, and select "Restart and run all".  If any of the cells produce error messages, you will either need to fix the error(s) or delete the code that is causing the error(s).  Then use "Restart and run all" again to see if there are any new errors.  Repeat this until no new error messages show up.

**You are not ready to submit until you are able to select "Restart and run all" without any new error messages showing up.  Your code will not be able to be graded if there are any error messages.**

To submit your lab for grading you must first download it to your compute as .py file. In the "File" menu select "Download .py". The resulting file can then be uploaded to http://www.math.byu.edu:30000 for grading.
"""