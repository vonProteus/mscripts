#!/bin/bash

echo "" >> ~/.bash_profile
echo "# mScripts added $(date)" >> ~/.bash_profile
echo "export PATH=\$PATH:$(pwd)/scripts" >> ~/.bash_profile
export PATH=$PATH:$(pwd)/scripts

chmod +x $(pwd)/scripts/*