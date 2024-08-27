#!/bin/bash

# gail
python train_gail.py ../../config/highD_velocity_constraint/train_GAIL_highd_velocity_constraint.yaml -n 5 -s 123
python train_gail.py ../../config/highD_velocity_constraint/train_GAIL_highd_velocity_constraint.yaml -n 5 -s 321
python train_gail.py ../../config/highD_velocity_constraint/train_GAIL_highd_velocity_constraint.yaml -n 5 -s 456
python train_gail.py ../../config/highD_velocity_constraint/train_GAIL_highd_velocity_constraint.yaml -n 5 -s 654
python train_gail.py ../../config/highD_velocity_constraint/train_GAIL_highd_velocity_constraint.yaml -n 5 -s 666

# bc2l
python train_icrl.py ../../config/highD_velocity_constraint/train_Binary_highD_velocity_constraint.yaml -n 5 -s 123
python train_icrl.py ../../config/highD_velocity_constraint/train_Binary_highD_velocity_constraint.yaml -n 5 -s 321
python train_icrl.py ../../config/highD_velocity_constraint/train_Binary_highD_velocity_constraint.yaml -n 5 -s 456
python train_icrl.py ../../config/highD_velocity_constraint/train_Binary_highD_velocity_constraint.yaml -n 5 -s 654
python train_icrl.py ../../config/highD_velocity_constraint/train_Binary_highD_velocity_constraint.yaml -n 5 -s 666

# mecl
python train_icrl.py ../../config/highD_velocity_constraint/train_ICRL_highD_velocity_constraint.yaml -n 5 -s 123
python train_icrl.py ../../config/highD_velocity_constraint/train_ICRL_highD_velocity_constraint.yaml -n 5 -s 321
python train_icrl.py ../../config/highD_velocity_constraint/train_ICRL_highD_velocity_constraint.yaml -n 5 -s 456
python train_icrl.py ../../config/highD_velocity_constraint/train_ICRL_highD_velocity_constraint.yaml -n 5 -s 654
python train_icrl.py ../../config/highD_velocity_constraint/train_ICRL_highD_velocity_constraint.yaml -n 5 -s 666

# vicrl
python train_icrl.py ../../config/highD_velocity_constraint/train_VICRL_highD_velocity_constraint.yaml -n 5 -s 123
python train_icrl.py ../../config/highD_velocity_constraint/train_VICRL_highD_velocity_constraint.yaml -n 5 -s 321
python train_icrl.py ../../config/highD_velocity_constraint/train_VICRL_highD_velocity_constraint.yaml -n 5 -s 456
python train_icrl.py ../../config/highD_velocity_constraint/train_VICRL_highD_velocity_constraint.yaml -n 5 -s 654
python train_icrl.py ../../config/highD_velocity_constraint/train_VICRL_highD_velocity_constraint.yaml -n 5 -s 666

