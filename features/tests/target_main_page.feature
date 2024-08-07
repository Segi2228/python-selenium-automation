# Created by lozak at 7/4/2024
Feature: Test Scenarios for  Target main page

  Scenario: Search for a product on target
    Given Open Target main page
    When  Search for coffee
#    Then  Verify search shows for coffee
#    Then Verify correct search results URL opens for coffee


  Scenario: Sign in page opens
     Given Open Target main page
     When Click on Sign In icon
     When Click on Sign In icon again
     Then Sign in form opens


  Scenario: Empty cart message displays
    Given Open Target main page
    When  Click on Cart icon
    Then  Your cart is empty message shown

