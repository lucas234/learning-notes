import hudson.tasks.test.AbstractTestResultAction

@NonCPS
def testStatuses() {
    def testStatus = ""
    AbstractTestResultAction testResultAction = currentBuild.rawBuild.getAction(AbstractTestResultAction.class)
    if (testResultAction != null) {
        int total = testResultAction.totalCount
        int failed = testResultAction.failCount
        int skipped = testResultAction.skipCount
        int passed = total - failed - skipped
        testStatus = "Test Status:\n  Passed: ${passed}, Failed: ${failed}, Skipped: ${skipped}"
    }
    return testStatus
}

pipeline{
    agent any
    tools {
        maven 'M 3'
    }
    stages{
        stage("checkout code"){
            steps {
                script{
                    //pull your code
                    echo "just a test"
                }}
        }
        stage("run test case"){
            steps {
                script{
                    //withMaven(maven: 'M 3') {
                    //			bat 'mvn test'
                    //		}
                    echo 'run test cases'
                    bat 'mvn test'
                    // bat 'mvn test -Dcucumber.options="--tags @test"'
                }}
        }

    }
    post('Generate report') {
        always {
            script{
                cucumber fileIncludePattern: '**/cucumber-default-reports/*.json', sortingMethod: 'ALPHABETICAL'

                junit '**/cucumber-default-reports/*.xml' //必须有这一步，否则没有数据    
                echo 'API and Android APP Test Result: ' + env.JOB_NAME + '-' + env.BUILD_NUMBER + " \n" + testStatuses()
                emailext subject: "Automation Result5: Job '${env.JOB_NAME} - ${env.BUILD_NUMBER}'",
                        body:'''${SCRIPT,template="groovy-html-larry-refactor.template"}''',
                        to:'$DEFAULT_RECIPIENTS'

                emailext subject: "Automation Result6: Job '${env.JOB_NAME} - ${env.BUILD_NUMBER}'",
                        body:''' ${SCRIPT,template="groovy-html-refactor.template"}''',
                        to:'$DEFAULT_RECIPIENTS'

                emailext subject: "Automation Result: Job '${env.JOB_NAME} - ${env.BUILD_NUMBER}'",
                        body:'''  
                      total:${TEST_COUNTS,var="total"},
                      pass:${TEST_COUNTS,var="pass"},
                      fail:${TEST_COUNTS,var="fail"}
                   ''',
                        to:'$DEFAULT_RECIPIENTS'
            }
        }
    }

}
