# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 12:09:57 2021

@author: user
"""


import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model =  pickle.load(open('Credit_card_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    '''
    For rendering results on HTML GUI
    '''
    # Tnput Coming
    # Numeric value
    Customer_Age = float(request.form.get('Customer_Age'))
    Dependent_count = float(request.form.get('Dependent_count'))
    Months_on_book = float(request.form.get('Months_on_book'))
    Total_Relationship_Count = float(request.form.get('Total_Relationship_Count'))
    Months_Inactive_12_mon = float(request.form.get('Months_Inactive_12_mon'))
    Contacts_Count_12_mon = float(request.form.get('Contacts_Count_12_mon'))
    Total_Revolving_Bal = float(request.form.get('Total_Revolving_Bal'))
    Total_Amt_Chng_Q4_Q1 = float(request.form.get('Total_Amt_Chng_Q4_Q1'))
    Total_Trans_Amt = float(request.form.get('Total_Trans_Amt'))
    Total_Trans_Ct = float(request.form.get('Total_Trans_Ct'))
    Total_Ct_Chng_Q4_Q1 = float(request.form.get('Total_Ct_Chng_Q4_Q1'))
    Avg_Utilization_Ratio = float(request.form.get('Avg_Utilization_Ratio'))
    
    # Featureritic values
    Gender = request.form.get('Gender')
    Education_Level = request.form.get('Education_Level')
    Marital_Status = request.form.get('Marital_Status')
    Income_Category = request.form.get('Income_Category')
    Card_Category = request.form.get('Card_Category')
    
    # Calculating Gender
    if Gender == 'Male':
        Gender_M = 1
    else:
        Gender_M = 0
    
    # Calculating Education Level
    if Education_Level == 'Doctorate':
        Education_Level_Doctorate = 1
        Education_Level_Graduate = 0
        Education_Level_High_School = 0
        Education_Level_Post_Graduate = 0
        Education_Level_Uneducated = 0
        Education_Level_Unknown = 0
    elif Education_Level == 'Graduate':
        Education_Level_Doctorate = 0
        Education_Level_Graduate = 1
        Education_Level_High_School = 0
        Education_Level_Post_Graduate = 0
        Education_Level_Uneducated = 0
        Education_Level_Unknown = 0
    elif Education_Level == 'High School':
        Education_Level_Doctorate = 0
        Education_Level_Graduate = 0
        Education_Level_High_School = 1
        Education_Level_Post_Graduate = 0
        Education_Level_Uneducated = 0
        Education_Level_Unknown = 0
    elif Education_Level == 'Post-Graduate':
        Education_Level_Doctorate = 0
        Education_Level_Graduate = 0
        Education_Level_High_School = 0
        Education_Level_Post_Graduate = 1
        Education_Level_Uneducated = 0
        Education_Level_Unknown = 0
    elif Education_Level == 'Uneducated':
        Education_Level_Doctorate = 0
        Education_Level_Graduate = 0
        Education_Level_High_School = 0
        Education_Level_Post_Graduate = 0 
        Education_Level_Uneducated = 1
        Education_Level_Unknown = 0
    else:
        Education_Level_Doctorate = 0
        Education_Level_Graduate = 0
        Education_Level_High_School = 0
        Education_Level_Post_Graduate = 0
        Education_Level_Uneducated = 0
        Education_Level_Unknown = 1
                
    #Calculating Nartial Status
    if Marital_Status == 'Married':
        Marital_Status_Married = 1
        Marital_Status_Single = 0  
        Marital_Status_Unknown = 0
    elif Marital_Status == 'Single':
        Marital_Status_Married = 0
        Marital_Status_Single = 1 
        Marital_Status_Unknown = 0
    else :
        Marital_Status_Married = 0
        Marital_Status_Single = 0 
        Marital_Status_Unknown = 1
        
        # Calculating Income Category
    if Income_Category == '40K-60K':
        Income_Category_40_60 = 1 
        Income_Category_60_80 = 0
        Income_Category_80_120 = 0
        Income_Category_Less_than_40 = 0
        Income_Category_Unknown = 0
    elif Income_Category == '60K-80K':
        Income_Category_40_60 = 0 
        Income_Category_60_80 = 1
        Income_Category_80_120 = 0
        Income_Category_Less_than_40 = 0
        Income_Category_Unknown = 0
    elif Income_Category == '80K-120K':
        Income_Category_40_60 = 0 
        Income_Category_60_80 = 0
        Income_Category_80_120 = 1
        Income_Category_Less_than_40 = 0
        Income_Category_Unknown = 0
    elif Income_Category == 'Less than 40k':
        Income_Category_40_60 = 0 
        Income_Category_60_80 = 0
        Income_Category_80_120 = 0
        Income_Category_Less_than_40 = 1
        Income_Category_Unknown = 0
    else:
        Income_Category_40_60 = 0 
        Income_Category_60_80 = 0
        Income_Category_80_120 = 0
        Income_Category_Less_than_40 = 0
        Income_Category_Unknown = 1
        
        #Calculating Card Category
    if Card_Category == 'Gold':
        Card_Category_Gold = 1
        Card_Category_Platinum = 0
        Card_Category_Silver = 0
    elif Card_Category == 'Platinum':
        Card_Category_Gold = 0
        Card_Category_Platinum = 1
        Card_Category_Silver = 0
    else:
        Card_Category_Gold = 0
        Card_Category_Platinum = 0
        Card_Category_Silver = 1
    
    final_data = [Customer_Age ,
                  Dependent_count ,
                  Months_on_book ,
                  Total_Relationship_Count ,
                  Months_Inactive_12_mon ,
                  Contacts_Count_12_mon ,
                  Total_Revolving_Bal ,
                  Total_Amt_Chng_Q4_Q1 ,
                  Total_Trans_Amt ,
                  Total_Trans_Ct ,
                  Total_Ct_Chng_Q4_Q1 ,
                  Avg_Utilization_Ratio ,
                  Gender_M ,
                  Education_Level_Doctorate ,
                  Education_Level_Graduate ,
                  Education_Level_High_School ,
                  Education_Level_Post_Graduate ,
                  Education_Level_Uneducated ,
                  Education_Level_Unknown ,
                  Marital_Status_Married ,
                  Marital_Status_Single ,  
                  Marital_Status_Unknown ,
                  Income_Category_40_60 , 
                  Income_Category_60_80 ,
                  Income_Category_80_120 ,
                  Income_Category_Less_than_40 ,
                  Income_Category_Unknown ,
                  Card_Category_Gold ,
                  Card_Category_Platinum , 
                  Card_Category_Silver 
                  ]
    
    prediction = model.predict([final_data])
    
    
    if prediction == 1:
        prediction = " stay"
    else:
        prediction= " not stay"      
    
    
    return render_template('index.html', prediction_text = "Coustomer will" + prediction )

if __name__ == "__main__":
    app.run()