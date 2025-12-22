# S.T.A.R.D.R.O.P by Stardrop

Roster: Alvin Sze, Kiran Soemardjo, James Sun, Jalen Chen

### Project Description:<br>
Our project aims to simulate a bartending experience using the BoozeAPI to acquire drink recipes and after customers order, the returned drink information will allow the player to click the appropriate ingredients. We thought of a short backstory that places the bar in space, and we will use the WhereTheISSAtAPI to tell the player what coordinates the bar is currently above. Since the bar is in space, we decided customers will pay in gold, which will be converted to USD using the GoldAPI, where we can also use the given historical data to match it with the ISS location at different times allowing the bar to move through time and space. Alcohol can be toggled on and off. Making drinks that the customers like will increase a hidden score of how much they like you, increasing the amount of tips you can earn. Restocking the store happens each “day” after you take the order of each customer once.

Each day you will be transported to a new time stamp. Take one order from each customer and make a satisfactory drink to earn gold coins. They will automatically be converted to USD at the current time stamp. Make great drinks to earn more tips and click the restock button to end the day.

## Install Guide:
Pre-requisites:
- python3 installed
- git installed

1. Clone repo:
```
$ git clone https://github.com/sze178/Stardrop.git
```

2. Install libraries:
```
$ pip install -r requirements.txt
```


## Launch Codes:
0. Activate your Python virtual environment
1. From the Stardrop directory, run:
```
$ python app/__init__.py
```
