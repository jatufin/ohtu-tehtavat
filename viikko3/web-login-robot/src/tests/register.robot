*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  ville
    Set Password  ville123
    Set Password Confirmation  ville123
    Submit Registration
    Welcome Page Should Be Open 

Register With Too Short Username And Valid Password
    Set Username  kal
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Registration
    Registration Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  martta
    Set Password  123456A
    Set Password Confirmation  123456A
    Submit Registration
    Registration Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Set Username  martta
    Set Password  1234567A
    Set Password Confirmation  1234567B
    Submit Registration
    Registration Should Fail With Message  Passwords don't match

*** Keywords ***
Set Password Confirmation
    [Arguments]  ${password}
    Input Text  password_confirmation  ${password}

Submit Registration
    Click Button  Register

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
    
