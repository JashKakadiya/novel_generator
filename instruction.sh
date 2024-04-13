#!/bin/bash

# Function to install requirements for GPU
install_gpu_requirements() {
    echo "Installing requirements for GPU..."
    CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python==0.1.78 --force-reinstall --upgrade --no-cache-dir --verbose
}

# Function to install requirements for CPU
install_cpu_requirements() {
    echo "Installing requirements for CPU..."
    pip install llama-cpp-python==0.1.78
}

# Make virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate the environment
echo "Activating virtual environment..."
source venv/bin/activate

# Prompt user for GPU or CPU installation
echo "Do you want to install for GPU or CPU?"
select installation_type in GPU CPU
do
    case $installation_type in
        GPU)
            install_gpu_requirements
            break
            ;;
        CPU)
            install_cpu_requirements
            break
            ;;
        *)
            echo "Invalid option. Please choose GPU or CPU."
            ;;
    esac
done

# Other dependencies
echo "Installing other dependencies..."
pip install langchain langchain-community pypdf python-dotenv python-docx PyDocX PyMuPDF torch

# Run the app
echo "ready to run app..."

