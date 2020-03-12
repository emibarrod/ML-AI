# Differences between Trainig, Validation and Test data 

## Training

As it name says, we train our model with this data. The model tries to fit to this data, so we have to take care of 
overfitting, but of underfitting too.

## Validation

We must not confuse it with test data. With validation data, we take care of our model to be well balanced, 
and to prove our model's architecture to be ok. This is, if we tune our models parameters, we need a set of 
data in wich we not have data leak, because if we tune our parameters according to our test data, we are tunning 
our parameters to optimize test outcome, so we have data leak.

## Test

The data where we check the model's performance.
