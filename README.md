TrafficTelligence

Advanced Traffic Volume Estimation using Machine Learning

Project Overview
--------------------------------------------------------------
TrafficTelligence is a smart traffic volume prediction system that leverages machine learning to forecast the number of vehicles on the road using real-time environmental and temporal data. This project is developed as part of the SmartInternz Internship in collaboration with AICTE.

It helps traffic management authorities, city planners, and commuters make informed decisions based on predicted traffic congestion levels.

Features
-------------------------------------------------------------
Predicts traffic volume using ML regression model.

Clean web interface to input environmental data.

Real-time prediction with Flask backend.

Uses 11 meaningful traffic-related features.

Fully functional on local Flask server.

Mobile responsive UI with prediction output page.

Tech Stack
------------------------------------------------------------
Frontend: HTML, CSS

Backend: Python, Flask

ML Framework: scikit-learn

Environment: Google Colab for training, VS Code for deployment

Folder Structure
-----------------------------------------------------------
TrafficTelligence/
🔼 app.py                    # Flask application
🔼 model.pkl                 # Trained machine learning model
🔼 scaler.pkl                # Scaler for preprocessing input
🔼 requirements.txt          # Python dependencies
🔼 .gitignore                # Git ignore settings
🔼 README.md                 # Project readme
🔼 Data/
🔼 └— Traffic Volume.csv    # Dataset used for training
🔼 templates/
🔼 ├— index.html            # Input form page
🔼 └— final.html            # Output result page

Setup Instructions
------------------------------------------------------------
Prerequisites

Python 3.7+

Git

Flask

Browser (Chrome recommended)

Installation
-----------------------------------------------------------
git clone https://github.com/kaushhreddy/TrafficTelligence.git
cd TrafficTelligence
python -m venv venv
source venv/bin/activate        # On Linux/macOS
venv\Scripts\activate           # On Windows
pip install -r requirements.txt

Ensure model.pkl and scaler.pkl are present in the root directory.

Running the Application
------------------------------------------------------------
python app.py

Then open your browser and navigate to:http://127.0.0.1:5000/

Model Summary
------------------------------------------------------------
Training Accuracy: 97.50%

Training Loss: 0.1223

Validation Accuracy: 12.50%

Validation Loss: 2.2094

Model used: Linear Regression / Random Forest Regressor (as evaluated in Colab)

Input Features
-------------------------------------------------------------
The model takes the following 11 features:

Holiday

Rain

Snow

Temperature

Weather

Year

Month

Day

Hour

Minuts

Seconds

Authentication
-------------------------------------------------------------------
This version does not require authentication. Future improvements will include:

Role-based login (Admin/User)

Prediction history tracking

Known Issues
---------------------------------------------------------------
Prediction may be less accurate on unseen environmental conditions.

No error prompts for incorrect or missing values.

Model is trained on a fixed dataset (~40,000 records).

Future Enhancements
-------------------------------------------------------------
Host on Render or AWS

Add user login and dashboard

Integrate live weather APIs

Add graph analytics for traffic trends

Upload CSV for bulk prediction

License
-----------------------------------------------------------
This project is for academic and learning purposes under the SmartInternz Internship program.

