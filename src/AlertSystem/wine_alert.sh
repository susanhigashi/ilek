#!/bin/bash

cd $ROOT_DIR/src/daemon

# Activate your Python virtual environment
source $ROOT_DIR/virtualenv/bin/activate

# Run the WineAlertSystem script
python wine_alert_system.py

# Deactivate the virtual environment
deactivate
