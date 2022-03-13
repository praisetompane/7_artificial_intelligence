'''
reference:
   Eric Grimson, John Guttag, and Ana Bell. 6.0002 Introduction to Computational Thinking and Data Science. Fall 2016. Massachusetts Institute of Technology: MIT OpenCourseWare, https://ocw.mit.edu. License: Creative Commons BY-NC-SA.
'''
'''
   Generates discrete approximation of guassian/normal distribution
'''
import random, matplotlib as pylab

random.seed(1)
dist, numSamples = [], 1000000

for i in range(numSamples):
   dist.append(random.gauss(0, 100))
   
weights = [1/numSamples]*len(dist)
'''
user added: 
            [1/numSamples] => determines how much to weigh each item in the bin
         
            weights = [1/numSamples]*len(dist)
            makes y axis easy to interpret
            result: y axis should represent A FRACTION of the values of DIST
                  that feel into a particular bin
'''
v = pylab.hist(dist, bins = 100,
              weights = [1/numSamples]*len(dist))
pylab.xlabel('x')
pylab.ylabel('Relative Frequency')              
print('Fraction within ~200 of mean =',
     sum(v[0][30:70]))
