pipeline {
    agent any
    parameters {
        choice(
            choices: ['greeting' , 'silence'],
            description: '',
            name: 'REQUESTED_ACTION')
    }
    environment {
        localCommit = bat(returnStdout: true, script: 'git log -n 1 --pretty=format:%%H').trim()
        remoteCommit = bat(returnStdout: true, script: 'git log origin/dev -n 1 --pretty=format:%%H').trim()
        def slc = localCommit.substring(localCommit.lastIndexOf("H") + 1, localCommit.length())  
        def src = remoteCommit.substring(remoteCommit.lastIndexOf("H") + 1, remoteCommit.length())    

    }
    

    stages {
        stage('test'){
            steps{
                script{
                    echo localCommit
                    echo remoteCommit
                    echo slc
                    echo src
                    branch=bat(returnStdout: true, script: 'git rev-parse --abbrev-ref HEAD').trim()
                    echo branch
                }
            }
        }
        stage ('pull code') {
            when {
                // Only say hello if a "greeting" is requested
                // expression { params.REQUESTED_ACTION == 'greeting' }
                expression { slc == src }
            }
            steps {
                echo "Hello, bitwiseman!"
            }
        }
    }
}