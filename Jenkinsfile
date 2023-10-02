pipeline {
  agent any

  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/Ujstor/social-media-fastapi/', branch: 'postgres')
      }
    }

    stage('Prepair enviroment') {
      steps {
        script {
          sh "cp -f /home/fastapi/.env ${WORKSPACE}"
        }
      }
    }

     stage('Create test db') {
      steps {
        script {
          sh "docker run --name postgres-fastapi_test -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=fastapi_test -p 5432:5432 -d postgres:latest" 

        }
      }
    }

    stage('Test') {
      steps {
        script {
          sh "${JENKINS_HOME}/scripts/pytest.sh ${WORKSPACE}"
        }
      }
    }

    stage('Remove test db') {
      steps {
        script {
          sh "docker stop postgres-fastapi_test && docker rm postgres-fastapi_test " 

        }
      }
    }

    stage('Build') {
      steps {
        script {
          sh 'docker build -t ujstor/fastapi .'
        }
      }
    }

    stage('Deploy') {
      steps {
        script {
          sh 'docker push ujstor/fastapi'
        }
      }
    }
  }
}
