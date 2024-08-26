#!/bin/bash

python train_icrl.py ../config/highD_velocity_constraint/train_VICRL_highD_velocity_constraint.yaml -n 5 -s 123
python train_icrl.py ../config/highD_velocity_constraint/train_VICRL_highD_velocity_constraint.yaml -n 5 -s 456
python train_icrl.py ../config/highD_velocity_constraint/train_VICRL_highD_velocity_constraint.yaml -n 5 -s 654
python train_icrl.py ../config/highD_velocity_constraint/train_VICRL_highD_velocity_constraint.yaml -n 5 -s 666
