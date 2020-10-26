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
                withEnv(["PYTHONPATH=:${env.WORKSPACE}/batchjob/"]){
                    sh 'bash -x -e jenkins/run_unit_tests.sh'

                }
                  
            }       
            "linting": {
                    sh 'bash -x -e jenkins/run_linting.sh'
            }

        }
    }
  }
}
