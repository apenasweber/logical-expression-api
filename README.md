# Nextron Challenge API
A Fastapi project to store, delete and evaluate logical expressions using Postgres on database and Docker for containerization.

nextron-challenge
┣ alembic  
 ┃ ┣ versions  
 ┃ ┃ ┗ 15366a5dec39_create_expression_table.py  
 ┃ ┣ env.py  
 ┃ ┣ README  
 ┃ ┗ script.py.mako  
 ┣ api  
 ┃ ┣ auth  
 ┃ ┃ ┣ auth_bearer.py  
 ┃ ┃ ┣ auth_handler.py  
 ┃ ┃ ┗ __init__.py  
 ┃ ┣ core  
 ┃ ┃ ┣ settings.py  
 ┃ ┃ ┗ __init__.py  
 ┃ ┣ database  
 ┃ ┃ ┣ connection.py  
 ┃ ┃ ┣ retry_logic.py  
 ┃ ┃ ┗ __init__.py  
 ┃ ┣ models  
 ┃ ┃ ┣ expression.py  
 ┃ ┃ ┣ schemas.py  
 ┃ ┃ ┗ __init__.py  
 ┃ ┣ routers  
 ┃ ┃ ┣ expression.py  
 ┃ ┃ ┣ login.py  
 ┃ ┃ ┗ __init__.py  
 ┃ ┗ __init__.py  
 ┣ .env  
 ┣ .env-example  
 ┣ .gitignore  
 ┣ alembic.ini  
 ┣ docker-compose.yml  
 ┣ Dockerfile  
 ┣ main.py  
 ┣ README.md  
 ┣ requirements.txt  
 ┗ __init__.py

## Requirements

 - Docker and Docker-compose
 - Git

## Running
1.

`git clone git@github.com:apenasweber/logical-expression-api.git`

2. `cd logical-expression-api`

2. Rename the ".env-example" file to ".env"

3. Run
    `docker-compose up --build`

4. Access http://localhost:8000/docs
5. Click on /login endpoint, Try it out, insert username(postgres) and password(password), finally click on execute.
6. You gonna receive a token: copy it, click on the "Authorize" button on right top of page and paste the token there clicking in Authorize.
7. Now you can use all endpoints authenticated(30 minutes time expiration for token)

## Endpoints
1.  **GET /expressions/** - This endpoint retrieves a list of all expressions stored in the database.
    
2.  **DELETE /expressions/{expression_id}** - This endpoint deletes the expression with the specified `expression_id` from the database. If the expression does not exist, a `404` error is returned with the message "Expression not found".
    
3.  **GET /expressions/evaluate/{expression_id}** - This endpoint evaluates the expression with the specified `expression_id`. The endpoint accepts query parameters `x`, `y`, `z`, `j`, and `k` which are used as the values of variables in the expression. If the expression or the values of variables are invalid, a `400` error is returned with the message "Invalid expression or values".
    
4.  **POST /expressions/expressions** - This endpoint creates a new expression in the database. The expression is passed as a JSON object in the request body. If the creation of the expression is successful, the ID of the newly created expression is returned in the response.

## Model Definition

The `Expression` model is defined in the `models.py` file. It is a representation of a boolean expression that is stored in a database. The model is created using SQLAlchemy's ORM and is defined using a declarative base class.

The `Expression` model has three fields:

-   `id`: This is a unique identifier for the expression and serves as the primary key for the table in the database.
-   `expression`: This field contains the string representation of the boolean expression. It is a required field and cannot be null.
-   `result`: This field contains the result of evaluating the expression. It is of type boolean and can be null, with a default value of `None`.

P.S: used alembic for deal with migrations and creating tables.

## Authentication
The project is implementing a custom authentication scheme using JSON Web Tokens (JWT).

The authentication works as follows:

-   The client sends a request to the API with an "Authorization" header in the format "Bearer <JWT token>".
-   The `JWTBearer` class, which extends the `HTTPBearer` class from the `fastapi` library, checks if the header is present. If not, it raises an exception with a `403` status code and a detail message of "Not authenticated".
-   If the header is present, the class splits the header value into a scheme ("Bearer") and the JWT token (credentials). If the scheme is not "Bearer", it raises an exception with a `403` status code and a detail message of "Invalid authentication scheme".
-   Finally, the `verify_jwt` method is called to validate the JWT token. If the token is invalid or has expired, an exception is raised with a `403` status code and a detail message of "Invalid token or expired token". If the token is valid, the method returns the credentials (the JWT token).

The authentication process can be summarized as follows:

-   The client sends a request with a Bearer token.
-   The server verifies the header and the token.
-   If the header or the token are invalid, the server returns a `403` status code with a message.
-   If the header and the token are valid, the server returns the token.

Note: The `decodeJWT` function used in the `verify_jwt` method is not part of this code and its implementation is not shown. This function is responsible for decoding the JWT token and returning its payload.

## Final Considerations
Unfortunately due to the high demand that I am currently in, I was not able to develop the project as I would like to do it and here are some points that I would certainly do differently:

 - Theres no unit, integration or load tests in my project, different from projects that i create when i have no high demands like: https://github.com/apenasweber/hurb-test
 - The "create expression" endpoint can be better: returning the id of expression inserted, for example.
 - The documentation about the project is confused because it mentions 4 features(**Some things it should be able to to:**) but mention after 3 endpoints, suggesting that we need a endpoint to create and update simultaneously, but thinking about the single responsability its not a good idea, so i didnt came this way.
 - I did just one commit to deliver the application fastly before my second deadline.
