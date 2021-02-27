pipeline {
agent any
stages {
    stage('pull from git') {
        steps {
            bat 'git.exe clean -ffdx'
            bat 'git clone https://github.com/isaacTadela/dev_project_3'
        }
    }
    stage('rest app') {
        steps {
            bat 'pip install -r requirements.txt'
			bat 'start /min python rest_app.py'
        }
    }
    stage('testing backend') {
        steps {
			bat 'python backend_testing.py'
        }
    }
    stage('clean environment') {
        steps {
			sleep(5)
            bat 'python clean_environment.py'
        }
    }
    stage('build image') {
        steps {
            bat 'docker build -t iitzhakk/dev_proj_3 .'
        }
    }
    stage('push image') {
        steps {
			bat "echo IMAGE_TAG=${env.BUILD_NUMBER}>.env"
			bat "more .env"
            bat 'docker push -q iitzhakk/dev_proj_3'
        }
    }
    stage('docker-compose up') {
        steps {
			bat 'docker-compose up -d'
        }
    }
    stage('testing docker-compose') {
        steps {
            bat 'python docker_backend_testing.py'
        }
    }
    stage('clean docker environment') {
        steps {
            bat 'docker-compose down -v --rmi all'
        }
    }
 }
 post {
        always {
            echo 'One way or another, I have finished'
			bat 'git.exe clean -ffdx' /* clean up our workspace */
        }
        success {
            echo 'I succeeded!'
        }
        failure {
            echo 'I failed :('
        }
    }
}