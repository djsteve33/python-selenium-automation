# Created by swomb at 3/7/2023
Feature: Amazon search tests
  # Enter feature description here

  Scenario: User can see Sign In button
    Given Open Amazon page
    When Click on Orders
    Then Verify Sign in header is visible
    Then Verify email input field is present


  Scenario: User can see their cart is empty
    Given Open Amazon page
    When Click on cart icon
    Then Verify cart is empty
