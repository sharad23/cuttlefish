pipeline {
    agent none
    stages {
        stage('Test') {
            agent {
                docker {
                    image 'python:3'
                }
            }
            steps {
                sh 'pip install pipenv'
                sh 'cd modana'
                sh './manage.py'
            }
        }
    }
}