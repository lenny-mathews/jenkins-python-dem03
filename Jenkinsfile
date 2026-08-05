node {
    stages{

        stage('Checkout') {
            git branch: 'main', url: 'https://github.com/lenny-mathews/jenkins-python-demo2.git'

            echo 'Code Checkout	Completed..'
        }
        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Run Application') {
            
            sh '''
               python3 -m venv venv
               . venv/bin/activate  
               . venv/bin/python3 -m pip install --upgrade pip
               . venv/bin/pip3 install -r requirements.txt
            
            '''
        }
        stage('Run Test') {
            steps {
                echo 'Running tests...'
                sh '''
                    . venv/bin/python3 -m pytest test_app.py
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying ..'
                sh '''
                      nohup . venv/bin/python3 -m app.py &
                      sleep 5
                      echo "Deployment successful ... Application is running in the background" 
                    '''   
            }
        }
                      

        stage('Test Jenkins Python Deployment') {
            steps {
                echo 'Testing the deployed website...'

                sh '''curl --fail http://localhost:5001||exit 1 
                      echo "Jenkins Python Deployment test successful ... Website is accessible" 
                      '''
            }
        }
    }
}