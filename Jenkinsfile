pipeline {
    agent any

    environment {
        DOCKER_HUB_USERNAME = 'ujstor'
        DOCKER_REPO_NAME = 'fastapi'
        VERSION_PART = 'Patch' // Patch, Minor, Major
        TAG = ''
    } 

    stages {
        stage('Checkout Code') {
            steps {
                git(url: 'https://github.com/Ujstor/social-media-fastapi/', branch: env.BRANCH_NAME)
            }
        }

        stage('Prepare Environment') {
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
                    sh "docker stop postgres-fastapi_test && docker rm postgres-fastapi_test"
                }
            }
        }

        stage('Generate Docker Image Tag') {
             when {
                expression { env.BRANCH_NAME == 'master' }
            }
            steps {
                script {
                    TAG = sh(script: "/var/lib/jenkins/scripts/docker_tag.sh $DOCKER_HUB_USERNAME $DOCKER_REPO_NAME $VERSION_PART", returnStdout: true).trim()

                    if (TAG) {
                        echo "Docker image tag generated successfully: $TAG"
                    } else {
                        error "Failed to generate Docker image tag"
                    }

                    env.TAG = TAG
                }
            }
        }

        stage('Build') {
            when {
                expression { env.BRANCH_NAME == 'master' }
            }

            steps {
                script {
                    sh "docker build --no-cache -t ${DOCKER_HUB_USERNAME}/${DOCKER_REPO_NAME}:${TAG} ."
                }
            }
        }

        stage('Deploy') {
            when {
                expression { env.BRANCH_NAME == 'master' }
            }

            steps {
                script {
                    sh "docker push ${DOCKER_HUB_USERNAME}/${DOCKER_REPO_NAME}:${TAG}"
                }
            }
        }

        stage('Environment Cleanup') {
            when {
                expression { env.BRANCH_NAME == 'master' }
            }

            steps {
                script {
                    sh "docker rmi ${DOCKER_HUB_USERNAME}/${DOCKER_REPO_NAME}:${TAG}"
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully"
        }
    }
}
