## The Impact of Coordination Scale on Vehicle-to-Grid Reinforcement Learning Optimization 

`abstract.md` contains a brief description of the project and it's goals

`journal.md` contains our weekly updates on the projects progress


## Repo Setup Instructions
Clone the repo and the submodules (submodule is EV2Gym: https://github.com/StavrosOrf/EV2Gym )
``` bash
git clone --recurse-submodules git@github.com:Nicky-2000/MLAndClimate.git
git submodule update --init --recursive
```

Create a virtual environment. **NOTE: You must use Python <= 3.9**
```bash
python3 -m venv venv
```

Activate virtual environment 

```bash
source venv/bin/activate
```

From the root of the repo install the dependencies:

```bash
pip install -r EV2Gym/requirements.txt
pip install -e EV2Gym 
```
Note: `pip install -e EV2Gym` makes it so all the changes made to the EV2Gym code are automatically included in the environment so you don't have to re-install it.



