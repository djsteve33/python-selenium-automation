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

    Scenario: User can add a product to the cart
    Given Open Amazon page
    When Input text clock
    When Click on search button
    And Click on the first product
    When Click on Add to cart button
    And Open cart page
    Then Verify that text Clock is shown

   Scenario: User can select and search in a department
    Given Open Amazon page
    When Select department by alias movies-tv
    When Input text Top Gun
    When Click on search button
    Then Verify movies-tv department is selected

  Scenario: User can see clothing options
    Given Open Amazon product B07YP9JK3F page
    When Hover over New Arrival options
    Then Verify Women option present