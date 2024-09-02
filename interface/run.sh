#!/bin/bash

DEVICE=0
SEEDS=(123 321 456 654 666)

for SEED in ${SEEDS[@]}
do
    #################################################
    # highD_velocity_constraint
    #################################################

    # run PPO-Lag
    CUDA_VISIBLE_DEVICES=$DEVICE python train_policy.py ../config/highD_velocity_constraint/train_ppo_lag_highD_velocity_constraint.yaml -n 5 -s $SEED

    # run GACL
    CUDA_VISIBLE_DEVICES=$DEVICE python train_gail.py ../config/highD_velocity_constraint/train_GAIL_highd_velocity_constraint.yaml -n 5 -s $SEED

    # run BC2L
    CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/highD_velocity_constraint/train_Binary_highD_velocity_constraint.yaml -n 5 -s $SEED

    # run MECL
    CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/highD_velocity_constraint/train_ICRL_highD_velocity_constraint.yaml -n 5 -s $SEED

    # run VICRL
    CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/highD_velocity_constraint/train_VICRL_highD_velocity_constraint.yaml -n 5 -s $SEED


    #################################################
    # highD_distance_constraint
    #################################################

    # run PPO-Lag
    CUDA_VISIBLE_DEVICES=$DEVICE python train_policy.py ../config/highD_distance_constraint/train_ppo_lag_highD_distance_constraint.yaml -n 5 -s $SEED

    # run GACL
    CUDA_VISIBLE_DEVICES=$DEVICE python train_gail.py ../config/highD_distance_constraint/train_GAIL_highD_distance_constraint.yaml -n 5 -s $SEED

    # run BC2L
    CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/highD_distance_constraint/train_Binary_highD_distance_constraint.yaml -n 5 -s $SEED

    # run MECL
    CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/highD_distance_constraint/train_ICRL_highD_distance_constraint.yaml -n 5 -s $SEED

    # run VICRL
    CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/highD_distance_constraint/train_VICRL_highD_distance_constraint.yaml -n 5 -s $SEED

    #################################################
    # highD_velocity_distance_constraint
    #################################################

    # run PPO-Lag
    CUDA_VISIBLE_DEVICES=$DEVICE python train_policy.py ../config/highD_velocity_distance_constraint/train_ppo_lag_highD_velocity_distance_constraint.yaml -n 5 -s $SEED

    # run GACL
    CUDA_VISIBLE_DEVICES=$DEVICE python train_gail.py ../config/highD_velocity_distance_constraint/train_GAIL_velocity_distance_constraint.yaml -n 5 -s $SEED

    # run BC2L
    CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/highD_velocity_distance_constraint/train_Binary_highD_velocity_distance_constraint.yaml -n 5 -s $SEED

    # run MECL
    CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/highD_velocity_distance_constraint/train_ICRL_highD_velocity_distance_constraint.yaml -n 5 -s $SEED

    # run VICRL
    CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/highD_velocity_distance_constraint/train_VICRL_highD_velocity_distance_constraint.yaml -n 5 -s $SEED

done