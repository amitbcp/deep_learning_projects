# **Behavioral Cloning Project** 
---
The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road
* Summarize the results with a written report


[//]: # (Image References)

[image1]: ./output_images/architecture.png "Model Visualization"
[image2]: ./output_images/original_dataset_distribution.png "Grayscaling"
[image3]: ./output_images/augmented_dataset_distribution.png "Recovery Image"
[image4]: ./examples/augmented_dataset_distribution_v1.png "Recovery Image"
[image5]: ./examples/placeholder_small.png "Recovery Image"
[image6]: ./examples/placeholder_small.png "Normal Image"
[image7]: ./examples/placeholder_small.png "Flipped Image"

---
### Model Architecture and Training Strategy

#### 1. An appropriate model architecture has been employed

The model architecture was inspired from NVIDIA to a certain extent but later with the help of the results, it could be seen that even a slightly simpler model works good.

The model is defined in the ```model.py``` script. It could be seen that the script has two function with the only difference in terms of addition of Dropout to make reduce overfitting.
The architecture has the following characteristics. -
  1. The Kernels used were 5x5 & 3x3. The depth size keeps on increasing from 24-36-48-64 till the end in the given order.
  2. RELU has been used as the Neural Network Activation  function to add non-linearity.
  3. Dropout is included in the last dense layers to avoid overfitting of the model.
  4. It should also be noted that no Max-Pool or Avg-Pool layers were used. Instead strides of 2 was used to reduce the dimensionality & parameters in the network.
  5. For loss , Mean Squared Error was used and, ADAM's optimizer for backprogation and convergence of the model.

#### 2. Attempts to reduce overfitting in the model

It was observed that the model started overfitting on the dataset highly on increasing the number of epoch's, i.e. training loss kept on decreasing while validation loss remained same.
The methods used for the same were -
  1. The entire dataset was divided into two separate-parts. Training/Validation which were kept separate. The division was 80%-20% for Training-Validation.
  2.Tracking Loss across the training over both training data-set & validation-set
  3. Dropout was used in the fully connected layers of the model.
Finally the model was tested by running it through the simulator and ensuring that the vehicle could stay on the track.

#### 3. Model parameter tuning

The model used an adam optimizer, so the learning rate was tuned automatically during the training.

#### 4. Appropriate training data

  1. Training data was chosen to keep the vehicle driving on the road. I used a combination of center lane driving, recovering from the left and right sides of the road.
  2. Apart from using only the center camera image, the images from the left/right camera was used for trainig. The steering angle was accordingly adjusted for the same , so the the car recovers if it moves to much in a particular direction going off the road.



### Model Architecture and Training Strategy

#### 1. Solution Design Approach

The overall strategy for deriving a model architecture was to ...

My first step was to use a convolution neural network model similar to the ... I thought this model might be appropriate because ...

In order to gauge how well the model was working, I split my image and steering angle data into a training and validation set. I found that my first model had a low mean squared error on the training set but a high mean squared error on the validation set. This implied that the model was overfitting. 

To combat the overfitting, I modified the model so that ...

Then I ... 

The final step was to run the simulator to see how well the car was driving around track one. There were a few spots where the vehicle fell off the track... to improve the driving behavior in these cases, I ....

At the end of the process, the vehicle is able to drive autonomously around the track without leaving the road.

#### 2. Final Model Architecture

The final model architecture (model.py lines 18-24) consisted of a convolution neural network with the following layers and layer sizes ...

Here is a visualization of the architecture (note: visualizing the architecture is optional according to the project rubric)

![alt text][image1]

#### 3. Creation of the Training Set & Training Process

For the training data, I used the default data provided by Udacity as using it along with Data Augmentation techniques, I was able to train the network pretty well.

Then I repeated this process on track two in order to get more data points.

To augment the data sat, I also flipped images and angles thinking that this would ... For example, here is an image that has then been flipped:

![alt text][image6]
![alt text][image7]

Etc ....

After the collection process, I had X number of data points. I then preprocessed this data by ...


I finally randomly shuffled the data set and put Y% of the data into a validation set. 

I used this training data for training the model. The validation set helped determine if the model was over or under fitting. The ideal number of epochs was Z as evidenced by ... I used an adam optimizer so that manually training the learning rate wasn't necessary.
