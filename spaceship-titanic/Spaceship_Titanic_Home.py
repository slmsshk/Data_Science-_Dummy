import streamlit as st
import UI
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Page Config
st.set_page_config('Spaceship- Dats exploration',page_icon='images\heart-exclamation_2763-fe0f.png')
UI.add_bg_from_local('images\header.png')

# Title
st.markdown(f"""<div style='color:#f2f3f4'>
<h1 style='color:#f2f3f4'>SpaceShip</h1>
<p style='color:#f2f3f4;font-weight: bolder'>Predict which passengers are transported to an alternate dimension
</p>
</div>""",unsafe_allow_html=True)

# Body
data_description="""Dataset Description
In this competition your task is to predict whether a passenger was transported to an alternate dimension during the Spaceship Titanic's collision with the spacetime anomaly. To help you make these predictions, you're given a set of personal records recovered from the ship's damaged computer system.

<div style='color:#000000;font-size:30px;text-decoration:underline'>
File and Data Field Descriptions:</div>
<ul>
<li style='color:#000000;font-size:25px;'>train.csv - Personal records for about two-thirds (~8700) of the passengers, to be used as training data.</li>

<li style='color:#000000;font-size:25px;'>PassengerId - A unique Id for each passenger. Each Id takes the form gggg_pp where gggg indicates a group the passenger is travelling with and pp is their number within the group. People in a group are often family members, but not always.

<li style='color:#000000;font-size:25px;'>- HomePlanet - The planet the passenger departed from, typically their planet of permanent residence.

<li style='color:#000000;font-size:25px;'>CryoSleep - Indicates whether the passenger elected to be put into suspended animation for the duration of the voyage. Passengers in cryosleep are confined to their cabins.</li>
<li style='color:#000000;font-size:25px;'>Cabin - The cabin number where the passenger is staying. Takes the form deck/num/side, where side can be either P for Port or S for Starboard.</li>
<li style='color:#000000;font-size:25px;'>Destination - The planet the passenger will be debarking to.</li>
<li style='color:#000000;font-size:25px;'>Age - The age of the passenger.</li>
<li style='color:#000000;font-size:25px;'>VIP - Whether the passenger has paid for special VIP service during the voyage.</li>
<li style='color:#000000;font-size:25px;'>RoomService, FoodCourt, ShoppingMall, Spa, VRDeck - Amount the passenger has billed at each of the Spaceship Titanic's many luxury amenities.</li>
<li style='color:#000000;font-size:25px;'>Name - The first and last names of the passenger.</li>
<li style='color:#000000;font-size:25px;'>Transported - Whether the passenger was transported to another dimension. This is the target, the column you are trying to predict.</li>
</ul>
<p style='color:#000000;font-size: 40px;'><u>test.csv</u><p> 
<p style='color:#000000;font-size: 20px;'>Personal records for the remaining one-third (~4300) of the passengers, to be used as test data. Your task is to predict the value of Transported for the passengers in this set.
<ul>
<li style='color:#000000;font-size:25px;'>sample_submission.csv - A submission file in the correct format.</li>
<li style='color:#000000;font-size:25px;'>PassengerId - Id for each passenger in the test set.</li>
<li style='color:#000000;font-size:25px;'>Transported - The target. For each passenger, predict either True or False.</li>
"""

UI.write(value=data_description,textalign='left',fontsize=20,fontweight='bolder',color='#fdee00')
# train=