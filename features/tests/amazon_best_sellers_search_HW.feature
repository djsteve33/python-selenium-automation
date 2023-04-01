# Created by swomb at 3/26/2023
Feature: Amazon best sellers tests
  # Enter feature description here

  Scenario: User can see 5 links
    Given Open Amazon page
    When Click on Best Sellers link
    Then Verify there are 5 links

    