# Created by lozak at 8/3/2024
Feature: Tests for Target App page

  Scenario: User is able to open Privacy Policy
    Given Open Target App page
    And  Store original window
    When Click Privacy Policy link
    And  Switch to new window
    Then Verify Privacy Policy page opened
    And  Close current page
    And  Return to original window


  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open Target App page
    When Click on Sign In icon
    When Click on Sign In icon again
    Then  Store original window
    Then Click on Target terms and conditions link
    And  Switch to new opened window
    Then Verify Terms and Conditions page is opened
    And  Close current page
    And Return to original window
