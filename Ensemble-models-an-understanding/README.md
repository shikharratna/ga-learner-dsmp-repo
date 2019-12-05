### Project Overview

 This dataset was generated using HRSC nadir panchromatic image h0905_0000 taken by the Mars Express spacecraft. The images is located in the Xanthe Terra, centered on Nanedi Vallis and covers mostly Noachian terrain on Mars. The image had a resolution of 12.5 meters/pixel.

The project is an implementation for the Emsemble models to predict and classify the carter size in Mars from set of images.

The Problem statement is to classify if the instance is  a Carter or not.




### Learnings from the project

 The learning was to apply different Emsemble methods like Random forest classifier, bagging , hard voting and soft Voting.

Now I can apply and combine  different classification methods known as  Ensemble methods and suscessfully select the best of the meathod based on diffrenct cost functions.

Multiple weak learners can be combined to get a strong ensemble method through Naive aggregation and Bagging(bootstrap aggregation.




### Approach taken to solve the problem

 First we clean the data and apply some basic data wrangling to get features and targer in required form. Then we applied MinMaxScaler to data to scale the data set.

The first model we applied was Logistic Regression and get the roc auc score of 83%.

Then we applied  Decision Tree Classifier and get the roc auc score of 87%.

Then we checked for the Random forest classifier and get a score of 90%

We applied bagging technique  on the Decision Tree Classifier to check the Auc Roc Score 


We finally applied hard voting method to all 3 different classifier and got an roc auc score of 91%.

Now we can suscessfully classify a carter by looking at nasa images.


### Challenges faced

 The main challenge was to convert the images to Numpy array and to convert it to MinMaxScaler.


### Additional pointers

 This a good way to identify the images for other planets and moons in solar system using the ML methods.

Recentely debris of  Vikran lander of Chandrayan was found by a  Shanmuga Subramaniam  an indian by using the images of NASA from moon orbiter.


