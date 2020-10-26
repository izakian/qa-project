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
            stage('unittest') {
                steps {
                    echo "unit testing..."
                    sh 'jenkins/run_unit_tests.sh'
                }   
            }       
            stage('linting') {
                steps {
                    echo "linting..."
                    sh 'jenkins/run_linting.sh'
                }   
            }

        }
    }
  }
}
