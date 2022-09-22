<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h1 align="center">Reddit Clone</h1>

  <p align="center">
    A clone of the reddit website
    <br />
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project

![RedditClone](https://github.com/kpp16/RedditClone/blob/main/ScreenShotFakeReddit.png)

This is a simple clone website of reddit.com


### Built With
1. Python: FastAPI
2. React.JS with TypeScript
3. PostgreSQL


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```
  
* React
  ```sh
  npx install create-react-app@latest -g
  ```

* Python: https://www.python.org/downloads/

* PostgreSQL: https://www.postgresql.org/download/


### Installation

To install this website in your local machine, follow the below steps:

1. Create and setup a PostgreSQL server and make a .env listing the database credentials

2. Clone the repo
   ```sh
   git clone https://github.com/kpp16/RedditClone.git
   ```
  
3. Install NPM packages
   ```sh
   cd frontend
   npm install
   ```
   
4. Make a python virtual environemnt and install the packages
   ```sh
   cd backend
   python3 -m venv myenv
   source myenv/bin/activate
   pip install fastapi uvicorn sqlalchemy
   ```

## Usage

To run this website locally,

1. Start the frontend server
```sh
cd frontend
npm start
```
2. Start the backend server
```sh
cd backend
uvicorn app.main:app --reload
```

3. Visit `localhost:8000` in your browser
