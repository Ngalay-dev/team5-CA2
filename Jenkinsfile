pipeline {
    agent any

    environment {
        IMAGE_NAME = "calculator-app"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup Python Virtual Environment') {
            steps {
                sh '''
                python3 --version
                python3 -m venv venv
                venv/bin/pip install --upgrade pip
                venv/bin/pip install -r requirements.txt
                '''
            }
        }

        

        stage('Run Tests (Quality Gate)') {
            steps {
                sh '''
                . venv/bin/pytest
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

        // OPTIONAL — only keep this if Swarm is running locally
        stage('Deploy to Docker Swarm') {
            when {
                expression { sh(script: 'docker info | grep -q Swarm', returnStatus: true) == 0 }
            }
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
            echo ' Pipeline succeeded. Tests passed and app built.'
        }
        failure {
            echo ' Pipeline failed. Deployment blocked by quality gate.'
        }
    }
}


