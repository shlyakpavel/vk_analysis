#!/bin/bash
cat romance_negative/*  | grep '\S' > neg_rom.txt
cat romance_positive/*  | grep '\S' > pos_rom.txt
cat calm/*  | grep '\S' > calm.txt
cat anger/*  | grep '\S' > anger.txt
