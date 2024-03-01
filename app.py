import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from datetime import datetime, timedelta
import requests

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index1.html')


@app.route('/', methods=['POST'])
def getvalue():
    db = request.form['dateofbirth']


    def bitcoin():
        df = pd.read_csv(r"C:\Users\HP\Downloads\BTC-USD (8).csv")

        df['Date'] = pd.to_datetime(df['Date'])
        df = df.dropna()

        x = df.drop(['Close', 'Date'], axis=1)
        y = df['Close']
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

        model = RandomForestRegressor(n_estimators=100, random_state=0)
        model.fit(x_train, y_train)

        input_date = db
        date = datetime.strptime(input_date, "%Y-%m-%d")

        date_df = pd.DataFrame({'Date': [date]})
        date_df = date_df.merge(df.drop(['Close'], axis=1).groupby('Date').mean().reset_index(), on='Date', how='left')
        date_df = date_df.fillna(df.drop(['Close', 'Date'], axis=1).mean())
        date_df = date_df.drop(['Date'], axis=1)

        y_pred = model.predict(x_test)
        prediction = model.predict(date_df)
        # print("prediction: ", prediction[0])

        new_data = pd.DataFrame({"Date": date, "Open": date_df["Open"], "High": date_df["High"], "Low": date_df["Low"],
                                 "Close": prediction[0], "Adj Close": date_df["Adj Close"],
                                 "Volume": date_df["Volume"]})

        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv(r"C:\Users\HP\Downloads\BTC-USD (2).csv", index=False)

        print(r2_score(y_test, y_pred) * 100)
        return prediction[0]

    def eth():
        df = pd.read_csv(r"C:\Users\HP\Downloads\ETH-USD (2).csv")
        df['Date'] = pd.to_datetime(df['Date'])
        x = df.drop(['Close', 'Date'], axis=1)
        y = df['Close']
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
        model = RandomForestRegressor(n_estimators=100, random_state=0)
        model.fit(x_train, y_train)
        input_date = input("Enter a date in YYYY-MM-DD format: ")
        date = datetime.strptime(input_date, "%Y-%m-%d")
        date_df = pd.DataFrame({'Date': [date]})
        date_df = date_df.merge(df.drop(['Close'], axis=1).groupby('Date').mean().reset_index(), on='Date',
                                    how='left')
        date_df = date_df.fillna(df.drop(['Close', 'Date'], axis=1).mean())
        date_df = date_df.drop(['Date'], axis=1)
        y_pred = model.predict(x_test)
        prediction = model.predict(date_df)
        print("prediction: ", prediction[0])
        new_data = pd.DataFrame(
        {"Date": date, "Open": date_df["Open"], "High": date_df["High"], "Low": date_df["Low"],
        "Close": prediction[0], "Adj Close": date_df["Adj Close"], "Volume": date_df["Volume"]})
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv(r"C:/Users/HP/Downloads/ETH-USD.csv", index=False)

        return prediction

    def usdt():
        df=pd.read_csv(r"C:\Users\HP\Downloads\USDT-USD (2).csv")

        df['Date'] = pd.to_datetime(df['Date'])

        x= df.drop(['Close', 'Date'], axis=1)
        y= df['Close']
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

        model = RandomForestRegressor(n_estimators=100, random_state=0)
        model.fit(x_train, y_train)

        input_date= input("Enter a date in YYYY-MM-DD format: ")
        date = datetime.strptime(input_date, "%Y-%m-%d")

        date_df = pd.DataFrame({'Date': [date]})
        date_df = date_df.merge(df.drop(['Close'], axis=1).groupby('Date').mean().reset_index(), on='Date', how='left')
        date_df = date_df.fillna(df.drop(['Close', 'Date'], axis=1).mean())
        date_df = date_df.drop(['Date'], axis=1)

        y_pred=model.predict(x_test)
        prediction = model.predict(date_df)
        print("prediction: ",prediction[0])

        new_data=pd.DataFrame({"Date":date,"Open":date_df["Open"],"High":date_df["High"],"Low":date_df["Low"],"Close":prediction[0],"Adj Close":date_df["Adj Close"],"Volume":date_df["Volume"]})

        df=pd.concat([df,new_data],ignore_index=True)
        df.to_csv(r"C:/Users/HP/Downloads/USDT-USD.csv",index=False)
        return prediction



    #if n==1:
     #   dummy=bitcoin()
    #elif n==2:
    #    dummy=eth()
    #else:
     #   usdt()


    return render_template('pass1.html', db=bitcoin())


if __name__ == '__main__':
    app.run(debug=True)
