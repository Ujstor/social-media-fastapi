pipeline {
    agent any

    environment {
        GITHUB_USER = 'ujstor'
        GITHUB_REPO = 'social-media-fastapi'
        DOCKER_HUB_USERNAME = 'ujstor'
        DOCKER_REPO_NAME = 'fastapi'
        BRANCH = 'master'
        VERSION_PART = 'Patch' // Patch, Minor, Major
        DOCKER_JENKINS_CERDIDENTALS_ID = 'be9636c4-b828-41af-ad0b-46d4182dfb06'
        TAG = ''
    }

    stages {
        stage('Checkout Code') {
            steps {
                script {
                    git(url: "https://github.com/${GITHUB_USER}/${GITHUB_REPO}/", branch: env.BRANCH_NAME)
                }
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
                expression { env.BRANCH_NAME == env.BRANCH}
            }
            steps {
                script {
                    TAG = sh(script: "${JENKINS_HOME}/scripts/docker_tag.sh $DOCKER_HUB_USERNAME $DOCKER_REPO_NAME $VERSION_PART", returnStdout: true).trim()

                    if (TAG) {
                        echo "Docker image tag generated successfully: $TAG"
                    } else {
                        error "Failed to generate Docker image tag"
                    }

                    env.TAG = TAG
                }
            }
        }

        stage('Docker Login') {
            when {
                expression { env.BRANCH_NAME == env.BRANCH }
            }
            steps {
                script {

                    withCredentials([usernamePassword(credentialsId: env.DOCKER_JENKINS_CERDIDENTALS_ID, passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        sh "docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"
                    }
                }
            }
        }

        stage('Build') {
            when {
                expression { env.BRANCH_NAME == env.BRANCH }
            }
            steps {
                script {
                    sh "docker build --no-cache -t ${DOCKER_HUB_USERNAME}/${DOCKER_REPO_NAME}:${TAG} ."
                }
            }
        }

        stage('Deploy') {
            when {
                expression { env.BRANCH_NAME == env.BRANCH }
            }
            steps {
                script {
                    sh "docker push ${DOCKER_HUB_USERNAME}/${DOCKER_REPO_NAME}:${TAG}"
                }
            }
        }

        stage('Environment Cleanup') {
            when {
                expression { env.BRANCH_NAME == env.BRANCH }
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
