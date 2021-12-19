Feature: My feature file using behave and
    testing my equation

    Scenario: Test my biquadratic equation1
        Given I have the coefficients 1, -5 and 4
        When I calculate them
        Then I expect the result to be -2, -1, 1, 2
        
    Scenario: Test my biquadratic equation2
        Given I have the coefficients 1, -5 and -36
        When I calculate them
        Then I expect the result to be -3, 3

    Scenario: Test my biquadratic equation3
        Given I have the coefficients 10, 25 and 0
        When I calculate them
        Then I expect the result to be 0