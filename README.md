## Capstone 

By David Marmor 

## Predicting Pitch Success 

## Background 

Major League Baseball (MLB) is the highest level of professional baseball in the world. It has been around for over a century but statistics and data have greatly changed the way teams are run in the last 20 years. Originally teams used baseball data that had been collected publicly for years and just looked at it in a more analytical light. But in recent years, as more teams started buying into analytic departments, teams have been looking for new edges by studying new information. One of the biggest sources of new data is the Statcast sensors which were installed in every MLB stadium in 2015. Statcast uses 12 tracking cameras placed around the field to track several aspects of every play that occurs during MLB games. Five of the cameras track pitches specifically, while the other 7 track batted balls and players. Statcast provides MLB teams with a level of pitch-by-pitch detail that did not exist before. Teams are able to use the data in their decision-making process. The collected data is also available to the public. 

## Problem Statement 

One way statcast data is used is by pitchers and teams to work on pitch characteristics. Pitchers can try different pitch grips and motions and see how that impacts the pitch data and results. There are many ways to measure pitch success. To be a successful pitcher one important thing is being able to generate swings and misses (known as whiffs). 

Can we predict whiffs using pitch characteristic data? In addition to having good model, the goal is to determine which characteristics of a pitch are most important to pitch success and how they vary by pitch type. With this information pitchers could work on the specific characteristics that matter the most for each pitch. That could allow them to optimize pitchs more effectively. 

A variety of models will be tried for each pitch. The target metric will be accuracy. In this case neither type of error is inherently worse than the other. The goal is to create a model that can accurately predict when a pitch will be a whiff and when it will not. 

Models will be constructed for each pitch thrown at least 2000 times in the dataset. Overall there are 9 pitches that meet the condition. 

## Data Dictonary 

|Feature|Description|
|---|---|
|**release_speed**|speed of pitch when it is released (miles per hour)| 
|**release_spin_rate**|spin rate of pitch when it is released (revolutions per minute)|
|**zone**|location of the ball as it crosses the plate|
|**vx0**|speed of the ball in the horizontal direction 50 feet from the plate (feet per second)|
|**vy0**|speed of the ball towards the plate 50 feet from the plate (feet per second)| 
|**vz0**|speed of the ball in the vertical direction 50 feet from the plate (feet per second)|
|**ax**|acceleration of the ball in the horizontal direction (feet per second squared)| 
|**ay**|acceleration of the ball towards the plate (feet per second squared)|
|**az**|acceleration of the ball in the vertical direction (feet per second squared)| 
|**pfx_x**|horizontal movement (feet)|
|**pfx_z**|vertical movement (feet)| 
|**spin_axis**|direction the pitch is spining (in degrees)|
|**description**|for pitches that were swung at was it missed (1) or hit (0)| 
|**pitch name**|which pitch was thrown| 

## Analysis 

The random forests model is the best model for all 9 pitches. The other models tried were nueral networks, gradient boosting, and logistic regression. 

|Pitch|Random Forests accuracy on test data|
|---|---|
|**Fastball**|0.92| 
|**Sinker**|0.96|
|**Slider**|0.82|
|**Change**|0.83|
|**Curve**|0.85| 
|**Cutter**|0.89|
|**Knuckle Curve**|0.84| 
|**Splitter**|0.79|
|**Knuckleball**|0.91| 

For fastballs, sinkers, changeups, splitters, and knuckleballs speed is the most important factor. For sliders, curves, and knuckle curves location is the most important factor. For cutters speed and location are about equally important.

## Conclusion 

We can successfully model whether pitches are swung and missed at. Random Forests are our best model for doing so. The most important pitch characteristics do vary by pitch type. Pitchers and teams can use our model to determine what skills are the most important to work on for each pitch. Using the app they can see what average characteristics they have to reach so they can generate more whiffs. 

## Future Work

The models can be further optimizted and more features can be included. In addition more model types can be tried to see if they can be more accurate then random forests. Whiffs are not the only measure of success. Future models could included soft contact as being a success. In addition pitches that are not swung on can be important as well. Another step to take is creating streamlit apps for all pitch types. 