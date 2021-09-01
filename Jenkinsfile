pipeline {
    environment {
        APP_PATH = 'application'
    }

    agent {
        docker {
            image 'python:3.8-slim-buster'
            args '-u root -v $HOME/.cache:/root/.cache -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    stages {
        stage('setup') {
            steps {
                dir("${APP_PATH}"){
                    sh"""
                    pip3 install -r requirements.txt
                    apt-get update && apt-get install -y docker.io
                    """
                }
            }
        }

        stage('Linting') {
             steps {
                 dir("${APP_PATH}") {
                     sh "flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics"
                     sh "flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics"
                 }
             }
         }

        stage('Unit Testing') { 
            steps {
                dir("${APP_PATH}"){
                    sh """
                    python -m pytest
                    """
                }
                }
            }

    }
}