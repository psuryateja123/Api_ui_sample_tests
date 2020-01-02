@smoke

Feature: checking the api status

    Scenario: Check accepted or rejected status for John smith
      Given I post the api with John smith json file
      Then I print the John smith result

    Scenario: Check for Karen Jones
      Given I post the api with Karen Jones json file
      Then I print Karen Jones results