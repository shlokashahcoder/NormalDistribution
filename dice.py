import plotly.figure_factory as ff
import random

count=[]
diceResult = []

for i in range(1,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    sum = dice1+dice2
    diceResult.append(sum)

curve = ff.create_distplot([diceResult],["Height Distribution Curve"], show_hist=True)
curve.show()