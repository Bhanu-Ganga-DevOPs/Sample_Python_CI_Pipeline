pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
                sh 'coverage run -m pytest --junitxml=testResults.xml'
            }
        }
    }
    post {
        always {
            steps {
                junit 'testResults.xml'
                sh 'coverage xml -o coverage.xml'
                cobertura coberturaReportFile: 'coverage.xml'
                archiveArtifacts artifacts: 'testResults.xml', fingerprint: true
                archiveArtifacts artifacts: 'coverage.xml', fingerprint: true
            }
        }
    }
}