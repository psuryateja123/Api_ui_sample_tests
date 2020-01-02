
  Feature:  Navigating to test page and checking for UI elements

    Scenario: Check for check button
      Given I navigate to test page
      Then I check for checkbox
      Then I click Remove button
      Then the checkbox should disappear
      And I click add button
      Then the checkox should reappear


    Scenario: check for enable/diable button
      Given I navigate to test page
      Then I check the text field status
      Then I click on enable button
      And I check the status
      Then I click on enable button
      And I check the current status