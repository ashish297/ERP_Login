#!/bin/bash

# Set the name of the virtual environment directory
VENV_DIR="myenv"

# Check if the virtual environment directory already exists
if [ -d "$VENV_DIR" ]; then
    echo "Virtual environment '$VENV_DIR' already exists."
else
    # Create the virtual environment
    python -m venv "$VENV_DIR"
    echo "Virtual environment '$VENV_DIR' created."
fi

# Activate the virtual environment
source "$VENV_DIR/Scripts/activate"

# Check if activation was successful
if [ $? -eq 0 ]; then
    echo "Virtual environment '$VENV_DIR' activated."

    # Install dependencies from requirements.txt if it exists
    if [ -f "requirements.txt" ]; then
        echo "Installing dependencies from requirements.txt..."
        pip install -r requirements.txt
    else
        echo "requirements.txt not found."
    fi
else
    echo "Failed to activate virtual environment '$VENV_DIR'."
fi
