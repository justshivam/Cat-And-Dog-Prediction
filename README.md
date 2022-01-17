# Cat And Dog Prediction

This project uses Transfer Learning to train a Model which classifies Cats and Dogs. The [Cat and Dog Dataset](https://www.kaggle.com/tongpython/cat-and-dog) from kaggle is used to train the model. The Two Models used in this projects are Resnet50 and MobilenetV2. Accuracy of Resnet50 Model is 96.63%. Accuracy of MobilenetV2 Model is 73.58%.

## How to run?

You need python installed on your system. You can download adn install it from [here](https://www.python.org/). After installing python, follow these steps:

### On Windows:

- Open the `cmd` in the working dictionary.
- Type `python -m venv venv` to create a vitual environment.
- Type `call venv\Scripts\activate.bat` to activate the virtual environment.
- Type `pip install -r requirements.txt` to install all the required dependencies.
- Type `jupyter-lab` to run the jupyter-server.

### On Mac OS/Linux:

- Open the `terminal` in the working dictionary.
- Type `python3 -m venv venv` to create a vitual environment.
- Type `source ./venv/bin/activate` to activate the virtual environment.
- Type `pip3 install -r requirements.txt` to install all the required dependencies.
- Type `jupyter-lab` to run the jupyter-server.


## How to Predict?

Follow the First 4 steps from `How to run?` section. After that, use `python predict.py [.../path/to/img]` to predict the images.