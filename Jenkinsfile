pipeline {
    agent any

    stages {

        stage('Setup Virtual Enviorment') {
            steps {
                sh '''
                rm -rf venv  ## Remove any existing virtual env
                python3 -m venv venv  ## Create anew virtual env
                chmod -R 755 venv
                bash -c "
                source venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt

                "
                '''
            }
        }

       
    }
}