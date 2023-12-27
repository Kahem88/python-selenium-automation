# Created by kahempatrick at 10/27/23
Feature: test to open subscription and payments page
  # Enter feature description here

  Scenario: User can open Subscription & payments page

  Given Open the main page
  When Log in to the page
  When Click on settings option.
  When Click on Subscription & payments option.
  When Verify the right page opens.
  Then Verify title “Subscription & payments” is visible.
#  Then Verify “back” and “upgrade plan” buttons are available.
    # Enter steps here