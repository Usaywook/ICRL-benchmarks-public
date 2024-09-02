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

    #################################################
    # Blocked Half-cheetah
    #################################################

    # run PPO-Lag
    CUDA_VISIBLE_DEVICES=$DEVICE python train_policy.py ../config/mujuco_BlockedHalfCheetah/train_ppo_lag_HCWithPos-v0.yaml -n 5 -s $SEED

    # run GACL
    CUDA_VISIBLE_DEVICES=$DEVICE python train_gail.py ../config/mujuco_BlockedHalfCheetah/train_GAIL_HCWithPos-v0.yaml -n 5 -s $SEED

    # run BC2L
    CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/mujuco_BlockedHalfCheetah/train_Binary_HCWithPos-v0.yaml -n 5 -s $SEED

    # run MECL
    CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/mujuco_BlockedHalfCheetah/train_ICRL_HCWithPos-v0.yaml -n 5 -s $SEED

    # run VICRL
    CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/mujuco_BlockedHalfCheetah/train_VICRL_HCWithPos-v0.yaml -n 5 -s $SEED

    #################################################
    # Blocked AntWall
    #################################################

    # run PPO-Lag
    CUDA_VISIBLE_DEVICES=$DEVICE python train_policy.py ../config/mujoco_BlockedAntWall/train_ppo_lag_AntWall-v0.yaml -n 5 -s $SEED

    # run GACL
    CUDA_VISIBLE_DEVICES=$DEVICE python train_gail.py ../config/mujoco_BlockedAntWall/train_GAIL_AntWall-v0.yaml -n 5 -s $SEED

    # run BC2L
    CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/mujoco_BlockedAntWall/train_Binary_AntWall-v0.yaml -n 5 -s $SEED

    # run MECL
    CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/mujoco_BlockedAntWall/train_ICRL_AntWall-v0.yaml -n 5 -s $SEED

    # run VICRL
    CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/mujoco_BlockedAntWall/train_VICRL_AntWall-v0.yaml -n 5 -s $SEED

    #################################################
    # Biased Pendulum
    #################################################

    # run PPO-Lag
    CUDA_VISIBLE_DEVICES=$DEVICE python train_policy.py ../config/mujoco_BiasedPendulum/train_ppo_lag_InvertedPendulumWall-v0.yaml -n 5 -s $SEED

    # run GACL
    CUDA_VISIBLE_DEVICES=$DEVICE python train_gail.py ../config/mujoco_BiasedPendulum/train_GAIL_InvertedPendulumWall-v0.yaml -n 5 -s $SEED

    # run BC2L
    CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/mujoco_BiasedPendulum/train_Binary_InvertedPendulumWall-v0.yaml -n 5 -s $SEED

    # run MECL
    CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/mujoco_BiasedPendulum/train_ICRL_InvertedPendulumWall-v0.yaml -n 5 -s $SEED

    # run VICRL
    CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/mujoco_BiasedPendulum/train_VICRL_InvertedPendulumWall-v0.yaml -n 5 -s $SEED

    #################################################
    # Blocked Swimmer
    #################################################

    # run PPO-Lag
    CUDA_VISIBLE_DEVICES=$DEVICE python train_policy.py ../config/mujoco_BlockedSwimmer/train_ppo_lag_SwmWithPos-v0.yaml -n 5 -s $SEED

    # run GACL
    CUDA_VISIBLE_DEVICES=$DEVICE python train_gail.py ../config/mujoco_BlockedSwimmer/train_GAIL_SwmWithPos-v0.yaml -n 5 -s $SEED

    # run BC2L
    CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/mujoco_BlockedSwimmer/train_Binary_SwmWithPos-v0.yaml -n 5 -s $SEED

    # run MECL
    CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/mujoco_BlockedSwimmer/train_ICRL_SwmWithPos-v0.yaml -n 5 -s $SEED

    # run VICRL
    CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/mujoco_BlockedSwimmer/train_VICRL_SwmWithPos-v0.yaml -n 5 -s $SEED

    #################################################
    # Blocked Walker
    #################################################

    # run PPO-Lag
    CUDA_VISIBLE_DEVICES=$DEVICE python train_policy.py ../config/mujoco_BlockedWalker/train_ppo_lag_WalkerWithPos-v0.yaml -n 5 -s $SEED

    # run GACL
    CUDA_VISIBLE_DEVICES=$DEVICE python train_gail.py ../config/mujoco_BlockedWalker/train_GAIL_WalkerWithPos-v0.yaml -n 5 -s $SEED

    # run BC2L
    CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/mujoco_BlockedWalker/train_Binary_WalkerWithPos-v0.yaml -n 5 -s $SEED

    # run MECL
    CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/mujoco_BlockedWalker/train_ICRL_WalkerWithPos-v0.yaml -n 5 -s $SEED

    # run VICRL
    CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/mujoco_BlockedWalker/train_VICRL_WalkerWithPos-v0.yaml -n 5 -s $SEED

done

#################################################
# Discrete World
#################################################

# run PPO-Lag knowing the ground-truth
CUDA_VISIBLE_DEVICES=$DEVICE python train_policy.py ../config/mujoco_WGW-v0/train_ppo_lag_WGW-v0-setting1.yaml -n 5 -s 123
CUDA_VISIBLE_DEVICES=$DEVICE python train_policy.py ../config/mujoco_WGW-v0/train_ppo_lag_WGW-v0-setting2.yaml -n 5 -s 123
CUDA_VISIBLE_DEVICES=$DEVICE python train_policy.py ../config/mujoco_WGW-v0/train_ppo_lag_WGW-v0-setting3.yaml -n 5 -s 123
CUDA_VISIBLE_DEVICES=$DEVICE python train_policy.py ../config/mujoco_WGW-v0/train_ppo_lag_WGW-v0-setting4.yaml -n 5 -s 123

# run GACL
CUDA_VISIBLE_DEVICES=$DEVICE python train_gail.py ../config/mujoco_WGW-v0/train_GAIL_WGW-v0-setting1.yaml -n 5
CUDA_VISIBLE_DEVICES=$DEVICE python train_gail.py ../config/mujoco_WGW-v0/train_GAIL_WGW-v0-setting2.yaml -n 5
CUDA_VISIBLE_DEVICES=$DEVICE python train_gail.py ../config/mujoco_WGW-v0/train_GAIL_WGW-v0-setting3.yaml -n 5
CUDA_VISIBLE_DEVICES=$DEVICE python train_gail.py ../config/mujoco_WGW-v0/train_GAIL_WGW-v0-setting4.yaml -n 5

# run BC2L
CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/mujoco_WGW-v0/train_Binary_WGW-v0-setting1.yaml -n 5
CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/mujoco_WGW-v0/train_Binary_WGW-v0-setting2.yaml -n 5
CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/mujoco_WGW-v0/train_Binary_WGW-v0-setting3.yaml -n 5
CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/mujoco_WGW-v0/train_Binary_WGW-v0-setting4.yaml -n 5

# run MECL
CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/mujoco_WGW-v0/train_ICRL_WGW-v0-setting1.yaml -n 5
CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/mujoco_WGW-v0/train_ICRL_WGW-v0-setting2.yaml -n 5
CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/mujoco_WGW-v0/train_ICRL_WGW-v0-setting3.yaml -n 5
CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/mujoco_WGW-v0/train_ICRL_WGW-v0-setting4.yaml -n 5

# run VICRL
CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/mujoco_WGW-v0/train_VICRL_WGW-v0-setting1.yaml -n 5
CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/mujoco_WGW-v0/train_VICRL_WGW-v0-setting2.yaml -n 5
CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/mujoco_WGW-v0/train_VICRL_WGW-v0-setting3.yaml -n 5
CUDA_VISIBLE_DEVICES=$DEVICE python train_icrl.py ../config/mujoco_WGW-v0/train_VICRL_WGW-v0-setting4.yaml -n 5