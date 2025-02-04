pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/chaitanya3105/CoinKeeper.git'
            }
        }
        stage('Run Shell Script') {
            steps {
                sh 'chmod +x fetch_data.sh'
                sh './fetch_data.sh'
            }
        }
        stage('Archive CSV') {
            steps {
                archiveArtifacts artifacts: 'repo_data.csv', fingerprint: true
            }
        }
    }
}
