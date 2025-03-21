## Abstract


## The Impact of Coordination Scale on Vehicle-to-Grid Reinforcement Learning Optimization 



Electric vehicles are an increasingly relevant power asset as their adoption continues to increase. There is significant potential to increase cost savings and decrease peak grid load with efficient management of the charging and discharging of EV batteries. It has been shown that centrally coordinating the charging of multiple EVs does result in such benifits (Get Source for this... There are lots). However, there are two large problems with this centralized control approach. Firstly, there are privacy concerns with sharing your electricity usuage data with a central entity. Secondly, as the number of centrally controlled units (houses) increases it becomes computationally intractable to coordinate them all. These two problems have led to many trying to develop RL agents that act based only on the observations of a single unit (household). However, systems with mulitple RL agents acting independantly often perform worse than centrally controlled systems.

This project investigates how the scale of coordinated EV groups impacts the efficiency of Vehicle-to-Grid (V2G) systems. Specifically, we will examine how system performance (cost, computational efficiency of RL algorithm) varies as we alter the size and number of independently coordinated groups within a fixed-size neighborhood.


We will use EV2Gym (an open source RL learning environment for V2G algorithms) to simulate a neigbourhood of 100 households (if it is possible we will try to scale this number up).Each of these households will have realistic and diverse EV usuage patterns. We will run many different simulations where we systematically vary the number of coordination groups. For example, coordinating all 100 households in a single group represents full centralization, while dividing them into 2, 4, 10, or even 20 groups demonstrates increasingly decentralized management, with fewer EVs per group. For each of these "group sizes" we will run a simulation using some of the standard RL algorithms detailed in this paper: https://www.sciencedirect.com/science/article/pii/S1364032122009339.

We are aiming to evaluate two key metrics: 
1. Cost savings
2. Efficiency of the algorithm




# OLD ABSTRACT now Deprecated!!
## Scalable Compliance Monitoring of Tree Cover By-Laws in Municipalities

In order to enforce a community's green space by-laws, it is essential to have accurate tree planting/cover data. This project aims to develop a scalable system for detecting tree planting compliance violations by property developers.

We will use satellite imagery and biomass data (e.g., GEDI) to build a ML model capable of estimating tree cover in urban and suburban areas. To ensure accuracy, we will fine-tune a model (probably a segmentation model?) and use Boston and New York’s tree datasets as ground truth for this fine-tuning process. We will then cross reference our model's tree cover estimates with municipalities' by-laws to try and identify discrepancies between mandated tree coverage and actual tree coverage.
- To extract tree cover guidelines from municipality by-laws, at scale, we will look into developing a DocETL or DSPy agent workflow enabling us to parse the by-laws of many different municipalities. If this is unfeasible, we will scope the project down to exploring one or two municipalites.

This project is valuable because it could provide small municipalities with a cost-effective tool for monitoring compliance, helping them enforce tree-planting regulations without expensive and time consuming inspections. Additionally, should this project prove successful, we could apply a similar methodology to verify reforestation carbon credits (i.e., compare reported tree planting with real-world satellite/biomass data).
