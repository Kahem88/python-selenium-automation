# Created by kahempatrick at 9/25/23
Feature: Test for amazon cart

  Scenario: Verify that the product is in the cart
    Scenario: user can add a product to the cart
    Given Open Amazon page
    When Search for table
    When Click on the second product
    When Store product name Small Computer Desk Small Office Desk 32 Inch Writing Desk
    When Click on add to cart button
    When Open cart page
    Then Verify cart has 1 items(s)
    Then Verify cart has correct product