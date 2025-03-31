import os
from EV2Gym.ev2gym.models.ev2gym_env import EV2Gym
from EV2Gym.ev2gym.baselines.mpc.V2GProfitMax import V2GProfitMaxOracle
from EV2Gym.ev2gym.baselines.heuristics import ChargeAsFastAsPossible

# Change current working directory to EV2Gym submodule directory
os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/EV2Gym")

config_file = "ev2gym/example_config_files/V2GProfitPlusLoads.yaml"

# Initialize the environment
env = EV2Gym(config_file=config_file,
              save_replay=True,
              save_plots=True)
state, _ = env.reset()
agent = V2GProfitMaxOracle(env,verbose=True) # optimal solution
#        or 
agent = ChargeAsFastAsPossible() # heuristic
for t in range(env.simulation_length):
    actions = agent.get_action(env) # get action from the agent/ algorithm
    new_state, reward, done, truncated, stats = env.step(actions) 
