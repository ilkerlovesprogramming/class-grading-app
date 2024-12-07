# Troubleshooting Guide for WSGI Configuration

## Problem
The Django development server is unable to load the WSGI application with the error:
```
ModuleNotFoundError: No module named 'studentgrades.wsgi'
```

## Resolution Steps

1. **Configure PyCharm Project Structure**
   - Open PyCharm Settings/Preferences
   - Go to "Project: studentgrades" > "Project Structure"
   - Mark the outer `studentgrades` directory as "Sources Root" (Right-click > Mark Directory as > Sources Root)
   - This ensures Python can find modules correctly

2. **Verify Virtual Environment Configuration**
   - Open PyCharm Settings/Preferences
   - Go to "Project: studentgrades" > "Python Interpreter"
   - Ensure the correct virtual environment is selected
   - Make sure Django is installed in this environment

3. **Run Configuration Setup**
   - Edit your Run Configuration for Django Server
   - Set "Working directory" to the outer studentgrades directory (where manage.py is located)
   - Ensure "Environment variables" includes PYTHONPATH with the project root

4. **Alternative Command Line Approach**
   If PyCharm still has issues, try running from command line:
   ```bash
   cd path/to/outer/studentgrades
   python manage.py runserver
   ```

## Project Structure Reference
Your project structure should look like:
```
studentgrades/             # Outer directory (mark as Sources Root)
    ├── manage.py
    ├── api/
    └── studentgrades/     # Inner directory
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```

## Note
The WSGI configuration is correct, but PyCharm's environment needs to be properly configured to find the Python modules. These steps should resolve the module import issues.