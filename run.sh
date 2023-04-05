#!/bin/bash
echo "Removing old ENV"
rm -rf oslili

echo "Creating ENV"
python3 -m venv oslili
activate="oslili/bin/activate"
if [ ! -f "$activate" ]
then
    echo "ERROR: activate not found at $activate"
    return 1
fi
. "$activate"
if [ ! -d "logs" ]; then
  mkdir logs
fi

echo "Install Python requirements"
#pip3 install --upgrade pip
pip3 install scikit-learn

echo "Running test script"
python3 cli.py sample.txt

deactivate
