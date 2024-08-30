def get_plot_results_dir(env_id):
    if env_id == 'highD_velocity_constraint':
        log_path_dict = {
            "PPO_lag_highD_velocity_constraint": [
                '../save_model/PPO-Lag-highD-velocity/train_ppo_lag_highD_velocity_constraint-multi_env-Aug-26-2024-12:19-seed_123/',
                '../save_model/PPO-Lag-highD-velocity/train_ppo_lag_highD_velocity_constraint-multi_env-Aug-27-2024-03:26-seed_321/',
                '../save_model/PPO-Lag-highD-velocity/train_ppo_lag_highD_velocity_constraint-multi_env-Aug-27-2024-19:00-seed_456/',
                '../save_model/PPO-Lag-highD-velocity/train_ppo_lag_highD_velocity_constraint-multi_env-Aug-28-2024-10:35-seed_654/',
                '../save_model/PPO-Lag-highD-velocity/train_ppo_lag_highD_velocity_constraint-multi_env-Aug-28-2024-23:19-seed_666/',
            ],
            "GAIL_highD_velocity_constraint": [
                '../save_model/GAIL-highD-velocity/train_GAIL_highd_velocity_constraint-multi_env-Aug-23-2024-15:25-seed_123/',
                '../save_model/GAIL-highD-velocity/train_GAIL_highd_velocity_constraint-multi_env-Aug-25-2024-00:06-seed_321/',
                '../save_model/GAIL-highD-velocity/train_GAIL_highd_velocity_constraint-multi_env-Aug-25-2024-02:54-seed_456/',
                '../save_model/GAIL-highD-velocity/train_GAIL_highd_velocity_constraint-multi_env-Aug-25-2024-05:47-seed_654/',
                '../save_model/GAIL-highD-velocity/train_GAIL_highd_velocity_constraint-multi_env-Aug-25-2024-08:28-seed_666/',
            ],
            "ICRL_highD_velocity_constraint": [
                '../save_model/ICRL-highD-velocity/train_ICRL_highD_velocity_constraint-multi_env-Aug-23-2024-21:16-seed_123/',
                '../save_model/ICRL-highD-velocity/train_ICRL_highD_velocity_constraint-multi_env-Aug-25-2024-00:07-seed_321/',
                '../save_model/ICRL-highD-velocity/train_ICRL_highD_velocity_constraint-multi_env-Aug-25-2024-04:54-seed_456/',
                '../save_model/ICRL-highD-velocity/train_ICRL_highD_velocity_constraint-multi_env-Aug-25-2024-10:23-seed_654/',
                '../save_model/ICRL-highD-velocity/train_ICRL_highD_velocity_constraint-multi_env-Aug-25-2024-15:14-seed_666/',
            ],
            "Binary_highD_velocity_constraint": [
                '../save_model/Binary-highD-velocity/train_Binary_highD_velocity_constraint-multi_env-Aug-23-2024-21:15-seed_123/',
                '../save_model/Binary-highD-velocity/train_Binary_highD_velocity_constraint-multi_env-Aug-26-2024-12:07-seed_321/',
                '../save_model/Binary-highD-velocity/train_Binary_highD_velocity_constraint-multi_env-Aug-26-2024-16:51-seed_456/',
                '../save_model/Binary-highD-velocity/train_Binary_highD_velocity_constraint-multi_env-Aug-26-2024-21:33-seed_654/',
                '../save_model/Binary-highD-velocity/train_Binary_highD_velocity_constraint-multi_env-Aug-27-2024-03:00-seed_666/',
            ],
            "VICRL_highD_velocity_constraint": [
                # '../save_model/VICRL-highD-velocity/train_VICRL_highD_velocity_constraint-multi_env-Aug-24-2024-09:55-seed_123/',
                '../save_model/VICRL-highD-velocity/train_VICRL_highD_velocity_constraint-multi_env-Aug-26-2024-12:07-seed_123/',
                '../save_model/VICRL-highD-velocity/train_VICRL_highD_velocity_constraint-multi_env-Aug-26-2024-17:01-seed_456/',
                '../save_model/VICRL-highD-velocity/train_VICRL_highD_velocity_constraint-multi_env-Aug-26-2024-22:00-seed_654/',
                '../save_model/VICRL-highD-velocity/train_VICRL_highD_velocity_constraint-multi_env-Aug-27-2024-03:43-seed_666/',
                '../save_model/VICRL-highD-velocity/train_VICRL_highD_velocity_constraint-multi_env-Aug-27-2024-13:33-seed_321/',
            ],
        }
    elif env_id == 'highD_distance_constraint':
        log_path_dict = {
            "ppo_highD_no_slo_distance_dm-5": [
                '../save_model/PPO-highD-distance/train_ppo_highD_no_slo_distance_penalty_bs--1_fs-5k_nee-10_lr-5e-4_dm-5-multi_env-May-24-2022-00:31-seed_123/',
                # '../save_model/PPO-highD-distance/train_ppo_highD_no_slo_distance_penalty_bs--1_fs-5k_nee-10_lr-5e-4_dm-5-multi_env-May-23-2022-04:26-seed_123/',
            ],
            "ppo_lag_highD_no_slo_distance_dm-5": [
                '../save_model/PPO-Lag-highD-distance/train_ppo_lag_highD_no_slo_distance_penalty_bs--1_fs-5k_nee-10_lr-5e-4_dm-5-multi_env-May-24-2022-00:53-seed_123/',
                '../save_model/PPO-Lag-highD-distance/train_ppo_lag_highD_no_slo_distance_penalty_bs--1_fs-5k_nee-10_lr-5e-4_dm-5-multi_env-May-26-2022-00:49-seed_321/',
                '../save_model/PPO-Lag-highD-distance/train_ppo_lag_highD_no_slo_distance_penalty_bs--1_fs-5k_nee-10_lr-5e-4_dm-5-multi_env-May-26-2022-00:49-seed_666/',
            ],
            "ICRL_highD_slo_distance_constraint_no_is_bs--1-1e3_fs-5k_nee-10_lr-5e-4_no-buffer_dm-5": [
                '../save_model/ICRL-highD-distance/train_ICRL_highD_slo_distance_constraint_no_is_bs--1-1e3_fs-5k_nee-10_lr-5e-4_no-buffer_dm-5-multi_env-May-25-2022-10:17-seed_123/',
            ],
            "VICRL_highD_slo_distance_constraint_p-9e-1-1e-1_bs--1-1e3_fs-5k_nee-10_lr-5e-4_cl-64-64_no-buffer_dm-20": [
                '../save_model/VICRL-highD-distance/train_VICRL_highD_slo_distance_constraint_p-9e-1-1e-1_bs--1-1e3_fs-5k_nee-10_lr-5e-4_cl-64-64_no-buffer_dm-20-multi_env-May-28-2022-10:19-seed_123/',
            ],
            'Binary_highD_slo_distance_constraint_no_is_bs--1-1e3_nee-10_lr-1e-4_mspe-5e1_no-buffer_dm-20_data-1e-1':[
                '../save_model/Binary-highD-distance/train_Binary_highD_slo_distance_constraint_no_is_bs--1-1e3_nee-10_lr-1e-4_mspe-5e1_no-buffer_dm-20_data-1e-1-multi_env-Jan-16-2023-16:03-seed_123/',
                '../save_model/Binary-highD-distance/train_Binary_highD_slo_distance_constraint_no_is_bs--1-1e3_nee-10_lr-1e-4_mspe-5e1_no-buffer_dm-20_data-1e-1-multi_env-Jan-17-2023-02:20-seed_321/',
                '../save_model/Binary-highD-distance/train_Binary_highD_slo_distance_constraint_no_is_bs--1-1e3_nee-10_lr-1e-4_mspe-5e1_no-buffer_dm-20_data-1e-1-multi_env-Jan-17-2023-12:21-seed_666/',
            ],
            "GAIL_highD_slo_distance_constraint_no_is_bs--1--1_lr-5e-4_no-buffer_dm-20": [
                '../save_model/GAIL-highD-distance/train_GAIL_highD_slo_distance_constraint_no_is_bs--1--1_lr-5e-4_no-buffer_dm-20-multi_env-May-30-2022-02:11-seed_123/',
                '../save_model/GAIL-highD-distance/train_GAIL_highD_slo_distance_constraint_no_is_bs--1--1_lr-5e-4_no-buffer_dm-20-multi_env-May-31-2022-04:39-seed_321/',
                '../save_model/GAIL-highD-distance/train_GAIL_highD_slo_distance_constraint_no_is_bs--1--1_lr-5e-4_no-buffer_dm-20-multi_env-May-31-2022-04:40-seed_666/'
            ]
        }
    elif env_id == 'highD_velocity_distance_constraint':
        log_path_dict = {
            "ppo_highD_velocity_distance_penalty_bs--1_fs-5k_nee-10_lr-5e-4_vm-40_dm-20": [
                '../save_model/PPO-highD-velocity-distance/train_ppo_highD_velocity_distance_penalty_bs--1_fs-5k_nee-10_lr-5e-4_vm-40_dm-20-multi_env-Aug-23-2022-05:41-seed_123/',
                '../save_model/PPO-highD-velocity-distance/train_ppo_highD_velocity_distance_penalty_bs--1_fs-5k_nee-10_lr-5e-4_vm-40_dm-20-multi_env-Aug-23-2022-05:41-seed_321/',
                '../save_model/PPO-highD-velocity-distance/train_ppo_highD_velocity_distance_penalty_bs--1_fs-5k_nee-10_lr-5e-4_vm-40_dm-20-multi_env-Aug-23-2022-05:41-seed_666/',
            ],
            "ppo_lag_highD_velocity_distance_penalty_bs--1_fs-5k_nee-10_lr-5e-4_vm-40_dm-20": [
                '../save_model/PPO-Lag-highD-velocity-distance/train_ppo_lag_highD_velocity_distance_penalty_bs--1_fs-5k_nee-10_lr-5e-4_vm-40_dm-20-multi_env-Aug-14-2022-13:27-seed_123/',
                '../save_model/PPO-Lag-highD-velocity-distance/train_ppo_lag_highD_velocity_distance_penalty_bs--1_fs-5k_nee-10_lr-5e-4_vm-40_dm-20-multi_env-Aug-23-2022-05:41-seed_321/',
                '../save_model/PPO-Lag-highD-velocity-distance/train_ppo_lag_highD_velocity_distance_penalty_bs--1_fs-5k_nee-10_lr-5e-4_vm-40_dm-20-multi_env-Aug-15-2022-07:57-seed_666/',
            ],
            "GAIL_highD_velocity_distance_constraint": [
                '../save_model/GAIL-highD-velocity-distance/train_GAIL_velocity_distance_constraint-multi_env-Aug-27-2024-20:24-seed_123/',
                '../save_model/GAIL-highD-velocity-distance/train_GAIL_velocity_distance_constraint-multi_env-Aug-27-2024-23:52-seed_321/',
                '../save_model/GAIL-highD-velocity-distance/train_GAIL_velocity_distance_constraint-multi_env-Aug-28-2024-03:19-seed_456/',
                '../save_model/GAIL-highD-velocity-distance/train_GAIL_velocity_distance_constraint-multi_env-Aug-28-2024-06:52-seed_654/',
                '../save_model/GAIL-highD-velocity-distance/train_GAIL_velocity_distance_constraint-multi_env-Aug-28-2024-10:16-seed_666/',
            ],
            "Binary_highD_velocity_distance_constraint": [
                '../save_model/Binary-highD-velocity-distance/train_Binary_highD_velocity_distance_constraint-multi_env-Aug-28-2024-13:40-seed_123/',
                '../save_model/Binary-highD-velocity-distance/train_Binary_highD_velocity_distance_constraint-multi_env-Aug-29-2024-00:22-seed_321/',
                '../save_model/Binary-highD-velocity-distance/train_Binary_highD_velocity_distance_constraint-multi_env-Aug-29-2024-10:56-seed_456/',
                '../save_model/Binary-highD-velocity-distance/train_Binary_highD_velocity_distance_constraint-multi_env-Aug-29-2024-21:21-seed_654/',
                '../save_model/Binary-highD-velocity-distance/train_Binary_highD_velocity_distance_constraint-multi_env-Aug-30-2024-09:30-seed_666/',

            ],
            "ICRL_highD_velocity_distance_constraint": [
                '../save_model/ICRL-highD-velocity-distance/train_ICRL_highD_velocity_distance_constraint-multi_env-Aug-27-2024-20:26-seed_123/',
                '../save_model/ICRL-highD-velocity-distance/train_ICRL_highD_velocity_distance_constraint-multi_env-Aug-28-2024-07:23-seed_321/',
                '../save_model/ICRL-highD-velocity-distance/train_ICRL_highD_velocity_distance_constraint-multi_env-Aug-28-2024-18:27-seed_456/',
                '../save_model/ICRL-highD-velocity-distance/train_ICRL_highD_velocity_distance_constraint-multi_env-Aug-29-2024-04:50-seed_654/',
                '../save_model/ICRL-highD-velocity-distance/train_ICRL_highD_velocity_distance_constraint-multi_env-Aug-29-2024-16:16-seed_666/',
            ],
            "VICRL_highD_velocity_distance_constraint": [
               '../save_model/VICRL-highD-velocity-distance/train_VICRL_highD_velocity_distance_constraint-multi_env-Aug-30-2024-03:04-seed_123/',
            ],
        }
    elif env_id == 'WGW-v0':
        log_path_dict = {
            'PI-Lag-setting1': [
                '../save_model/PI-Lag-WallGrid/train_ppo_lag_WGW-v0_max-nu-1-setting1-Dec-29-2022-19:07-seed_123/',
            ],
            'PI-Lag-setting2': [
                '../save_model/PI-Lag-WallGrid/train_ppo_lag_WGW-v0_max-nu-1-setting2-Dec-21-2022-17:08-seed_123/',
            ],
            'PI-Lag-setting3': [
                '../save_model/PI-Lag-WallGrid/train_ppo_lag_WGW-v0_max-nu-1-setting3-Dec-23-2022-17:37-seed_123/',
            ],
            'PI-Lag-setting4': [
                '../save_model/PI-Lag-WallGrid/train_ppo_lag_WGW-v0_max-nu-1-setting4-Dec-26-2022-19:19-seed_123/',
            ],
            "ICRL_without-action_by_games_max-nu-1_with-buffer-setting1": [
                '../save_model/ICRL-WallGrid/train_ICRL_WGW-v0_without-action_by_games_max-nu-1_recon_obs_with-buffer-setting1-Dec-23-2022-17:22-seed_123/',
            ],
            "ICRL_without-action_by_games_max-nu-1_with-buffer-setting2": [
                '../save_model/ICRL-WallGrid/train_ICRL_WGW-v0_without-action_by_games_max-nu-1_recon_obs_with-buffer-setting2-Dec-23-2022-17:22-seed_123/',
            ],
            "ICRL_without-action_by_games_max-nu-1_with-buffer-setting3": [
                '../save_model/ICRL-WallGrid/train_ICRL_WGW-v0_without-action_by_games_max-nu-1_recon_obs_with-buffer-setting3-Dec-23-2022-17:49-seed_123/',
            ],
            "ICRL_without-action_by_games_max-nu-1_with-buffer-setting4": [
                '../save_model/ICRL-WallGrid/train_ICRL_WGW-v0_without-action_by_games_max-nu-1_recon_obs_with-buffer-setting1-Dec-23-2022-17:22-seed_123/',
            ],
            "VICRL_without-action_by_games_max-nu-1_with-buffer-setting1": [
                '../save_model/VICRL-WallGrid/train_VICRL_WGW-v0_without-action_by_games_max-nu-1_recon_obs_p-9e-2-1e-2_with-buffer-setting1_mean-Dec-29-2022-17:40-seed_123/',
            ],
            "VICRL_without-action_by_games_max-nu-1_with-buffer-setting2": [
                '../save_model/VICRL-WallGrid/train_VICRL_WGW-v0_without-action_by_games_max-nu-1_recon_obs_p-9e-2-1e-2_with-buffer-setting2_mean-Dec-29-2022-18:05-seed_123/',
            ],
            "VICRL_without-action_by_games_max-nu-1_with-buffer-setting3": [
                '../save_model/VICRL-WallGrid/train_VICRL_WGW-v0_without-action_by_games_max-nu-1_recon_obs_p-9e-2-1e-2_with-buffer-setting3_mean-Dec-29-2022-18:05-seed_123/',
            ],
            "VICRL_without-action_by_games_max-nu-1_with-buffer-setting4": [
                '../save_model/VICRL-WallGrid/train_VICRL_WGW-v0_without-action_by_games_max-nu-1_recon_obs_p-9e-2-1e-2_with-buffer-setting4_mean-Dec-29-2022-18:05-seed_123/',
            ],
            "Binary_without-action_by_games_max-nu-1_with-buffer-setting1": [
                '../save_model/Binary-WallGrid/train_Binary_WGW-v0_without-action_by_games_max-nu-1_recon_obs_with-buffer-setting1-Dec-23-2022-17:56-seed_123/',
            ],
            "Binary_without-action_by_games_max-nu-1_with-buffer-setting2": [
                '../save_model/Binary-WallGrid/train_Binary_WGW-v0_without-action_by_games_max-nu-1_recon_obs_with-buffer-setting2-Dec-23-2022-17:56-seed_123/',
            ],
            "Binary_without-action_by_games_max-nu-1_with-buffer-setting3": [
                '../save_model/Binary-WallGrid/train_Binary_WGW-v0_without-action_by_games_max-nu-1_recon_obs_with-buffer-setting3-Dec-23-2022-18:17-seed_123/',
            ],
            "Binary_without-action_by_games_max-nu-1_with-buffer-setting4": [
                '../save_model/Binary-WallGrid/train_Binary_WGW-v0_without-action_by_games_max-nu-1_recon_obs_with-buffer-setting4-Dec-26-2022-21:14-seed_123/',
            ],
            "GAIL_without-action_by_games_with-buffer-setting1": [
                '../save_model/GAIL-WallGrid/train_GAIL_WGW-v0_without-action_by_games_with-buffer-setting1-Jan-20-2023-17:28-seed_123/',
                # '../save_model/GAIL-WallGrid/train_GAIL_WGW-v0_without-action_by_games_with-buffer-setting1-Jan-19-2023-17:22-seed_123/',
                # '../save_model/GAIL-WallGrid/train_GAIL_WGW-v0_without-action_by_games_with-buffer-setting1-Jan-19-2023-19:37-seed_123/',
            ],
            "GAIL_without-action_by_games_with-buffer-setting2": [
                '../save_model/GAIL-WallGrid/train_GAIL_WGW-v0_without-action_by_games_with-buffer-setting2-Jan-20-2023-17:28-seed_123/',
                # '../save_model/GAIL-WallGrid/train_GAIL_WGW-v0_without-action_by_games_with-buffer-setting2-Jan-19-2023-17:31-seed_123/',
                # '../save_model/GAIL-WallGrid/train_GAIL_WGW-v0_without-action_by_games_with-buffer-setting2-Jan-20-2023-10:34-seed_123/',
            ],
            "GAIL_without-action_by_games_with-buffer-setting3": [
                '../save_model/GAIL-WallGrid/train_GAIL_WGW-v0_without-action_by_games_with-buffer-setting3-Jan-20-2023-17:28-seed_123/',
                # '../save_model/GAIL-WallGrid/train_GAIL_WGW-v0_without-action_by_games_with-buffer-setting3-Jan-19-2023-17:44-seed_123/'
                # '../save_model/GAIL-WallGrid/train_GAIL_WGW-v0_without-action_by_games_with-buffer-setting3-Jan-20-2023-10:37-seed_123/',
            ],
            "GAIL_without-action_by_games_with-buffer-setting4": [
                '../save_model/GAIL-WallGrid/train_GAIL_WGW-v0_without-action_by_games_with-buffer-setting4-Jan-20-2023-17:20-seed_123/',
                # '../save_model/GAIL-WallGrid/train_GAIL_WGW-v0_without-action_by_games_with-buffer-setting4-Jan-19-2023-17:52-seed_123/',
                # '../save_model/GAIL-WallGrid/train_GAIL_WGW-v0_without-action_by_games_with-buffer-setting4-Jan-20-2023-10:41-seed_123/',
            ],
        }
    elif env_id == 'HCWithPos-v0':
        log_path_dict = {
            "PPO_lag_Pos": [
                '../save_model/PPO-Lag-HC/train_ppo_lag_HCWithPos-v0-multi_env-Apr-21-2022-04:49-seed_123/',
                '../save_model/PPO-Lag-HC/train_ppo_lag_HCWithPos-v0-multi_env-Apr-21-2022-06:27-seed_321/',
                '../save_model/PPO-Lag-HC/train_ppo_lag_HCWithPos-v0-multi_env-Apr-21-2022-08:05-seed_456/',
                '../save_model/PPO-Lag-HC/train_ppo_lag_HCWithPos-v0-multi_env-Apr-21-2022-09:42-seed_654/',
                '../save_model/PPO-Lag-HC/train_ppo_lag_HCWithPos-v0-multi_env-Apr-21-2022-11:18-seed_666/'
            ],
            "ICRL_Pos_with-action": [
                '../save_model/ICRL-HC/train_ICRL_HCWithPos-v0_with-action-multi_env-Apr-22-2022-08:54-seed_123/',
                '../save_model/ICRL-HC/train_ICRL_HCWithPos-v0_with-action-multi_env-Apr-22-2022-10:43-seed_321/',
                '../save_model/ICRL-HC/train_ICRL_HCWithPos-v0_with-action-multi_env-Apr-22-2022-12:29-seed_456/',
                '../save_model/ICRL-HC/train_ICRL_HCWithPos-v0_with-action-multi_env-Apr-22-2022-14:17-seed_654/',
                '../save_model/ICRL-HC/train_ICRL_HCWithPos-v0_with-action-multi_env-Apr-22-2022-16:04-seed_666/',
            ],
            "VICRL_Pos_with-buffer_with-action_p-9e-1-1e-1_clr-5e-3": [
                '../save_model/VICRL-HC/train_VICRL_HCWithPos-v0_with_action_with_buffer_p-9e-1-1e-1_clr-5e-3_no_is-multi_env-Apr-21-2022-05:00-seed_123/',
                '../save_model/VICRL-HC/train_VICRL_HCWithPos-v0_with_action_with_buffer_p-9e-1-1e-1_clr-5e-3_no_is-multi_env-Apr-21-2022-06:42-seed_321/',
                '../save_model/VICRL-HC/train_VICRL_HCWithPos-v0_with_action_with_buffer_p-9e-1-1e-1_clr-5e-3_no_is-multi_env-Apr-21-2022-08:25-seed_456/',
                '../save_model/VICRL-HC/train_VICRL_HCWithPos-v0_with_action_with_buffer_p-9e-1-1e-1_clr-5e-3_no_is-multi_env-Apr-21-2022-10:08-seed_654/',
                '../save_model/VICRL-HC/train_VICRL_HCWithPos-v0_with_action_with_buffer_p-9e-1-1e-1_clr-5e-3_no_is-multi_env-Apr-21-2022-11:52-seed_666/',
            ],
            "Binary_HCWithPos-v0_with-action": [
                '../save_model/Binary-HC/train_Binary_HCWithPos-v0_with-action-multi_env-Apr-21-2022-04:49-seed_123/',
                '../save_model/Binary-HC/train_Binary_HCWithPos-v0_with-action-multi_env-Apr-21-2022-06:27-seed_321/',
                '../save_model/Binary-HC/train_Binary_HCWithPos-v0_with-action-multi_env-Apr-21-2022-08:05-seed_456/',
                '../save_model/Binary-HC/train_Binary_HCWithPos-v0_with-action-multi_env-Apr-21-2022-09:43-seed_654/',
                '../save_model/Binary-HC/train_Binary_HCWithPos-v0_with-action-multi_env-Apr-21-2022-11:20-seed_666/',
            ],
            "GAIL_HCWithPos-v0_with-action": [
                '../save_model/GAIL-HC/train_GAIL_HCWithPos-v0_with-action-multi_env-Apr-21-2022-05:55-seed_123/',
                '../save_model/GAIL-HC/train_GAIL_HCWithPos-v0_with-action-multi_env-Apr-21-2022-07:32-seed_321/',
                '../save_model/GAIL-HC/train_GAIL_HCWithPos-v0_with-action-multi_env-Apr-21-2022-09:18-seed_456/',
                '../save_model/GAIL-HC/train_GAIL_HCWithPos-v0_with-action-multi_env-Apr-21-2022-11:02-seed_654/',
                '../save_model/GAIL-HC/train_GAIL_HCWithPos-v0_with-action-multi_env-Apr-21-2022-12:45-seed_666/'
            ],
        }
    else:
        raise ValueError("Unknown env id {0}".format(env_id))
    return log_path_dict
