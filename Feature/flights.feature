Feature: Flight searching
  Scenario:Booking low price ticket
    Given click on Flights option
    When Enter origin as "HYD" select "HYD" from list
    And Enter destination as "TIR" Select "TIR" from list
    And Select departure month as "OCTOBER" and date as "26"
    And click on search
    Then modify button appears



