docker ps
docker compose build
docker compose run rl
docker compose run rl bash /workspace/start_jupyter.sh

python3 -c "import mujoco; print('MuJoCo OK:', mujoco.__version__)"
python3 -c "import torch; print('GPU available:', torch.cuda.is_available())"
python3 -c "import gymnasium as gym; import myosuite; env = gym.make('myoHandPoseFixed-v0'); print('MyoSuite OK')"
exit    