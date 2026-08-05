node {
    stages{

        stage('Checkout') {
            git branch: 'main', url: 'https://github.com/lenny-mathews/jenkins-python-demo2.git'

            echo 'Code Checkout	Completed..'
        }
        stage('Install Dependencies') {
            
                echo 'Installing dependencies...'
                sh '''
                 python3 -m venv venv
               . venv/bin/activate  
               . venv/bin/python3 -m pip install --upgrade pip
               . venv/bin/pip3 install -r requirements.txt
                '''
            
        }
        stage('Run Application') {
            echo 'Running the Application '
            sh '''
                    . venv/bin/python3 -m pytest test_app.py
                '''
            }
        }
        stage('Run Test') {
            
                
                sh '''
                    echo 'Running tests...'
                    . venv/bin/python3 -m pytest test_app.py
                '''
            
        }

        stage('Deploy') {

                
                sh '''
                      echo 'Deploying ..'
                      nohup . venv/bin/python3 -m app.py &
                      sleep 5
                      echo "Deployment successful ... Application is running in the background" 
                    '''   
        }
                      

        stage('Test Jenkins Python Deployment') {
 
                sh '''curl --fail http://localhost:5001||exit 1 
                      echo "Jenkins Python Deployment test successful ... Website is accessible" 
                   '''
                echo 'Testing the deployed website...'
            }
        }
    }
}
