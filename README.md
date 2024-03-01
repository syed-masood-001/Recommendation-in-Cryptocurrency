
## **Description:**
This project is a recommendation system for cryptocurrency prices. It allows users to:
**Select a cryptocurrency:** Bitcoin, Ethereum, or Tether.
**Enter a future date:** The system will predict the price of the chosen cryptocurrency on that date.
**View the predicted price:** The system displays the predicted price along with a graph representing the historical and predicted market sentiment.
**Access buy/sell options:** The system provides a QR code that redirects users to a trusted website (Coinbase) for buying or selling the chosen cryptocurrency.

## **Technologies Used:**
**Frontend:** HTML, CSS, JavaScript (Bootstrap)

**Backend:** Python (Flask)

**Machine Learning:** Random Forest Regression



## **Project Files:**
**app.py:** Python script containing the Flask app logic, including data loading, model training, prediction, and routing.

**index.html:** Main HTML file for the user interface.

**index1.html:** Login page HTML file. (Currently not functional)

**pass1.html:** HTML file displaying the predicted price, market sentiment graph, and QR code for buy/sell options.

**index1.css, pass1.css:** CSS files for styling the user interface.

## **How to Run the Project:**
Make sure you have Python (version 3.6 or later) and the required libraries (Flask, pandas, numpy, sklearn) installed. You can install them using pip install flask pandas numpy scikit-learn.

Clone or download the project repository.

Open a terminal or command prompt and navigate to the project directory.

Run the following command: python app.py

Open http://127.0.0.1:5000/ in your web browser to access the application.

## **Disclaimer:**
This project is for educational purposes only and should not be considered financial advice. Cryptocurrency trading involves significant risks, and you should always conduct your own research before making any investment decisions.
