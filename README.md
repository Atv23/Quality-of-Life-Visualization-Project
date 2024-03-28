# Quality of Life Visualization Project

## Project Overview
This repository contains the work submitted for the CSC3833 Data Visualization and Visual Analytics course's summative assignment. The project aims to visualize the Quality of Life across countries using data from the OECD Better Life Index. The visualization project consists of an interactive web page that explores, compares, and analyzes data related to human well-being globally.

## Objective
Design and implement an interactive visualization that allows users to explore and understand the Quality of Life across different countries. This project targets a broad audience, emphasizing accessibility and ease of understanding without requiring a statistical or mathematical background.

## Data Source
The project uses data from the OECD Better Life Index, which measures well-being across various areas in OECD and selected non-OECD countries. The dataset encompasses 38 OECD countries and 3 non-OECD countries, across 24 indicators categorized into 11 topic areas, including Housing, Income, Jobs, Community, Education, Environment, Civic Engagement, Health, Life Satisfaction, Safety, and Work-Life Balance.

## Technologies Used
- **Python**: For data wrangling and analysis.
- **Vega-Altair**: For visualization design.
- **Pandas and Numpy**: For data management.

## Features
- **Interactive Elements**: Users can engage with the visualization to explore and compare quality of life indicators.
- **Multiple Views**: The project includes multiple views focusing on Life Satisfaction Across Countries, Life Satisfaction by Inequality Measure, and Employment Rate Across Countries.
- **Stand-alone Web Page**: The visualization is accessible as an HTML page, designed to be self-explanatory and suitable for users with any level of technical expertise.

## Project Structure
- `main.html`: The main HTML page that hosts the visualization, incorporating the individual views as embedded `iframe` elements.
- `view1.html`, `view2.html`, `view3.html`: HTML files for each of the visualization views.
- `Python_code.py`: The Python script used for data preprocessing and visualization generation.
- `BLI_29112023224043012.csv`: The OECD dataset used for the visualization.
- `Technical Report.pdf`: A comprehensive report discussing the visualization design, objectives, methodology, and insights.

## Running the Project
To view the visualization, open `main.html` in any modern web browser. Ensure that all files are in the same directory to allow for proper loading of the views.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- OECD for providing the Better Life Index data.
- CSC3833 Course Instructors and TAs for guidance and support.
