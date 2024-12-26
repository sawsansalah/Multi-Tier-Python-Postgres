pipeline {
    agent any
    
     environment{ 
 SCANNER_HOME= tool 'sonar-scanner' 
 }

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

      stage('Test') {
            steps {
            sh '''
            bash -c "
            source venv/bin/activate
            pytest --cov=app --cov-report=xml
            pytest --cov=app --cov-report=term-missing --disable-warnings
            "
            '''
    }
    }
    
    stage('Sonar') {
    steps {
    withSonarQubeEnv('sonar-server') {
    sh ''' $SCANNER_HOME/bin/sonar-scanner -Dsonar.projectKey=python-project \
    -Dsonar.projectName=python-project \
    -Dsonar.exclusions=venv/** \
    -Dsonar.sources=. \
    -Dsonar.python.coverage.reportPaths=coverage.xml'''
    }
    }
    }
    }
    }