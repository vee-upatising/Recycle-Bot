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
* Crane arm with camera connected to Rasberry Pi
* Servo motor with rotating stick<br/>
![Platform](https://i.imgur.com/4Z5y41F.jpg)

# Machine Learning Model Selection
![model](https://i.imgur.com/jTY9cpw.png)<br/>
* Best Performing Model Was Support Vector Machine With An Out Of Sample Accuracy of 0.992

# Linear Model Using Hinge Loss
![linear](https://i.imgur.com/q7s3rRz.png)<br/>
* The Best Performing Model Was Using Regularization Constant = 0.01<br/>
* Testing Accuracy Using 5-Fold Cross Validation = 0.9529230769230768

# Logistic Regression
![logistic](https://i.imgur.com/dhcOeSL.png)<br/>
* The Best Performing Model Was Using Regularization Constant = 10<br/>
* Testing Accuracy Using 5-Fold Cross Validation = 0.9446153846153846

# Support Vector Machine
![SVM](https://i.imgur.com/fJCgv1U.png)<br/>
* The Best Performing Model Was Using Regularization Constant = 0.01<br/>
* Testing Accuracy Using 5-Fold Cross Validation = 0.992

# Decision Tree
![Tree](https://i.imgur.com/YyWqpTD.png)<br/>
* The Best Performing Model Was Using Max Tree Depth = 9<br/>
* Testing Accuracy Using 5-Fold Cross Validation = 0.9763076923076923

# Convolutional Neural Network Design
![CNN](https://i.imgur.com/nBVDjjw.png)

# Forward Propagation Visualization
![Forward Prop](https://raw.githubusercontent.com/vee-upatising/Recycle-Bot/master/CNN%20Forward%20Propagation.gif)

# Training
![loss](https://i.imgur.com/urBS8MK.png)<br/>
* Using Hinge Loss And Adamax Optimizer

# Testing Accuracy
![testing](https://i.imgur.com/qggApQM.png)

# Test
The output of the model is a positive / negative number based on which class the image belongs to with the magnitude of the number being the confidence of the model.<br/>
![test1](https://i.imgur.com/nIcemHx.png)
![test2](https://i.imgur.com/TvuEe14.png)
