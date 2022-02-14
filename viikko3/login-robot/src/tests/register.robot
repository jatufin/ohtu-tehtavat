*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  juuso  kalle123
    Output Should Contain  Username already exists
    
Register With Too Short Username And Valid Password
    Input Credentials  kal  kalle123
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  kalle  123456a
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  abcdefghIJK
    Output Should Contain  Password can not contain only letters

*** Keywords ***
Create User And Input New Command
    Create User  juuso  password0
    Input New Command
    