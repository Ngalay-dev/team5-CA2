pipeline {
    agent any

    environment {
        IMAGE_NAME = "calculator-app"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Ngalay-dev/team5-CA2.git'
            }
        }

        stage('Install Dependencies & Run Tests (Quality Gate)') {
            agent {
                docker {
                    image 'python:3.9'
                    args '-u root'
                }
            }
            steps {
                sh '''
                python --version
                pip install --upgrade pip
                pip install -r requirements.txt
                pytest
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t $IMAGE_NAME .
                '''
            }
        }

        stage('Deploy to Docker Swarm') {
            steps {
                sh '''
                docker service rm calculator-service || true
                docker service create \
                  --name calculator-service \
                  --replicas 2 \
                  -p 5000:5000 \
                  $IMAGE_NAME
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded. App deployed to Docker Swarm.'
        }
        failure {
            echo 'Pipeline failed. Deployment blocked by quality gate.'
        }
    }
}

