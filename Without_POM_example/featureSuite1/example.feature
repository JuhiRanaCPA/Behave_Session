# -- FILE: features/example.feature
Feature: Showing off behave

  Background:
    Given user open the url



  Scenario: Tc1 -Sample Google search testcase
    When user search for python
    And user select python.or site link
    Then user will be on python.or site and the title should be "Welcome to Python.org"


  Scenario: TC2- Sample Google search testcase with parameterization
    When user search for "Python"
    And user select python.or site link
    Then user will be on python.or site and the title should be "Welcome to Python.org"


  Scenario: TC2- Sample Google search testcase with parameterization
    When user search for "Selenium"
    And user select python.or site link
    Then user will be on python.or site and the title should be "Welcome to Python.org"


  Scenario Outline: TC3- Sample Google search testcase for with parameterization
    When user search for "<search_text>"
    And user select "<link>" site link
    Then the title should be "<Title>"
    Examples:
      | search_text | Title                 | link       |
      | python      | Welcome to Python.org | python.org |
      | India       | India - Wikipedia     | wikipedia  |





