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
                if (testResult == 'Failed') {
                    error "test failed"
        }
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
            parallel {
                stage("Buidl Image Kubernetese") {
                    when{
                        expression {params.deployment_type == "kubernetse"}
                    }
                    steps{
                        sh 'docker build -t cartrawler#{buildnumber}'
                }
                }
                stage("Buidl Image aws") {
                    when{
                        expression {params.deployment_type == "aws"}
                    }
                    steps{
                        sh 'docker build -t #{param.ecrendpoint}cartrawler#{buildnumber}'
                }
                }

            
            }
        
        stage('Push Image'){
                when {
                   expression { params.deployment_type == "kubernetse" }
                }
                steps{
                sh 'docker push cartrawler#{buildnumber}'
            }
        
        stage('Push Image ECR'){
                when {
                   expression { params.deployment_type == "aws" }
                }
                steps{
                sh 'docker push cartrawler#{buildnumber}'
            }
        
        }

        stage ('prepare variable for dev deployment'){
            when{
                expression { params.deployment_type == "aws" }
            steps {
                sh '''
                echo "region: ${REGION}" > extra_vars.yml
                echo "account_id: ${REGION}" >> extra_vars.yml
                echo "security_group: ${SECURITY_GROUP}" >> extra_vars.yml
                echo "subnet: ${SUBNET}" >> extra_vars.yml
                echo environment: development  >> extra_vars.yml
                echo  version  : #{params.Deploy_version}
                echo role_arn: #{params.role_arn}

                '''
            }

            }
        }
        stage('Deploy to Dev'){
            steps{
               sh '''ansible-playbook  
               --extra-vars "@extra_vars.yml"
               deploy_container.yml -vv --tag "#{params.deployment_type}'''
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
