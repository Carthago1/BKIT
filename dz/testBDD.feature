Feature: testing my bot

    Scenario: Test1
        Given I have the conditions пасмурно
        When I find picture_path
        Then I expect the result to be D:\BKIT\dz\pictures\пасмурно.png
    
        Scenario: Test2
        Given I have the conditions переменная облачность
        When I find picture_path
        Then I expect the result to be D:\BKIT\dz\pictures\переменная облачность.png