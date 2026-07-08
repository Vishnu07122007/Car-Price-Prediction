# Car Price Prediction

An interactive machine learning web app that estimates the selling price of a used car in real time. The project combines **XGBoost**, **Pandas**, and **Streamlit** to turn a trained regression model into a clean, user-friendly prediction tool.

## Why This Project Stands Out

- Fast, instant price estimation from a few simple car details
- Clean Streamlit interface with a minimal user journey
- Trained regression model powered by XGBoost
- Easy to run locally and simple to extend for deployment

## Live Workflow

1. Enter the car's market value and usage details.
2. Select the fuel type, seller type, and transmission.
3. Choose the number of previous owners and the purchase year.
4. The app converts those values into model-ready features.
5. The trained XGBoost model returns the predicted selling price.

## Features

- Predicts used car selling price in **lakhs**
- Supports multiple categorical inputs
- Uses purchase year to derive car age automatically
- Loads a saved model from `xg_model.json`
- Simple one-click prediction experience

## Tech Stack

- Python
- Pandas
- NumPy
- XGBoost
- Streamlit

## Project Structure

- `car_price_prediction.py` - Streamlit application
- `xg_model.json` - saved trained XGBoost model
- `car data.csv` - dataset used for exploration and modeling
- `CAr_price_prediction.ipynb` - notebook version of the project

## Input Features Used by the Model

- Present Price - ex-showroom price of the car
- KMs Driven - total distance driven
- Fuel Type - Petrol, Diesel, or CNG
- Seller Type - Dealer or Individual
- Transmission - Manual or Automatic
- Owner - number of previous owners
- Age - calculated from the purchase year

## How the Model Works

The app collects user input, transforms categorical values into numeric codes, creates a single-row dataframe, and passes that data to the saved XGBoost model. The prediction is then formatted and displayed as the estimated resale value.

## Input Mapping

- Fuel Type: `Petrol = 0`, `Diesel = 1`, `CNG = 2`
- Seller Type: `Dealer = 0`, `Individual = 1`
- Transmission: `Manual = 0`, `Automatic = 1`

## Run Locally

Install the dependencies:

```bash
pip install pandas numpy xgboost streamlit
```

Start the app:

```bash
streamlit run car_price_prediction.py
```

## Example Use Case

If you want to estimate the resale value of a second-hand car before buying or selling it, enter the car details into the form and click **Predict**. The app will return an estimated selling price in lakhs.

## Notes

- Keep `xg_model.json` in the same directory as `car_price_prediction.py`.
- The result is an estimate, not a guaranteed market price.
- You can improve the project further by adding charts, deployment, and a richer UI.

## Future Improvements

- Add model performance metrics
- Include sample screenshots or a demo GIF
- Deploy the app to Streamlit Cloud or Hugging Face Spaces
- Expand support for more car attributes
- Add data validation and better error handling
