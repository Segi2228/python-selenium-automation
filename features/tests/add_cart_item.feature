# Created by lozak at 7/15/2024
Feature: Add item to cart tests

  Scenario: Users can add a product to cart
    Given Open Target main page
    When Search for teatree oil
    Then Click on Add to Cart button
    And store product name
    Then Add item to cart
    And View cart
    #Then Open Cart page
    Then Verify cart has the item