# FreeCodeCamp Data Analysis Projects

This repository contains five data analysis projects that were completed as part of my **Data Analysis with Python** certification from [freeCodeCamp](https://www.freecodecamp.org/). Each project showcases different techniques in Python for analyzing, visualizing, and predicting data trends. The repository is structured to highlight both the code logic and test cases, along with the visual outputs in some cases.

## Projects

1. **Demographic Data Analyzer**
   - Analyze demographic data from a dataset using statistical calculations.
   - Outputs include various metrics like race count, average age of men, and gender-based percentage calculations.
   - Files: 
     - `demographic_data_analyzer.py` - contains the logic for data analysis.
     - `test_module.py` - test cases to verify the functionality.
     - `main.py` - the main executable file.

2. **Mean-Variance-Standard Deviation Calculator**
   - A program that computes the mean, variance, and standard deviation of a 3x3 matrix.
   - The project implements simple statistical operations.
   - Files: 
     - `mean_variance_std_calculator.py` - core logic for matrix operations.
     - `test_module.py` - unit tests.
     - `main.py` - the main entry point.

3. **Medical Data Visualizer**
   - Visualization of medical data, including factors such as cholesterol, glucose levels, and cardiovascular disease.
   - Various types of plots like categorical plots and heatmaps are generated to uncover patterns in the medical data.
   - Files: 
     - `medical_data_visualizer.py` - script for data visualization.
     - `test_module.py` - tests to ensure the accuracy of the visualizations.
     - `main.py` - the main file to run the program.
     - Plots are saved as output images.

4. **Page View Time Series Visualizer**
   - Visualizes a dataset of daily page views over a time period using line plots, bar charts, and box plots.
   - Provides insights into time-based data trends.
   - Files: 
     - `page_view_time_series_visualizer.py` - logic for generating the visualizations.
     - `page_view_time_series_visualizer_notebook.ipynb` - an interactive way to generate the visualizations.
     - `test_module.py` - testing script for the visualizer.
     - `main.py` - the main executable.
     - Plots are saved as results.

5. **Sea Level Predictor**
   - Uses linear regression to predict future sea levels based on historical data.
   - Visualizes the trend of sea levels using a line plot and makes predictions for future sea levels.
   - Files: 
     - `sea_level_predictor.py` - core logic for sea level prediction and visualization.
     - `sea_level_predictor_notebook.ipynb` - an interactive way to see the sea level prediction and visualization.
     - `test_module.py` - unit tests.
     - `main.py` - the main executable.
     - Plots are saved as output images.

## How to Run the Projects

1. Clone the repository:
  ```bash
  git clone https://github.com/yourusername/freeCodeCamp-data-analysis-projects.git
  ```
   
2. Navigate to a project folder:
  ```bash
  cd project-name
  ```

3. Create a virtual environment and activate it:
  ```bash
  python -m venv .venv
  ```

  ```bash
  # For Linux Based OS Or Mac-OS.
  source ./.venv/bin/activate

  # For Windows With CMD
  .\venv\Scripts\activate.bat

  # For Windows With Power shell
  .\venv\Scripts\activate.ps1
  ```

4. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
   
5. Run the project:
  ```bash
  python main.py
  ```
