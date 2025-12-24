#!/bin/bash
cat environment/input.txt | tr ' ' '\n' | sort | uniq -c > environment/output.txt

