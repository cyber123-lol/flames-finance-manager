## project overview
flame's finance manager is a web application designed to assist users in managing their personal finances. the project was built using flask, which i thought would be a great and lightweight web framework in python. this application incorporates various features such as user authentication, transaction management, goal setting, financial analytics, and report generation. this document will outline my technical implementation and design decisions made while working on this project

## architecture

### 1. **flask framework**
- **reason for selection**: flask was chosen for its simplicity and its flexibility. it allowed me to easily integrate various extensions and libraries while maintaining a minimalistic structure.
- **projection structure**:
  - `app.py`: the main application file that contains the core logic, routes, and viewing functions
  - `templates/`: directory for the HTML templates
  - `static/`: contains static files such as `style.css` and `dark_mode.js`
  - `initialize_db.py`: script for initializing the sqlite3 database

### 2. **user auth**
  - **implementation**: user authentication was implemented using flask-login. this library handles the user session management, making it easier to restrict access to certain routes on the site
  - **design decision**: flask-login was chosen for its seamless integration with flask and its ability to manage user sessions with minimal configuration
 
### 3. **database design**
  - **SQLite**: an sqlite database was used for this project due to its simplicity and the fact that it doesn't require a separate server setup, making it ideal for a smaller-scale application like this one
  
  - **tables**:
    -`users`: stores the user credentials and profile information

    -`transactions`: logs all income and expense records

    -`goals`: tracks the savings goals set by the user
  
  - **design decision**: sqlite was chosen for its lightweight nature and ease of use during development. it also supports atomic commit and rollback, which is important for maintaining the data integrity

### 4. **frontend design**
  - **html**: static html templates are used to structure the application's web pages. the templates are styled using css for a consistent and responsive design
  - **css**: the application uses custom css along with bootstrap 5.3.2 for responsive design and ui components. bootstrap provides a clean, modern look while custom css allows for further customization
  - **dark/light mode**: implemented using a combination of css classes and javascript to toggle between modes. the user’s preference is stored in `localStorage` to persist between sessions

### 5. **financial analytics and visualizations**
  - **chart.js**: this library was used for generating interactive charts in the analytics section. it provides a variety of chart types and customization options, making it ideal for visualizing financial data
  - **design decision**: chart.js was selected because of its ease of integration with static html and css, and its capability to handle dynamic datasets that change based on user input

### 6. **report generation**
  - **reportlab**: the pdf report generation feature was implemented using reportlab, a library for creating pdfs in python
  - **design decision**: reportlab was chosen because it provides low-level control over the pdf creation process, allowing for a fully customized report layout that primarily utilizes text

## design considerations

### 1. security
  - **password hashing**: user passwords are hashed using `werkzeug.security` before being stored in the database. this ensures that even if the database is compromised, passwords remain protected
  - **session management**: flask-login is used to manage user sessions securely, ensuring that only authenticated users can access certain routes

### 2. **performance**
  - **pagination**: both transactions and goals are paginated to ensure that the application performs efficiently even as the dataset grows
  - **database optimization**: queries are optimized to fetch only the necessary data, reducing load times and improving the user experience

### 3. **user experience**
  - **responsive design**: the application is fully responsive, ensuring that it is usable on devices of various sizes, from desktops to mobile phones
  - **smooth transitions**: css transitions are used to enhance the visual experience, particularly in dark/light mode toggling and section expansion on the dashboard

### 4. **extensibility**
  - **modular design**: the project is designed in a modular fashion, making it easy to extend functionality. new features or sections can be added with minimal changes to the existing codebase, which also makes this a great project to continue in the future 
  - **future improvements**: the architecture allows for potential future enhancements such as integration with external financial apis, multi-user support, advanced analytics features, and extra design choices with css.
