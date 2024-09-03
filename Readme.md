A Quiz app for JS Quiz contest of 
st.xavier's School Jawalakhel
Here's the final version of the setup guide, including instructions on how to run the application.

### Complete Setup Guide for JS_Quiz_Contest Repository

### 1. **Clone the Repository**
- Clone the repository to your local machine:
```bash
git clone https://github.com/Lonesoldier230/JS_Quiz_Contest.git
cd JS_Quiz_Contest
```

### 2. **Create the `postgres_keys.env` File**
- In the root directory of the project, create a `postgres_keys.env` file:
```bash
touch postgres_keys.env
```
- Open the `postgres_keys.env` file and add the following content, replacing the placeholders with your actual database
credentials:
```env
POSTGRES_DB = your_db_name
POSTGRES_USER = your_username
POSTGRES_PASSWORD = your_password
```

### 3. **Create the `.env` File**
- In the root directory, create a `.env` file:
```bash
touch .env
```
- Open the `.env` file and add the following content, replacing the placeholders with your actual values:
```env
DJANGO_SECRET_KEY = your_secret_key
DB_NAME = your_db_name
DB_USER = your_username
DB_PASSWORD = your_password
```

### 4. **Build the Application**
- With the environment variables set up, build the application using Docker Compose:
```bash
docker-compose up --build
```
- This command will build the necessary services as defined in the `docker-compose.yml` file.

### 5. **Run the Application**
- After building, start the application:
```bash
docker-compose up
```
- The application should now be running.

### 6. **Access the Application**
- Once the application is running, you can access it by navigating to `http://0.0.0.0` or `http://localhost` in your web
browser.

### 7. **Stopping the Application**
- To stop the application and remove the containers, run:
```bash
docker-compose down
```

### 8. **Development Workflow**
- Any changes you make to the code on your local machine will be automatically reflected inside the container, making
development smoother.

### Conclusion
This guide provides all the necessary steps to set up, build, run, and access the JS_Quiz_Contest application using
Docker. By following these instructions, you can ensure that the application runs smoothly and is easily accessible via
your local machine.