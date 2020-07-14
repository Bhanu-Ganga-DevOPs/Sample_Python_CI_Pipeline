pipeline {
    agent { dockerfile true }
    options {
        buildDiscarder(
            logRotator(numToKeepStr:'5'))
    }
    stages {
        stage('Test') {
            steps {
                sh 'coverage run -m pytest --junitxml=testResults.xml'
            }
        }
    }
    post {
        always {
            junit 'testResults.xml'
            sh 'coverage xml -o coverage.xml'
            cobertura coberturaReportFile: 'coverage.xml'
            archiveArtifacts artifacts: 'testResults.xml', fingerprint: true
            archiveArtifacts artifacts: 'coverage.xml', fingerprint: true
        }
    }
}