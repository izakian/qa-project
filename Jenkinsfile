pipeline {
    agent any
    stages {
        stage('test') {
            environment {
                THING = 'foobarbuzz'
            }
            steps {
                echo "blah"
                echo "foobarbuzz"
                echo "foobarZZZbuzz"
                echo "This is a $THING here"
            }
        }
    }
}