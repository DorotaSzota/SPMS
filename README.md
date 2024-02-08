# Santa's Package Management System

Santa has asked you to create a system for managing packages. The system should allow for adding new packages and assigning them to the appropriate elves. Additionally, a system for managing elves would be useful. It would be great if the elves could have options for managing their time off, including maternity/paternity leave. To ensure Santa can use the system from anywhere in the world, it should be deployable using Docker and DockerHub. Santa offers additional points for setting up a CI/CD workflow. While the choice of deployment service is less critical, DigitalOcean with the option of free $200 credits for GitHub Student is recommended.

## Technical Details:

1. **WebService:** We recommend using FastAPI with basic CRUD operations for Elves and Items.
2. **Database:** Connecting the service to a database is necessary. You can use SQL Lite, Postgres, or any other database according to preference.
3. **Deployment:** Deploy using DockerHub, and utilize DigitalOcean as the IAAS platform. The choice of deployment service is important for configuring the environment.

## Additional Information:

- **Documentation:** Create documentation in the form of a README.md file for the project. It should include instructions for installation, startup, deployment process, etc.
- **Continuous Delivery (CD):** Configure CI/CD using GitHub Actions and DockerHub for automation of the delivery process.

Make sure to maintain clarity and comprehensibility for potential users, including Santa, throughout the development process and documentation.

## Dependencies
All Python dependencies are in the requirements.txt file.

## Prerequisites
Before starting work on the project you must install all needed dependencies:
    pip install -r requirements.txt

# How to
## How to run the app for the first time
    uvicorn main:app 

## How to run the app with hot reload
    uvicorn app.main:app --reload

## How to pull and run docker image
    docker pull owcen/pyt15:latest
    docker run -p 8000:8000 owcen/pyt15

## How to build and run docker image
    docker build -t pyt15 .
    docker run -p 80:80 pyt15

## Swagger UI 
    127.0.0.1:8000/docs