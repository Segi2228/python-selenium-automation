# Created by lozak at 7/13/2024
  Feature: Search page tests
  Scenario: Search for a product on target
    Given Open Target main page
    When  Search for coffee
    Then  Verify search shows for coffee
    Then Verify correct search results URL opens for coffee

