# Django Speed Test Application

This Django application provides a simple and modern interface for running internet speed tests using the `speedtest-cli` library.  It stores results in a database, offers a user-friendly UI powered by Tailwind CSS, and handles tests asynchronously.


## Features

- **Database Storage:** Results are stored using the `SpeedTestResult` model.
- **Modern UI:** Styled with CSS.
- **Asynchronous Testing:** Speed tests run asynchronously using AJAX.
- **Progress Visualization:** Animated progress bars for download, upload, and ping.
- **History:** Displays the last 5 test results.
- **Error Handling:** Proper error handling and user feedback.

## Installation

1. **Create a new Django project and app:**

    ```bash
    django-admin startproject speedtest_project
    cd speedtest_project
    python manage.py startapp speedtest_app


2. **Install required packages:**

    ```bash
    pip install django speedtest-cli

3. **Project setup:**
    Add 'speedtest_app' to INSTALLED_APPS in settings.py.
    Copy the models.py, views.py, and urls.py content into the speedtest_app directory.
    Create the templates directory structure:
      ```bash
      mkdir -p speedtest_app/templates/speedtest_app
    Copy the index.html content into the newly created directory.

4. **Configure the main URLs** (speedtest_project/urls.py):


    ```bash
    from django.contrib import admin
    from django.urls import path, include
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('speedtest_app.urls')),
    ]

5. **Create and apply the database migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate

6. **Run the development server:**

    ```bash
    python manage.py runserver


## Usage

1.  Navigate to http://127.0.0.1:8000/ in your browser to access the speed test application.
2.  Click the "Start Test" button to begin the speed test.
3.  Observe the progress bars for download, upload, and ping speeds.
4.  The results, including the last 5 tests, will be displayed on the page.

![speedtest](https://github.com/user-attachments/assets/1a011def-eef4-4a2b-84f1-4da4cd2c8728)


## Key Features (Detailed)
1.  Database Storage: Results are stored in a database using the SpeedTestResult model, allowing for historical analysis and tracking.
2.  Modern UI:  Tailwind CSS provides a clean and responsive user interface.
3.  Asynchronous Testing: AJAX is used to run the speed tests in the background without blocking the user interface, improving responsiveness.
4.  Progress Visualization: Animated progress bars provide real-time feedback on the progress of the download, upload, and ping tests.
5.  History: The application displays the last 5 test results, allowing users to quickly compare their recent speeds.
6.  Error Handling: The application includes error handling to provide informative messages to the user in case of issues during the speed test.

## Important Notes
  The speed test might take 20-30 seconds to complete.
  
  Ensure your server timeout settings are configured appropriately to accommodate the test duration.
  
  Consider adding a loading indicator during the test for better user experience.
  
  You might want to add user authentication to track individual user's test history.

## Contributing
Contributions are welcome!  Please open an issue or submit a pull request.

## License
MIT License
