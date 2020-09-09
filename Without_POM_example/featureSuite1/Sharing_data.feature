# demo to show how to pass around data from step to step

Feature: Sharing data globally

    Scenario: scenario one where we are assigning value to a variable in a step and will access the the value in further steps
        Given Creating a new variable and assign a value to it
        When Trying to access the value of userName in second step
        And Now I try to update the value of username
        Then Updated value of user name is XYZ

    Scenario: Scenario two where we try to access the context variable which we have defined in previous testcase
        When Trying to access the value of userName in second step
        Then previous step should fail