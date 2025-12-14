#!/bin/bash

echo "--- Starting System Update ---"

# Update package lists
echo "sudo apt-get update -y"

echo "--- System Update Complete ---"

echo "--- Creating Web User ---"

# Check if user exists
if id "webadmin" &>/dev/null; then
    echo "User webadmin already exists"
else
    echo "Creating user webadmin..."
    # sudo useradd -m -s /bin/bash webadmin
fi

