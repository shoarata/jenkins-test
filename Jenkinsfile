pipeline{
    agent{
        node{
            label 'agent-python'
        }
    }
    triggers{
        pollSCM '* * * * *'
    }
    stages{
        stage('build'){
            steps{
                sh """
                    echo "Building step...."
                    pip install -r requirements.txt
                    sleep 0.5
                """
            }
        }
        stage('Test'){
            steps{
                sh """
                    echo "Testing step...."
                    sleep 0.5
                """
            }
        }
        stage('Deploy'){
            steps{
                sh """
                    echo "Running app"
                    ls
                    cd jenkins-test
                    python3 simple-cli.py hello --name="Kim"
                    python3 simple-cli.py sum_list --numbers="[1,2,3]"
                    python3 simple-cli.py multiply 2 4
                    sleep 0.5
                """
            }
        }
    }
}
