*** Settings ***
Documentation    Common Keywords
Resource         variables.resource
Library          ../libs/keywords/common_keywords.py

*** Keywords ***
Set up test environment
    [Documentation]    Initialize test environment
    Log    Setting up test environment
    IF    "${OPERATION_STRATEGY}" == "crd"
        init k8s api client
    ELSE IF    "${OPERATION_STRATEGY}" == "rest"
        init harvester api client    ${HARVESTER_ENDPOINT}    ${HARVESTER_USERNAME}    ${HARVESTER_PASSWORD}
    ELSE IF    "${OPERATION_STRATEGY}" == "gui"
        init harvester gui client    ${HARVESTER_ENDPOINT}    ${HARVESTER_USERNAME}    ${HARVESTER_PASSWORD}
        # Convert timeouts from seconds to milliseconds in Playwright 
        Set Global Variable    ${WAIT_TIMEOUT}    ${WAIT_TIMEOUT * 1000}
        Set Global Variable    ${SLEEP_TIMEOUT}    ${SLEEP_TIMEOUT * 1000}
    ELSE
        Fatal Error    Unexpected HARVESTER_OPERATION_STRATEGY: 
    END
    Set Suite Metadata    OPERATION_STRATEGY    ${OPERATION_STRATEGY}

Cleanup test resources
    [Documentation]    Clean up all resources created during tests
    Log    Cleaning up test resources
    Run Keyword And Ignore Error    common_keywords.Cleanup VMs
    Run Keyword And Ignore Error    common_keywords.Cleanup images
    Run Keyword And Ignore Error    common_keywords.Cleanup volumes
    Run Keyword And Ignore Error    common_keywords.Cleanup networks
    Run Keyword And Ignore Error    common_keywords.Cleanup backups
