# Brief overview : AI Engineering

![A real feast](images/image.jpeg)ç

## Explainer
In context learning - model will learn new information from the prompts, for example if the python documentation is outside the knowledge cutoff the model will learn from the prompt which save these new prompts from getting outdated 

Each example provided is called a shot

And using few examples to teach the model how to respond is called few shot prompting 

If no example was given then it becomes zero shot prompting 
Which seems to be the case for most of the latest models for most of the time

The number of examples are limited by the models context length and this barrier has also surpassed by latest gemini models and the upcoming DL paradigm which is called Titan if it come to see the day (not sure google will opensource the  exact model data)

If the system prompt and the user prompt was given the model will combine the two following a template 

## Defender

Why having a better system prompt is good - she mentions two possible reasons, one is the system prompt is being fed into the system first then so it will prime the model to answer the user prompt most effectively 

Second some of the models seems to be made to look for system prompts and pay more attention to the system prompt and closely follow the instructions given in the prompt 

Not all parts in a prompt are equal, model is much better at understanding the prompt at the begging and the end. 

There is test to check this which is called a needle in the haystack, - a piece of information is being fed into different parts of the prompt and ask the model to find it 

When prompting adhere to following best practices
* Write clearly[^1]
* Ask the model to adopt a persona
* Provide examples 
* Specify the output format - you can ask to avoid unnecessary preambles 
* Provide sufficient context - which will save the model from hallucinating 
* Break complex tasks into subtasks 
* Give the model time to think - this is same as chain of though prompting and this seems to be less used in the industry because of the recent reasoning models, CoT thinking is more intuit into these newer models - this is also known as self critique techniques 


⠀
Best thing is to have a separate prompts.py file

You can use the pydantic BaseModel to ensure type safety 

This is how the neural networks are taught - or more specifically trained - this part is not the natural order I need to have in this particular document but this part is important 

The method used to train NN - backpropagation 

It has two parts - forward pass and backward pass 

During the forward pass - computing the output from the input 

Backward pass - updating the model weights according to the aggregated signal of the forward pass

Oversimplified version of what’s happen during the backwardness is like this

1. The computed values of the forward pass is compared with the expected values which are knowns as ground truths - if these show significant variations then it is called LOSS - the main aim of an NN is to minimize this number

2. How much this variation is caused by adjusting the parameters can be identified and calculated using the GRADIENT - this is the derivative of the loss respect to each trainable parameter
3. Trainable parameters are adjusted accordingly , how much the parameter has to be adjusted is determined by an OPTIMIZER - like SGD and ADAM - transformers use Adam 











[^1]: this is the first reference 
