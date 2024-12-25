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

         stage('Tests') {
            steps {
                sh '''
                bash -c "
                source venv/bin/activate
        
                pytest  --cov=app -cov-report=xml  ##run test cases that inside app folder and provide result as xml
 
                pytest  --cov=app  --cov-report=term-missing  --disable-warnings  ##run test case only in ui without report

                "

                '''
            }
        }

       
    }
}