<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Login</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      background-color: #f8f8f8;
      margin: 0;
      padding: 0;
    }

    h1 {
      color: #333;
      margin-top: 20px;
    }

    img {
      max-width: 300px;
      margin: 20px auto;
    }

    .login-container {
      background: #fff;
      border: 1px solid #ccc;
      padding: 20px;
      width: 300px;
      margin: 20px auto;
      border-radius: 8px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }

    label {
      display: block;
      margin-top: 10px;
      color: #555;
    }

    input {
      width: 100%;
      padding: 8px;
      margin-top: 5px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 14px;
    }

    button {
      background-color: #007bff;
      color: white;
      padding: 10px 15px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 14px;
    }

    button:hover {
      background-color: #0056b3;
    }

    .flash-message {
      color: red;
      margin-top: 10px;
    }
  </style>
</head>
<body>
  <h1>Welcome to Cookie Manipulation!</h1>
  <img src="{{ url_for('static', filename='images/milk-and-cookies.png') }}" alt="Milk and Cookies">

  {% with messages = get_flashed_messages() %}
    {% if messages %}
      <div class="flash-message">
        {{ messages[0] }}
      </div>
    {% endif %}
  {% endwith %}

  <div class="login-container">
    <form method="POST">
      <label for="username">Username:</label>
      <input type="text" id="username" name="username" required>
      <label for="password">Password:</label>
      <input type="password" id="password" name="password" required>
      <button type="submit">Log In</button>
    </form>
  </div>
</body>
</html>
