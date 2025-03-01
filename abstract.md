## Abstract

## Scalable Compliance Monitoring of Tree Cover By-Laws in Municipalities

In order to enforce a community's green space by-laws, it is essential to have accurate tree planting/cover data. This project aims to develop a scalable system for detecting tree planting compliance violations by property developers.

We will use satellite imagery and biomass data (e.g., GEDI) to build a ML model capable of estimating tree cover in urban and suburban areas. To ensure accuracy, we will fine-tune a model (probably a segmentation model?) and use Boston and New York’s tree datasets as ground truth for this fine-tuning process. We will then cross reference our model's tree cover estimates with municipalities' by-laws to try and identify discrepancies between mandated tree coverage and actual tree coverage.
- To extract tree cover guidelines from municipality by-laws, at scale, we will look into developing a DocETL or DSPy agent workflow enabling us to parse the by-laws of many different municipalities. If this is unfeasible, we will scope the project down to exploring one or two municipalites.

This project is valuable because it could provide small municipalities with a cost-effective tool for monitoring compliance, helping them enforce tree-planting regulations without expensive and time consuming inspections. Additionally, should this project prove successful, we could apply a similar methodology to verify reforestation carbon credits (i.e., compare reported tree planting with real-world satellite/biomass data).
