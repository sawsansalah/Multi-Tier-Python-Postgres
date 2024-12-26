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

         stage('Tests') {
            steps {
                sh '''
                bash -c "
                          source venv/bin/activate
        
                          pytest  --cov=app --cov-report=xml  

                "
                

                '''
            }
        }



    stage('SonarQube Analysis') {
        steps {
        withSonarQubeEnv('sonar-server') {

        sh ''' 
        $SCANNER_HOME/bin/sonar-scanner -Dsonar.projectName=python-project \
        -Dsonar.projectKey=python-project \
        -Dsonar.sources=. \
        -Dsonar.exclusions=venv/**\

        -Dsonar.python.coverage.reportPaths=coverage.xml 
        '''


        }
        }
        }



       
    }
}