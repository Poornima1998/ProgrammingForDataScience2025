Question 1:

Project Overview:
The project involves a university management system that is programmed in Python and Object-Oriented Programming(OOP). It handles various departments, courses, students and faculty which reflects the OOP concepts such as inheritance, encapsulation, and Polymorphism.

Repository Structure:
├── question1_university_system/
│ ├── main.py           #Program entry point demonstrating system features
│ ├── person.py         #Base person class
│ ├── student.py        #Student class and subclasses
│ ├── faculty.py        #Faculty class and roles
│ ├── department.py     #Department management
│ ├── course.py         #Course of the management
│ └── staff.py          #Staff class

How to run:
1. Ensure python 3 is installed.
2. Clone the repository
3. Navigate to the directory (question1_university_system)
4. Run the main script (bash - python main.py)

This executes this system demo that forms departments, faculty, and students, registers courses, computes GPA, and displays tasks.

Key functionalities:
- Full class inheritance hierarchy for university members: Person->Student,Faculty,Staff->specialized faculty and student roles
- Student course enrollments with method to add/drop and track courses
- GPA calculation across semesters with academic status evaluation
- Secure data handling with encapsulation for critical data such as GPA
- Different responsibility methods overridden by class to reflect roles (Polymorphism)
- Department and course management with enrolment limits and prerequisite checking

Design and Implementation notes:
- Used python super() for clear inheritance and code reuse
- To protect data use encapsulations
- Validate inputs such as GPA and enrollment limits
- Polymorphism demonstrated by method overriding in Person subclasses


Question 2:

Project Overview:
This project is a scraper of book information of an online book store, cleans and processes the information, analyzes the trends in prices and ratings, visualizes the results, and develops prediction models. The folder system is used to keep every element of the project clean and comprehensible so that new users and reviewers can easily follow the process of how the analysis is carried out.

Repository Structure:
question2_social_media_analysis/
├── data_collection/
│   └── scrape_books.py         # Scrapes book data and saves it as CSV
├── data_processing/
│   └── clean_data.py           # Cleans and formats scraped data
├── analysis/
│   ├── descriptive_stats.py    # Exploratory analysis (EDA), stats, and summary reporting
│   └── predictive_model.py     # Linear regression and basic recommendation system
└── visualizations/
    ├── plots.py                # Static and interactive graph visualizations
    └── interactive_plots.py    # Plotly-based exploratory graphs
└── main.py                     # Runs the entire pipeline in order


How to run:
1. Install Python
2. Install libraries. run in the terminal (pip install requests beautifulsoup4 pandas seaborn matplotlib scikit-learn plotly)
3. Clone the project
4. Open terminal and move into the directory
5. Run the program (python main.py)
6. Check the output, CSV files, and graphs

File Descriptions:
scrape_books.py
Connects to the target website, downloads book info (title, price, rating), saves raw results, and handles multiple pages and delays between requests.

clean_data.py
Removes duplicates and missing entries, standardizes text (lowercase, removes extra characters), and validates the data format for analysis.

descriptive_stats.py
Calculates and prints price summaries, average ratings, counts, and detects outliers and correlations.

predictive_model.py
Uses regression to link ratings to prices and demonstrates simple recommendation by finding similar books.

plots.py
Quickly shows distributions (histograms, box plots, scatter plots); compares categories, rating, and price visually.

interactive_plots.py
Loads interactive charts using Plotly for better data exploration, including color-by-category and filtering.

main.py
“Glue code” that runs each module: collects data, cleans data, analyzes findings, builds and tests models, and shows all visualizations.

Design and Implementation notes:
- Each file contains comments explaining its purpose and key function steps
- Graphs and models illustrate core data science concepts simply.