# Module450_Labo1_MC_JG

Simple application for the first laboratory of module 450

## Tests state

![Run Tests](https://github.com/Morgane8/Module450_Labo1_MC_JG/actions/workflows/ci.yml/badge.svg)

## Product specification

The prupose of this app is to control if an email address is valid or not by :

- check if there is a '@' sign, and only one.

- check if there is at least a name, lastname or nickname before the '@' sign.

- check if there is a domain name and a suffix (such as '.com'), after the '@' sign.

Example of a valid email address : morgane@epsic.com

> ### User story 1 : email validation
>
> As an user, I want to be able to give my email address in order to check if it is valid or not.
>
> **_Acceptance criteria :_**
>
> 1.  check if there is a '@' sign, and only one.
> 2.  check if there is at least a name, lastname or nickname before the '@' sign.
> 3.  check if there is a domain name and a suffix (such as '.com'), after the '@' sign.

## Dependencies

- Python 3: [Python 3 download](https://www.python.org/downloads/)
- pytest : [Pytest documentation](https://pypi.org/project/pytest/)
- Docker desktop: [Docker Desktop download](https://www.docker.com/products/docker-desktop/)

## Installation

The application is made to be Dockerized.

So you don't have to create any python vitrual environment on your machine.

Instead, first clone the repositors on your computer (since we use docker, it can be under any OS).

Then, navigate to the root folder of the app.

Here, use the following command to build the docker image (replace 'my-image-name' by the desired name) :

```bash
docker build -t my-image-name .
```

You can confirm that the image was correctly built by typing :

```bash
docker images
```

Ensure that the name your provided to your image is present in the given list.

## Usage

Now, to run the application itself, use the following command :

```bash
docker run -it my-image-name
```

Note that it is very important to give the `-it` flag, or you will not be able to give inputs to the program.

After that, the program will be launched.

You'll see two diferent options here :

- test your own email address

- exit the app

You can run as many iteration as you wish until you exit the app.

## Tree structure (will evolve during development)

```
├── .dockerignore
├── .gitignore
├── Dockerfile
├── main.py
├── README.md
├── requirements.txt
├── tests
│   ├── test_checkers.py
│   ├── __init__.py
├── verify
│   ├── checkers.py
├── .github
│   ├── workflows
│   |       ├── ci.yml
```

## Access test logs

Once you push your code to GitHub, the tests run automatically using GitHub Actions. You can access the test logs by following these steps:

- Go to the GitHub Repository

- Open the repository where the tests are set up.
  Navigate to the Actions Tab

- Click on the "Actions" tab in the top navigation bar.
  Select the Latest Workflow Run

- You'll see a list of workflow runs (automated test executions).
  Click on the most recent run that corresponds to the latest commit.
  View the Job Details

- Inside the workflow, you'll find different jobs (e.g., "Run Tests").
  Click on the "Run Tests" or a similarly named job.
  Check the Logs

- Scroll down to view the logs. If a test failed, GitHub Actions will highlight the errors.

### Test logs link

Use the following link the directly go to the test log related page.

[View Test Runs](https://github.com/Morgane8/Module450_Labo1_MC_JG/actions)

## Credits

Morgane Cachin and Jonathan Gabioud
