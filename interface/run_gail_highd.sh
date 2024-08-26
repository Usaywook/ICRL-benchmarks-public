#!/bin/bash

python train_gail.py ../config/highD_velocity_constraint/train_GAIL_highd_velocity_constraint.yaml -n 5 -s 321
python train_gail.py ../config/highD_velocity_constraint/train_GAIL_highd_velocity_constraint.yaml -n 5 -s 456
python train_gail.py ../config/highD_velocity_constraint/train_GAIL_highd_velocity_constraint.yaml -n 5 -s 654
python train_gail.py ../config/highD_velocity_constraint/train_GAIL_highd_velocity_constraint.yaml -n 5 -s 666
