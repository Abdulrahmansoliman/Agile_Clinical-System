
# Clinic Management System
This is a simple Flask application for a clinic management system. The application uses SQLAlchemy for database management and Sentry for error logging.
## Getting Started
To get started, first clone the repository:
```bash
    git clone https://github.com/yourusername/clinic-management-system.git
```
Next, create a virtual environment and activate it:
```bash
    python3 -m venv venv
    source venv/bin/activate
```
Install the required dependencies:

```bash
    pip install -r requirements.txt
```
Create a PostgreSQL database and set the DATABASE_URL environment variable with the connection string.

Then, run the following command to initialize the database:
```bash
    python3 manage.py db upgrade
```
```bash
    Finally, run the Flask application:
```
The application will be available at http://localhost:5000.


## Usage

The application provides endpoints to manage users, appointments, and clinic items. The endpoints are documented using Swagger and can be accessed at http://localhost:5000/api/docs.
## License

This application is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License. See the LICENSE file for more information.

