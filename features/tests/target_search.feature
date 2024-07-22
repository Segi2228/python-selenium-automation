# Created by lozak at 7/13/2024
  Feature: Search page tests
  Scenario: Search for a product on target
    Given Open Target main page
    When  Search for product
    Then  Verify search worked

