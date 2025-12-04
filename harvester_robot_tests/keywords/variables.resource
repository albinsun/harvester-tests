*** Settings ***
Documentation    Global Variables for Harvester Robot Tests
Library          Collections
Library          String  
Library          DateTime

*** Variables ***
# Harvester Cluster
${HARVESTER_ENDPOINT}           %{HARVESTER_ENDPOINT=https://10.115.252.130}
${HARVESTER_USERNAME}           %{HARVESTER_USERNAME=admin}
${HARVESTER_PASSWORD}           %{HARVESTER_PASSWORD=password1234}

# Testing
${OPERATION_STRATEGY}           %{HARVESTER_OPERATION_STRATEGY=crd}

# Timeouts and Intervals
${WAIT_TIMEOUT}                 ${600}
${RETRY_INTERVAL}               ${3}
${SLEEP_TIMEOUT}                ${3}

# Images
${OPENSUSE_IMAGE_URL}           http://192.168.123.1:8080/openSUSE-Leap-15.6.x86_64-NoCloud.qcow2
${UBUNTU_IMAGE_URL}             http://192.168.123.1:8080/ubuntu-24.04-server-cloudimg-amd64.img

# Network
${VLAN_ID}                      %{VLAN_ID=1}
${VLAN_NIC}                     %{VLAN_NIC=mgmt}

# VM Defaults
${DEFAULT_VM_CPU}               2
${DEFAULT_VM_MEMORY}            4Gi
${DEFAULT_VM_REPLICAS}          3

# Storage
${DEFAULT_STORAGE_CLASS}        longhorn
${DEFAULT_VOLUME_SIZE}          10Gi

# Test Execution
${LOOP_COUNT}                   3
${RETRY_COUNT}                  100

# Namespaces and Labels
${DEFAULT_NAMESPACE}            default
${LABEL_TEST}                   test-harvester
