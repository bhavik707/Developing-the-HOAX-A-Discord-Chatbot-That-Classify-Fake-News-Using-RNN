# Developing-the-HOAX-A-Discord-Chatbot-That-Classify-Fake-News-Using-RNN

This project is based on classification of news using RNN-LSTM model on Discord platform. This project has used python libraries such as Pandas, Numpy, Scikit Learn, and Keras.

## Dataset Can be Access: [Data](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset)
## Installation and execution procedures for the project:

### 1. Discord Bot API configuration and python files set up

In order to use this project, Please follow below step to get Discord Bot API:

1. Sign up and login to Discord platform and Go to https://discord.com/developers/applications
2. Create New Application by clicking the button right top corner of the screen.
3. Go to your discord application and create a new server.
4. Create Bot and copy the Bot's token code.
5. Got to the OAuth2 tab and authenticate your API to add your bot to your Discord server.
6. Download both python files(Discord.py & MMmodel.py) and dataset in same directory.
7. Install all the packages required for the code provided in requirements.txt and assign roles to bot.
8. Go t0 discord.py and at the bottom of code.client.run(), put your Bot's token code that copied from step 4.
9. Now this project is ready to run.

### 2. To run the project

1. Use /TrueNews prefix before artlicle headline to get results.
2. Results will show how much percentage the news is true.

