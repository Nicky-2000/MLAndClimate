# Sunday April 28th - Sunday May 11th

Worked on finishing project and final paper. Note that the DQN stuff is on a separate branch from main.

# Sunday April 20th - Saturday April 27th

Mostly worked on preparing presentation slides and recording.

# Sunday April 13th - Saturday April 19th

Tuesday April 15th -- Have a working simulator!!
See Here: https://github.com/Nicky-2000/EV2Gym-DrivewayV1
- Note: it made more sense to abstract this out into another repo.
    So commits to EV2Gym-DrivewayV1 repo are just as important as commits to this repo

Note 2: When the simulator code in the other repo is fully working (with RL algo) then 
we will integrate it into this repo for our experiments.

# Sunday April 6th - Saturday April 12th
Dove very deep into EV2Gym simulator. Started to re work it so it will work for our simulation. 
Lots of work needs to be done here but it is doable!


# Sunday March 30th - Saturday April 5th
Mainly focused on problem set. Not too much work done.

# Sunday March 23rd - Saturday March 29th

Weekly Achievements: 
1. Read, understood, and tinkered with EV2Gym.
2. Started to set up some sample simulation envrionments.
3. Dicussed project with Nicolas and ideated a high level overview of our project report

Tentative Flow for Project Report (which guides how we will be running simulations): 

Centralized control and execution has been shown to be much more effective than centralized control decentralized execution in terms of coordinating DERs and EV charging

However, there are two main bottlenecks to this approach 
1: As the number of EVs / DERs increases the dimensionality of the optimisation increases. At some point it becomes computationally intractable to run certain algorithms

2: Privacy. Many people are, rightly, concerned about sharing their electricity usuage patterns with another entity. However, there is wiggle room here. Most people would be fine with sharing their data with their neighbour, what about their 10 neighbours... 
- If there is enough of an incentive (monetary) then I believe some people would be willing to do some partial datasharing.


Therefore, philosophically, we believe there is a sweet spot in regards to coordinated EV charging and discharging that would both computationally tractable and provide enough benefit to consumers to incentive them to accept sharing data at a local level. 


Methodology: 
Run simulations with 100 houses and one algorithm (iterate through the algos) controlling them all. Collect metrics

Run simulations with 100 houses split into two groups of 50 where each group is controlled by a separate algo (iterate through all the algos). Collect metrics at the 100 house scale (maybe we can have "Money Saved per house" metric)

Split into 4 groups of 25... repeat the same process.


We have 3 dimensions to our collected data. 
Dimension 1: Size of group, (this includes control algo runtime)
Dimension 2: Money Saved per house (compared to everyone just running 'Charge as Fast as Possible' algorithm)
Dimension 3: Type of Algo (different families scale better)


Ambitious Target for project:
If we can get to it... We will try to develop our own RL algo (potentially make a PR to EV2Gym with a new algo).


Action Items for next week:
1. Begin running simulations at scale.
2. Test at least 2 different algos on two different group scales.


# Sunday March 16th - Saturday March 22nd

Found a good simulation environment that can help us set up our experiment: https://github.com/StavrosOrf/EV2Gym
Looking into setting up the simulation environment.

EV2Gym Paper: https://arxiv.org/abs/2404.01849

Action Items for next week: 
1. Go through the EV2Gym repo and understand its capabilities and limitations
2. Set up config files that include about 100 houses each with an EV
3. Figure out how to have 100 houses being controlled together, Figure out how to make it so we can have groups of variables sizes being controlled together (so groups of 10 houses are individually controlled)

# Sunday March 9th - Saturday March 15th

- More reserach into RL for VPPs
- Read this paper: Reinforcement learning for electric vehicle applications in power systems: A critical review
    - Link: https://www.sciencedirect.com/science/article/pii/S1364032122009339

Reading this gave understanding of how RL is currently being used to control multiple power producing assets. 

What we got from this paper: We narrowed our focus onto the Vehicle 2 Grid subproblem in which the action set is {charge, discharge} for each vehicle. 
We also decided we were going to primarly focus on a "cost" metric since this seems like the most managable option. 

# Sunday March 2nd - Saturday March 8th
- Met to discuss the best datasources to use
- There are good tree datasets already out there to use as ground truth

- Atalanta has some interesting by-laws. 
- Specifically they require 1 tree for every 8 parking spots in a parking lot.
https://library.municode.com/ga/atlanta/codes/code_of_ordinances/177780?nodeId=PTIICOORENOR_CH158VE


Also looking into some Virtual Power Plant project. This seems like a more interesting space.
- Read a couple of review papers about data driven VPP control systems
- Trying to understand if it is possible to do something related to VPPs

# Sunday February 23rd - Saturday March 1st

Meet with Nicolas to discuss Arctic Ice and Forest Cover Projects. 
- Forest cover project appealed to him the most.
- Specifically the by-law compliance tree cover project seemed the most promising.
    - A tool / model that small towns could use would really improve enforcement of such by-laws. 
- We are not 100% satisfied with this idea. But we are going to write an abstract for it and go from there. 
- Another idea that has come into play is reinforcement learning for the best "tree planting policy". This idea has not been well formed yet.

# Sunday February 6th - Saturday February 22nd
David investigated data sources and project topics for arctic sea ice.
- High level ideas: 
    1. Causal link between Arctic Ice melting and sea level rise
    2. Predict regions of ice most likely to melt
    3. Forecast annual extent and concentration of sea ice 

Nicky investigated data sources and topics for forest/tree cover related projects
- High level ideas: 
    1. Monitor the change in forest cover in areas where companies have received carbon credits for planting trees (validating carbon credits)
    2. Making sure developers plant enough trees on their properties (validating by-law compliance).
    3. Detecting ideal locations to plant trees to stop deforestation (take into account the road network / how accessible a planting location is). 



# Sunday February 9th - Saturday February 15th
Formed group and started to brainstorm topics. The two ideas that stood out to us were Arctic Ice and Forest Cover related projects.
