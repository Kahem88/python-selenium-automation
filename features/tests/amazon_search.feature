Feature: Tests for amazon search

  Scenario: Verify that a user can search for a table
    Given Open Amazon page
    When Search for table
    Then Verify search result is correct

  Scenario: Verify that clicking Orders takes to signin
    Given Open Amazon page
    When Click Orders
    Then Verify sign in page opened

  #Scenario: user can add a product to the cart
    #Given Open Amazon page
    #When Search for table
    #When Click on the first product
    #When Store product name
    #When Click on add to cart button
    #When Open cart page
    #Then Verify cart has 1 items(s)
    #Then Verify cart has correct product