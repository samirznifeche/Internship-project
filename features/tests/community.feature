# Created by lenovo at 7/19/2025
Feature: Tests for Community Functionality

  Scenario: User can open the community page
    Given Open the sign_in page
    When Log in to the page with valid credentials: 'your_email', 'your_password'
    And Click on the settings option
    And Click on the Community option
    Then Verify the right page opens
    And Verify the “Contact support” button is available and clickable