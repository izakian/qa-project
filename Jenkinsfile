pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        echo "*************************"
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        echo "*************************"
      }   
    }
  }
}
JENKINSFILE