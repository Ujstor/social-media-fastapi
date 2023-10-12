# FastAPI Project

![](https://i.imgur.com/jPqQa5E.png)

# Testing
You can test the API using docs at deployed version: https://fastapi.astipan.com/docs or  https://fastapi.astipan.com/redoc

Another option is to use [Postman](https://www.postman.com/ujstor/workspace/fastapi-test/) collection or import colection in local Postman app (.json file in the repo); create fork and in environment variables set `URL` to `https://fastapi.astipan.com/` , also you need JWT token variable, copy this code in Login user - Tests tab:
```js
pm.environment.set("JWT", pm.response.json().access_token);
```

![Variables](https://i.imgur.com/urKV3Gk.png)
<br>
<br>
![JWT](https://i.imgur.com/3RBG6cR.png)
<br>
<br>
### Create user
![](https://i.imgur.com/iODzIXx.png)
<br>
<br>
### Login
![](https://i.imgur.com/9q9MSdZ.png)
<br>
<br>
### Test endpoints
![](https://i.imgur.com/IWlNzYM.png)
<br>
<br>
# Local deployment
Running the API locally is simple, just clone the repo, create virtual environment and install requirements. Create .env file with following variables:
```
DATABASE_HOSTNAME=
DATABASE_PORT=
DATABASE_NAME=
DATABASE_USERNAME=
DATABASE_PASSWORD=
SECRET_KEY=9009eb7770b5d012179802a09ddc5484ecde87e730f86b5dffce30c78564c50c
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
Create database and run migrations with `alembic upgrade head`.
<br>
Then run `uvicorn app.main:app --reload` and you are good to go.
<br>
You can test endpoints with POSTMAN or docs at http://localhost:8000/docs.
<br>
<br>

# Docker

To build the Docker image from the code, run:

```
docker compose -f .\docker-compose-dev.yml up
```

If you want to pull the image from the Docker repository instead, use:

```
docker compose -f .\docker-compose-prod.yml up
```

Image is automatically built and deployed through the Jenkins pipeline after changes in GitHub, and it expects a .env file for loading variables.

<br/>

![](https://i.imgur.com/o7SnJvi.png)

# Jenkins Pipeline


Pipeline is designed to automate the build, test and deployment of a FastAPI application stored in a GitHub repository. It performs a series of steps to build and deploy the application, as well as run tests and generate Docker image tags. 



## Pipeline Execution Conditions

- The pipeline stages related to Docker image generation, building, deployment, and cleanup only run when the branch being built is 'master.' This is controlled by the `when` expressions in the respective stages.

## Post-build Actions

- If the pipeline runs successfully, a message is printed to indicate the completion of the pipeline.

This Jenkins pipeline streamlines the continuous integration and deployment process for a FastAPI application and offers flexibility in managing versioning and Docker image deployment. It can be customized further based on specific project requirements and integrations.



# Pytest
To run tests, you need manually create test database, just add `_test` to new database (fastapi;  fastapi_test). At each test run, the database is cleared and the data is reloaded from the fixtures. To run tests, use `pytest -v -s` command.
<br>
<br>
![](https://i.imgur.com/vsiTQZc.png)
<br>
<br>


# Project Overview

This comprehensive project on developing a RESTful API using FastAPI is structured around several key themes:

1. **FastAPI Basics**: This part provides a foundation of working with FastAPI, including handling different types of path operations, managing HTTP requests, applying data validation using Pydantic, and implementing CRUD operations. The significance of the path operation order and Postman for API testing are also covered.

2. **Working with Databases**: This section is dedicated to databases, explaining SQL queries, operations, and filters, along with managing databases using PgAdmin GUI. Database integration with Python for creating and retrieving posts is another focus of this section.

3. **Python and Raw SQL**: Here, the project explores setting up an application database and how to connect to it using Python. It then goes on to manage (retrieve, create, delete, and update) posts via the database.

4. **Object-Relational Mapping (ORM)**: This part of the project introduces ORMs, setting up SQLAlchemy and adding extra functionality to it. It also demonstrates how to manage posts using SQLAlchemy.

5. **Pydantic Models**: This section delves into the differences between Pydantic and ORM models and gives a detailed explanation of Pydantic Models.

6. **Authentication & Users**: This part handles user-related operations such as creating user tables, registering users, hashing passwords, retrieving user data, and managing JWT tokens for user authentication.

7. **Database Relationships**: The focus here is on SQL relationships, foreign keys, updating post schemas, managing ownership of posts, and the concept of SQLAlchemy relationships.

8. **Vote/Like System**: This part covers the creation of a voting system for the posts, explaining how to manage votes on the database level and with SQLAlchemy.

9. **Database Migration with Alembic**: This section introduces the concept of database migration tools and shows how to set up and use Alembic for database schema revisions.

10. **Testing**: This part emphasizes writing effective tests for the API, working with Pytest, handling database interactions in tests, and testing user authentication.

11. **Continuous Integration/Continuous Deployment (CI/CD) pipeline**: The final section of the project introduces CI/CD concepts, working with GitHub Actions.
