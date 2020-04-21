from users.models import *
doctors_extd = ExtendedDoctorsDetail.objects.filter(specialization='Family Physicians')
doctors_base = doctors_extd.user
print(doctors_extd)

'''import requests
import json

send_url = "http://api.ipstack.com/check?access_key=b652053a823bacc0fda4b403ffd99e03"
geo_req = requests.get(send_url)
geo_json = json.loads(geo_req.text)
latitude = geo_json['latitude']
longitude = geo_json['longitude']
city = geo_json['city']

print(city)

import datetime
import calendar

start_time = '10'
end_time = '16'
today_date = datetime.date.today()
holidays = ['sunday', 'saturday']
for i in range(10):
    the_date = today_date + datetime.timedelta(days=i)
    the_day_of_week = calendar.day_name[datetime.datetime.strptime(str(the_date), '%Y-%m-%d').weekday()]
    if the_day_of_week.lower() not in holidays:
        print(the_date, ' ', the_day_of_week)

        now_time = datetime.datetime.now().time()#.strftime('%I:%M %p')
        if the_date == today_date:
            print('now: ', now_time.strftime('%I:%M %p'))
        for ix in range(int(start_time), int(end_time)):
            tm1 = datetime.datetime.strptime(str(ix), '%H').time()
            tm2 = datetime.timedelta(hours=tm1.hour, minutes=tm1.minute) + datetime.timedelta(hours=1)
            tm2 = (datetime.datetime.min + tm2).time()#.strftime('%I:%M %p')
            #tm1 = tm1

            if the_date == today_date:
                if now_time < tm1:

                    print('Going', tm1.strftime('%I:%M %p'), '->', tm2.strftime('%I:%M %p'))
            else:
                print('Going', tm1.strftime('%I:%M %p'), '->', tm2.strftime('%I:%M %p'))
    else:
        print(the_date, ' ', the_day_of_week)
        print('Not Available')

###########################################
import csv
import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB

# load Training and Testing datasets
train_file = open('database_files/dataset/Training.csv')
test_file = open('database_files/dataset/Testing - Copy.csv')

# convert into readable format from csv file
train_result = pd.read_csv(train_file)
test_result = pd.read_csv(test_file)

# Extract the Features and Target class for Training
Features_Train = train_result.drop(['prognosis'], axis=1).values
Target_Train = train_result['prognosis'].values

# Extract the Features and Target class for Testing
Features_Test = test_result.drop(['prognosis'], axis=1).values
Target_Test = test_result['prognosis'].values

gnb = GaussianNB()

gnb.fit(Features_Train, Target_Train)
################################################
# all the diseases that model can predict(41)
tags = np.unique(Target_Train)

# data to check for prediction
Features_Predict = Features_Test[:2]

# predicting with probability for each disease
predicts = gnb.predict_proba(Features_Predict)

# create dictionary with key as disease and probability as value {'disease': 0.5}
# predict_proba gives nested array,
# when single row of data provided, we have to access the internal array
pred_dict = dict(zip(tags, predicts[0]))
# sort dictionary based on probability
dicts = sorted(pred_dict.items(), key=lambda x: x[1], reverse=True)

# print only top 3 disease with highest probability
for i in range(3):
    if dicts[i][1] >= 0.30:
        print(dicts[i][0], ' --> Accuracy: ', round(dicts[i][1]*100), '%')
'''