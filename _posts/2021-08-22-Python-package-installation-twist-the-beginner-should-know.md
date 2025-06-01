---
Title: Python Package Installation Twist Beginner Should Know
Author: Shuvangkar Das
Date: 2022-07-16
Alias: 
Tags: 
Status: 
---

Recently I have started working with deep learning although I don’t have that much knowledge over machine learning and neural network. The only thing I believe to be good at is programming. So switching to new programming is not that challenging for me. Also, I have a little bit of understanding of python before.

We know that there are two approaches for learning anything, the bottom down approach and the top-down approach. In the case of the bottom down approach, you will build things from the beginning, first, you will learn the theory and after that, you will learn to implement the theory. The top-down approach is exactly the opposite. you will learn how to apply or implementing the thing first and understanding the theory later or side by side. There are advantages and disadvantages of the two methods.

I had to choose the second approach. I kind of ok with that. Because in the field of deep learning and machine learning, there are a lot of examples I can find on the internet. Most of them are comprehensive and described in detail how to implement. So now I try to implement any problem on a topic and try to understand the theory behind it. It kind of helping me to feel the inner meaning of the theory.

But the problem in package management. while writing code for the deep learning problem, I had to install the libraries. Claimed to be good at googling, I am messing things up by the way. I am installing the library and checked that installation is ok but my code cannot load the library from the Jupyter notebook. So I am facing a problem with python package management. The problem with the library is that, think about a situation. You have installed module ‘X’ before. The version of module ‘X’ you installed is 1.2. Now you are installing another module ‘Y’. The module ‘Y’ is dependent on module ‘X’. But module ‘Y’ uses the 1.0 version of module ‘X. Here comes the conflict. It is difficult to handle such types of situations. If you are a newbie to python it is a very common problem for everyone. As I am a newbie and kind of figured out the dilemma, I should share my findings.

First thing you need to know about the virtual environment. So using a virtual environment, you can now separate concerns of your projects. Whenever you install a different python package it normally resides in the default location of python. In the virtual environment, all your modules will be installed on your local directory or separate directory in root. So by this way you can separate the dependencies of one project from another. There are other advantages of using a virtual environment. you can package and manage your project easily. you can create a dependency file, so anyone can run your project in the new environment. Just he/she has to put a simple command to install all the packages with the corresponding version. It is so easy to manage your project using a virtual environment.

The next thing you need to know is about python package management tools. For Python developers, two package management tools are popular. pip and conda. both of the tools are CLI-based and you can install packages using both of the tools. But you need to know where to use which tools. otherwise, you are sure to mess up everything. Just remember that Anaconda is not a package management tool. It is python distribution and conda comes with anaconda.

So I had to study these package management tools and figure out which is best suited for my deep learning projects. There is a lot of discussion on these two tools and different people use different tools for a different purposes. But For me, I had to choose conda because of few reasons.

In the

-  conda comes with Anaconda distribution and Anaconda installs a few other tools which are necessary for deep learning and machine learning type projects.
-   If I just use raw python with pip I had to install a lot of dependency for my project. Conda makes it easier to manage. Also If I am not comfortable with the command line Anaconda has GUI-based package management tools which is a good thing.
-   Moreover, I can use the pip command inside conda to install the package. But it not going to behave well all the time.

So as a newbie I was not sure about both of the tools. So whenever I need a new package I am just searching google. Most of the time google giving me the pip command to install a package. I am just copying the command and trying to install the package in the root environment of conda. Here comes the conflict.

First I am not creating a virtual environment. Second I am using pip inside conda. There are already conda commands to install any package I need. It is better to install any package using conda command inside conda cli.

So in conclusion always follow these thumb rules as a Python beginner.

1.  If you prefer to use pip with raw python that’s good.
2.  Don’t try to install any package using pip inside conda cli if you are not sure it will behave properly. look for conda command to install any package inside conda cli.
3.  Always create a virtual environment for a new project. python default has venv for creating the virtual environment and conda also has a built-in feature to create the virtual environment.

If you need to know how to manage and create a virtual environment using pip and conda follow my next blog. I will write on it in detail. Till then stay safe and share my blog and if you have any questions comment, please.




