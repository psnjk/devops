<br />
<p align="center">
  <a href="https://github.com/psnjk/devops">
    <img src="https://github.com/psnjk/meme/blob/master/Music.gif" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Innopolis University F21 Devops</h3>

  <p align="center">
    Devops course repository for practical lab tasks
    <br />
    <a href="https://github.com/psnjk/devops"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/psnjk/devops">View Demo</a>
    ·
    <a href="https://github.com/psnjk/devops/issues">Report Bug</a>
    ·
    <a href="https://github.com/psnjk/devops/issues">Request Feature</a>
  </p>
</p>

# Simple Python Web Application
Jameel Mukhutdinov B18-SE-02
Simple Python web application, that shows current time in Moscow.

## Prerequisites
- Python 3.8+
- pip 21.2.4

## Installation and Usage
Windows
1. ``` git clone https://github.com/psnjk/devops ``` - clone repository
2. ``` cd application ``` - change working directory to ```application```
3. ``` python3 -m venv env ``` - set up virtual envirinment
4. ``` .\env\Scripts\activate ``` - activate it
5. ``` pip3 install -r requirements.txt``` - install requirements
6. ```flask run``` - run the application
7. Open your browser and type in search bar localhost:5000

## Docker
1. ``` cd application ``` - change working directory to ```application```, ```Dockerfile``` is ready here
2. ```docker build --tag python-docker .   ``` - build an image
3. ```  docker images``` - check for an image
4. ``` docker run python-docker ``` - run it

or just ```docker run  -it -p 5000:5000 psnjk/devops:latest```

### Unit tests
to run unit test manually run the following command inside application directory:
```pytest```

## Contributing
1. Fork repository (https://github.com/psnjk/devops/fork)
2. Create your feature branch (git checkout -b feature/fooBar)
3. Commit your changes (git commit -am 'Add some fooBar')
4. Push to the branch (git push origin feature/fooBar)
5. Create a new Pull Request
