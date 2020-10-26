pipeline {
  agent {docker {image 'python:3.7.3'}}
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('unittest and linting')
    {
        parallel{
            failFast: true,
            "unittesting": {
                    sh 'nosetests src/'
            }
            "linting": {
                    sh 'bash -x -e jenkins/run_linting.sh'
            }

        }
    }
  }
}
