# Created by lenovo at 8/29/2025
Feature: Tests for Secondary Functionality

  Scenario: User can filter the Secondary deals by "want to sell" option
    Given Open the sign_in page
    When Log in to the page with valid credentials: 'samirznifeche@gmail.com', 'HabibiOlya@76'
    And Click on "Secondary" option at the left side menu
    Then Verify the Secondary page opens
    When Click on Filters
    And Filer the products by "want to sell"
    And Click on Apply Filter
    Then Verify all cards have "for sale" tag