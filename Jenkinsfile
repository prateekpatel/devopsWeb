pipeline {
    agent any
    parameters {
        string (name: 'Deploy_version', description: 'Deploy to this environment')
        string (name: 'role_arn', description: 'role to assume in order to deploy the application')

    }
    stages{
        stage('checkout'){
            steps{
                sh 'git pull cartrwaler'
            }
        }
        stage('Preperation'){
            steps{
                // looking for mandatory files, variables
                sh ''
            }
        }
        stage('Build'){
            steps{
                sh 'pip install requirements.txt'
            }
        }
        stage('Test'){
            steps{
                sh ''
            }
        }
        stage('Sonar Scan'){
            steps{
                sh 'sonarscanner '
            }
        }
        stage('Lint'){
            steps{
                sh ''
            }
        }
        stage('Build Image'){
            steps{
                sh 'docker build -t cartrawler#{buildnumber}'
            }
        }
        stage('Deploy to Dev'){
            steps{
               sh """ansible-playbook  \
               --extra-vars "environment=development version=#{params.Deploy_version} role_arn=#{role_arn}"
               deploy_container.yml -vv"""
            }
        }
    }
    post{
    failure {
        script{
            msg = "Build failed "
        }

    }
    }

}
