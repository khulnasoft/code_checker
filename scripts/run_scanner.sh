#!/bin/bash

# Run the security scanner

# Set the directory to scan
DIRECTORY_TO_SCAN=${1:-.}

# Run SAST scanner
echo "Running SAST scanner..."
python3 -m code_checker.src.scanner.sast $DIRECTORY_TO_SCAN

# Run dependency scanner
echo "Running dependency scanner..."
python3 -m code_checker.src.scanner.dep_scan $DIRECTORY_TO_SCAN

# Run custom rule engine
echo "Running custom rule engine..."
python3 -m code_checker.src.scanner.rule_engine $DIRECTORY_TO_SCAN

echo "Scanning completed."
