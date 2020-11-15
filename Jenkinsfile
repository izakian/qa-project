pipeline {
  agent {
    docker {image 'python:3'}
  }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('unit-tests') {
      steps {
        sh 'bash jenkins/run_unit_tests.sh'
      }  
    }
  }
}
