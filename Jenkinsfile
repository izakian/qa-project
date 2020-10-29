pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('unittest and linting')
    {
        parallel{
            "unittesting": {
                    sh 'bash -x -e jenkins/run_unit_tests.sh'
            }
            "linting": {
                    sh 'bash -x -e jenkins/run_linting.sh'
            }

        }
    }
  }
}
