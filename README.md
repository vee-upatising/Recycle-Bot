# Recycle-Bot
Using Machine Learning to Sort Trash From Recyclables on the Raspberry Pi 4. <br/>

After consulting with the UMass Office of Waste Management, I've determined that the most common item that gets improperly discarded are paper to-go cups. They are no longer recyclable after being used. <br/>
![trash](https://i.imgur.com/kAUAi2h.png) <br/>
Taken directly from their website, it is clear that The Office of Waste Management have to spend resources sorting out these commonly discarded items. <br/>

The goal is to help automate this process.

# Demo
![Recycle](https://github.com/vee-upatising/Recycle-AI/blob/master/Trash.gif)
![Recycle](https://github.com/vee-upatising/Recycle-AI/blob/master/Recycle.gif)
<br/>

# Design
The design of the Recycle Bot includes:<br/>
* A viewing platform
* Crane arm with camera connected to Raspberry Pi
* Servo motor with rotating stick<br/>
![Platform](https://i.imgur.com/4Z5y41F.jpg)

# Machine Learning Model Selection
![model](https://i.imgur.com/RoTqcjP.png)<br/>
* Best Performing Model Was Support Vector Machine With An Out Of Sample Accuracy of 99.2%

# Logistic Regression
![logistic](https://i.imgur.com/xrvqndp.png)<br/>
* The Best Performing Model Was Using Regularization Constant = 1 with L2 Penalty<br/>
* Testing Accuracy Using 5-Fold Cross Validation = 85.824111822947%<br/>
![decicion boundary](https://i.imgur.com/AB6UsMw.png)

# K-Nearest Neighbors
![KNN](https://i.imgur.com/D6Faroe.png)<br/>
* The Best Performing Model Was Using 10 Neighbors <br/>
* Testing Accuracy Using 5-Fold Cross Validation = 88.21538461538461% <br/>
![decicion boundary](https://i.imgur.com/5vPYfCr.png)

# Decision Tree
![Tree](https://i.imgur.com/YyWqpTD.png)<br/>
* The Best Performing Model Was Using Max Tree Depth = 9<br/>
* Testing Accuracy Using 5-Fold Cross Validation = 97.63076923076923%
![decisiontree](https://i.imgur.com/AmPVfXD.png)

# Support Vector Machine
![SVM](https://i.imgur.com/fJCgv1U.png)<br/>
* The Best Performing Model Was Using Regularization Constant = 0.01<br/>
* Testing Accuracy Using 5-Fold Cross Validation = 99.2%
![svm](https://i.imgur.com/sU8CgSl.png)

# Convolutional Neural Network Design
![CNN](https://i.imgur.com/mQnUptP.png)

# Forward Propagation Visualization
![Forward Prop](https://raw.githubusercontent.com/vee-upatising/Recycle-Bot/master/44.gif)
![Forward Prop 2](https://raw.githubusercontent.com/vee-upatising/Recycle-Bot/master/63.gif)

# Convolutional Filter Heat Map
![63](https://i.imgur.com/0JTGrmm.png)

# Training
* I performed 5-Fold Cross Validation on this model and the training loss over each fold is plotted below:
![loss](https://i.imgur.com/PlGAcsJ.png)<br/>
* Using Hinge Loss And Adamax Optimizer
* These five models achieved an average testing accuracy of 89.84615384615384%

# Testing Accuracy
![testing](https://i.imgur.com/qggApQM.png)

# Sample Output
The output of the model is a positive / negative number based on which class the image belongs to with the magnitude of the number being the confidence of the model.<br/>
![test1](https://i.imgur.com/nIcemHx.png)
![test2](https://i.imgur.com/TvuEe14.png)
