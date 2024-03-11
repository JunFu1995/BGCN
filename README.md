# Bayesian-Graph-Convolutional-Network-for-Traffic-Prediction

## TODO
- [x] ~~Code release~~ 
- [ ] Release the code for calculating the posteriori of the road network 

## Introduction
For the convenience of comparison, we integrate the proposed BGCN into an open library for urban spatial-temporal data mining, called [LibCity](https://github.com/LibCity/Bigscity-LibCity?tab=readme-ov-file). 

For the implementation details of BGCN, please see the file "libcity/model/traffic_speed_prediction/BGCN.py".

## Train and Test
First, download datasets following the instructions in [LibCity](https://github.com/LibCity/Bigscity-LibCity?tab=readme-ov-file).  

Second, train and test the model using the following command:
```
python run_model.py --task traffic_state_pred --model BGCN --dataset PeMS07
```
The results are recorded in the folder "libcity/log".
## Acknowledgement
This project is based on [LibCity](https://github.com/LibCity/Bigscity-LibCity?tab=readme-ov-file). Thanks for the awesome work.

## Citation
Please cite the following paper if you use this repository in your reseach.
```
@article{FU2024127507,
title = {Bayesian graph convolutional network for traffic prediction},
journal = {Neurocomputing},
pages = {127507},
year = {2024},
issn = {0925-2312},
doi = {https://doi.org/10.1016/j.neucom.2024.127507},
url = {https://www.sciencedirect.com/science/article/pii/S0925231224002789},
author = {Jun Fu and Wei Zhou and Zhibo Chen},
keywords = {Traffic prediction, Bayesian, Generative model},
}
```
## Contact
For any questions, feel free to contact: `fujun@mail.ustc.edu.cn`