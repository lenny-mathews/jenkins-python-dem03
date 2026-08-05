node {


        stage('Checkout') {
            git branch: 'main', url: 'https://github.com/lenny-mathews/jenkins-python-demo2.git'

            echo 'Code Checkout	Completed..'
        }

        
        stage('Install Dependencies') {
            
                echo 'Installing dependencies...'
                sh '''
                 python3 -m venv .venv
                 
                 .venv/bin/python3 -m pip install --upgrade pip
                 .venv/bin/python3 -m pip install -r requirements.txt
                '''
            
        }
        
        stage('Run Test') {
                  
                sh '''
                    echo 'Running tests...'
                    .venv/bin/python3 -m pytest3 -v
                '''
            
        }
        
        stage('Run Application') {
            echo 'Running the Application '
            sh '''
                    nohup .venv/bin/python3  -m app.py &
                    echo $! > app.id
                    sleep 5
                    cat app.id
                    echo 'Application deployed sucessfully'
                '''
            }
        
   

        stage('Test Jenkins Python Deployment') {
 
                sh '''curl --fail http://localhost:5001||exit 1 
                      echo "Jenkins Python Deployment test successful ... Website is accessible" 
                   '''
                echo 'Testing the deployed website...'
            }
        }
    
