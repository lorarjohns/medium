* GitHub PR:
* CMS Link: 

# Who is this article for?
- Machine learning Python programmers who want to do deep learning projects using these frameworks. They are familiar with Python and the basics of machine learning, but I assume no background knowledge of PyTorch or TensorFlow, nor of a lot of math. (I'll peg my reader as someone who's slightly below the target audience of PyTorch's 60-minute blitz tutorial.) I'll explain the structure and math of neural networks as it is necessary to do so.

## How will this article benefit your ideal reader?

- They'll come out of it knowing how to use each framework; where to find more info on each; and with enough knowledge to choose the right one for their project. 

## What will your ideal reader be able to do at the end of your article?

- They'll come out having made a working example of useful code they can use in one of those projects, a skeleton neural network that can serve as starter code for lots of other things.

## Title Ideas

* Python Deep Learning in PyTorch vs. TensorFlow
* PyTorch vs. TensorFlow Neural Networks: Who's Smarter?

key phrase: pytorch vs. tensorflow

## What examples and/or datasets will you use (if applicable)?

- Write a simple neural net
- Possible data: Celebrity faces, image style transfer (Wiki art), fashion, presidential speeches (if text generation model)

Ideas for follow-up articles:
- Write a reusable component they can use in their Pytorch/TensorFlow project (a dataloader, a hidden layer, etc.)
- Demonstrate, e.g., Inception model in PyTorch and original TF, from the respective model [hubs](https://pytorch.org/hub/pytorch_vision_inception_v3/)
- Show training visualization using TensorBoard (compatible with both libraries)


# Outline / Main Sections

## Introduction
 *  Define the scope of the article:
         
     * The audience (deep learning/machine learning engineers)
     * The frameworks (PyTorch and Tensorflow) we're talking about
 * Introduce the use case for using a deep learning library/framework
     * To build a neural network in idiomatic python
     * Explain "tensors", the core data type of both PyTorch and TensorFlow 

## Pytorch vs. TensorFlow: Comparing Libraries
 * TensorFlow 
     * Name, origins, and core characteristics
         * Google; translated for python from C++
         * lots of low-level building blocks
     * Popularity over time
         * Reputation for being more production than research, but not necessarily true
     * Keras and TF
         * What is Keras
         * Keras is the recommended way to use TF 2.0 (became more tightly integrated in response to PyTorch's user-friendlier, layer-basedprogramming design)
     * TF 1.x vs. TF 2.0
         * Backwards incompatibility and migrating code
         * Explain TF's static graph in relation to production performance andengineering concerns
         * In TF 2.0, pre-define computational graph or use immediate executionautodifferentiation 'eager mode' (inspired by PyTorch)
     * Fun facts / extra features
         * Dedicated Google Cloud Platform service for distributed model execution
         * Lots of different APIs (e.g., one for scikit-learn)
         * Many platforms and devices - tensorflow lite, tensorflow.js, tensorflowserving...
         * Keras makes it very easy to get a model prototyped quickly
         * Widely used; TF Hub is a great resource
         * Has adopted some of PyTorch's best features (e.g. autodiff by default)
     * Gotchas
         * Code written with TF 1.x will not run under 2.0 -- lots of research paper repos that are hard to reproduce; easy to mess up your dependencies if you aren't careful about your virtual environments
         * Fairly hard to debug, partly due to the static graph and the source code for TF; can be frustrating
     
 * PyTorch
     * Name, origins, and core characteristics
         * Facebook; extension of torch from Lua
         * high-level, Pythonic, expressive, but not just a Python wrapper
         * popular misconception: not a framework (no inversion of control)
     * Popularity over time
         * Reputation for being more research than production, but rapidly gainingusers
     * PyTorch and Python
         * Written to have the production optimization of TF while making neuralnetworks easier to write
         * Can write custom layers directly in Python but execute on GPU
         * Native tensors are compatible with numpy, and it's easy to convert backand forth
     * "Eager mode" dynamic computation graph
         * Autodifferentiation - automatically calculates the gradient offunctions defined in torch.nn for backpropagation 
         * Lets you run a neural net as you build and facilitates easierconstruction of conditionals within the net
     * Fun facts / extra features
         * Has a C++ API
         * Can also use Tensorboard for visualization
         * Easier to debug
         * fast.ai API
     * Gotchas
         * Less support for model serving in production
         * Potentially fewer resources overall for documentation, learning, etc.
         * The fast.ai API takes away a lot of the decisions/details you mightwant to make in building a model
 * Which one should I use?
     * It depends!
     * But it probably pays to know both

## Implementing a simple neural network in TensorFlow

* Install dependencies and load data
* Preprocess and split data
* Define the computational graph
    * Input layer: Define activation, size, shape, normalization
    * Define deep layers
    * Define output layer with softmax activation
* Inspect the model
    * Summarize
* Add a loss function, an optimizer, and metrics
* Train the model on the training data
    * (Visualize training with Tensorboard)
    * Pass the validation data as a parameter/evaluate the model 
* Use the model to perform inference

## Implementing a simple neural network in PyTorch

* Install dependencies and load data
* Preprocess and split data
* Define the model type, then insert layers
    * Input layer and parameters
    * Dense layers and parameters
    * Output layer and parameters
* Inspect the model
    * Summarize
* Define loss and optimizer
* Train the model on the training data
    * Define the metric in Python
    * Write the training loop
* Evaluate the model
    * With your metric/statistics
    * With model.eval()
* Use the model to perform inference

## Conclusion

* Recap: Tensorflow vs. PyTorch
    * Similarities and Differences
    * Pros and Cons
* Recap: What we built and how the process differed
    * Different ways to load and process data
    * Different default behavior of nn.Linear (You need to specify nonlinearitiesseparately -- nice clean illustration of the math behind why a neural networkworks, and isn't just a linear transformation.)
    * Calling model.fit() to train and evaluate versus writing a training loopfor forward and backward propagation, then model.eval()

## Other helpful RP articles/videos you could link to

* [Practical Text Classification With Python and Keras](https://realpython.com/python-keras-text-classification/)
* [Setting Up Python for Machine Learning on Windows](https://realpython.com/python-windows-machine-learning-setup/)
* [Pure Python vs NumPy vs TensorFlow Performance Comparison](https://realpython.com/numpy-tensorflow-performance/)
* [Logistic Regression in Python](https://realpython.com/logistic-regression-python/)