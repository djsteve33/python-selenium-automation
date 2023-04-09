# Created by swomb at 4/8/2023
Feature: Amazon Privacy Notice tests
  # Enter feature description here

  Scenario: User can open and close Amazon Privacy Notice
   Given Open Amazon T&C page
   When Store original windows
   Then Click on Amazon Privacy Notice link
   When Switch to newly opened window
   Then Verify Amazon Privacy Notice page is opened
   When User can close new window and switch back to original