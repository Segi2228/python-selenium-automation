# Created by lozak at 7/12/2024
  Feature: Cart check tests

Scenario: Empty cart message displays
    Given Open Target main page
    When  Click on Cart icon
    Then  Your cart is empty message shown