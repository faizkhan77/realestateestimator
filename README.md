# RealEstateEstimator

RealEstateEstimator is an end-to-end machine learning and Django project designed to predict property prices based on various features. This project uses real-life data consisting of 200,000 property details from 81 different cities in India.

## Project Structure

- **Raw Data**: The raw data can be downloaded from [here](https://www.kaggle.com/datasets/juhibhojani/house-price).
- **Jupyter Notebook**: Located in the root directory. Contains data cleaning, feature engineering, and model training processes.
- **Static Files**: All static files such as images, CSS, SCSS, and JS are in the `static` folder.
- **Saved Model**: The trained model is saved in the `artifact` folder.
- **Django Project**: The main Django project, `houseprice_project`, contains the `settings.py` file.
- **Django App**: The Django app, `api`, contains `views.py` and `urls.py`.
- **Templates**: The `template` folder consists of the GUI made using Django templates.
- **Requirements**: Dependencies are listed in the `requirements.txt` file.

## Overview

### Data Cleaning and Feature Engineering

- Analyzed and visualized each feature.
- Cleaned null values and incorrect formats.
- Identified and managed outliers.
- Created new features to enhance predictive power.

### Model Training

Trained various regression models and selected the best performer with 95% accuracy on the test dataset:
- Linear Regression
- Elastic Net
- Random Forest Regressor
- Decision Tree Regressor
- Gradient Boosting Regressor
- Bagging Regressor
- KNN Regressor

### Django Application

Built a Django application to serve the model predictions:
- Designed a user-friendly interface using CSS, Bootstrap, and SCSS.
- Developed views for API endpoints to load features and make predictions.
- Implemented JavaScript to handle fetching of features and displaying predicted values dynamically.

## Deployment

The application is hosted using Railway. Check out the website [here](https://realestateestimator.up.railway.app/).

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/faizkhan77/realestateestimator.git
   cd RealEstateEstimator
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the Django server:
   ```sh
   python manage.py runserver
   ```

## Usage

- Access the Jupyter notebook in the root directory to explore the data cleaning, feature engineering, and model training processes.
- Use the Django application to predict property prices based on various input features.

## Contributing

Feel free to contribute to the project if you want to help improve the model or the Django application. Your contributions are greatly appreciated!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
