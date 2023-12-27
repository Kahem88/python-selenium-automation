# Created by kahempatrick at 12/19/23
Feature: click on the connect the company button and register a new company
  # Enter feature description here

  Scenario: User clicks on “Connect the company” button and can use the form to register a new agency

     Given Open the reelly main page
     When Log in to the reelly page
     When click on connect the company
     When switch the new tab
     # Then scroll down to bottom
     When enter some test information in the form
     Then verify the right information is present
     Then verify "send request" button is available and clickable
     Then Verify “buy a subscription” button is available and clickable



    # Enter steps here





