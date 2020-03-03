# Recycle-Bot
Using Convolutional Neural Networks to Sort Trash From Recyclables on the Raspberry Pi 4. <br/>

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

# Convolutional Neural Network Design
![CNN](https://i.imgur.com/duTaHI8.png)

# Training
![loss](https://i.imgur.com/9mR32uA.png)<br/>
The model started overfitting after 8 epochs, so the model weights were restored from the end of the best epoch

# Test
![test](https://i.imgur.com/TjCkQQD.png)
