# Fire Weather Index (FWI) Prediction

## Project Overview
This project aims to predict the Fire Weather Index (FWI) based on various meteorological and environmental factors. The FWI is a critical indicator used in forest fire management, assessing the risk and potential behavior of fires.

## Key Features
- **Data Cleaning and Preprocessing**: Ensuring the dataset is clean and ready for analysis.
- **Exploratory Data Analysis (EDA)**: Observing patterns and relationships within the data, such as the increase in fire incidents during summers.
- **Feature Selection**: Addressing issues like multicollinearity to ensure reliable model performance.
- **Model Training**:
  - Linear Regression
  - Lasso Regression
  - Ridge Regression
  - ElasticNet Regression
- **Cross-Validation**: Evaluating models to select the most suitable one based on performance metrics.
- **Model Deployment**: Saving the best model using pickle and implementing it in a Flask app for user interaction.

## Dataset
The dataset includes various meteorological and environmental factors such as:
- Date
- Fire Weather Index (FWI)
- Relative Humidity (RH)
- Wind Speed (Ws)
- Rain
- Fine Fuel Moisture Code (FFMC)
- Duff Moisture Code (DMC)
- Drought Code (DC)
- Initial Spread Index (ISI)
- Buildup Index (BUI)
- Temperature
- Class (fire or not fire)

  
## Project Structure
- `application.py`: Main Flask application file.
- `model.pkl`: Pickle file containing the trained model.
- `templates/`: Folder containing HTML templates.
- `README.md`: Project documentation.
- `requirements.txt`: List of required packages.

## Model Evaluation
The models were evaluated using cross-validation and the following metrics:
- **Mean Absolute Error (MAE)**
- **R² Score**

The selected model provides a balance of high accuracy and generalizability.
