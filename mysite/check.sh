#!/bin/bash

echo "PYLINT"
pylint mysite/polls

echo -e "\n\n\nPEP8\n"

pep8 . && echo "pep8 correct"                                                                                                 
