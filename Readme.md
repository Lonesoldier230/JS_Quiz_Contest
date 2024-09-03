A Quiz app for JS Quiz contest of 
st.xavier's School Jawalakhel

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JS_Quiz_Contest</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        h1, h2, h3 {
            color: #333;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 4px;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
        }
        a {
            color: #007bff;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

    <h1>JS_Quiz_Contest</h1>
    <p>Welcome to the JS_Quiz_Contest repository! This project is designed to offer a quiz contest platform using JavaScript.</p>

    <h2>Setup Guide</h2>

    <h3>1. Clone the Repository</h3>
    <pre><code>git clone https://github.com/Lonesoldier230/JS_Quiz_Contest.git
cd JS_Quiz_Contest</code></pre>

    <h3>2. Create the <code>postgres_keys.env</code> File</h3>
    <p>In the root directory of the project, create a <code>postgres_keys.env</code> file:</p>
    <pre><code>touch postgres_keys.env</code></pre>
    <p>Open the <code>postgres_keys.env</code> file and add the following content, replacing the placeholders with your actual database credentials:</p>
    <pre><code>POSTGRES_DB = your_db_name
POSTGRES_USER = your_username
POSTGRES_PASSWORD = your_password</code></pre>

    <h3>3. Create the <code>.env</code> File</h3>
    <p>In the root directory, create a <code>.env</code> file:</p>
    <pre><code>touch .env</code></pre>
    <p>Open the <code>.env</code> file and add the following content, replacing the placeholders with your actual values:</p>
    <pre><code>DJANGO_SECRET_KEY = your_secret_key
DB_NAME = your_db_name
DB_USER = your_username
DB_PASSWORD = your_password</code></pre>

    <h3>4. Build the Application</h3>
    <p>With the environment variables set up, build the application using Docker Compose:</p>
    <pre><code>docker-compose up --build</code></pre>

    <h3>5. Run the Application</h3>
    <p>After building, start the application:</p>
    <pre><code>docker-compose up</code></pre>
    <p>The application should now be running.</p>

    <h3>6. Access the Application</h3>
    <p>Once the application is running, you can access it by navigating to <a href="http://0.0.0.0">http://0.0.0.0</a> or <a href="http://localhost">http://localhost</a> in your web browser.</p>

    <h3>7. Stopping the Application</h3>
    <p>To stop the application and remove the containers, run:</p>
    <pre><code>docker-compose down</code></pre>

    <h3>8. Development Workflow</h3>
    <p>Any changes you make to the code on your local machine will be automatically reflected inside the container, making development smoother.</p>

    <h2>Conclusion</h2>
    <p>This guide provides all the necessary steps to set up, build, run, and access the JS_Quiz_Contest application using Docker. By following these instructions, you can ensure that the application runs smoothly and is easily accessible via your local machine.</p>

</body>
</html>
