pipeline {
  agent { docker { image 'python:3.7.3' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('unittest') {
      steps {
        sh 'jenkins/run_unit_tests.sh'
      }   
    }
    stage('linting') {
      steps {
        sh 'jenkins/run_linting.sh'
      }   
    }
  }
}
