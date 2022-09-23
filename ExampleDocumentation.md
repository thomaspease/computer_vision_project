# Example Project Documentation Guideline

> Include here a brief description of the project, what technologies are used etc.

## Milestone 2

Using Google's 'Teachable machine' (https://teachablemachine.withgoogle.com/) I trained a model which recognises the gestures 'rock', 'paper', 'scissors' and 'nothing'. This was then downloaded for use with Tensorflow.

## Milestone 3

The bulk of this milestone was to set up a conda environment for the project. It was necessary to install OpenCV (an open source computer vision lib), Tensorflow (which will be used to make predictions based on the trained model), and ipykernel.

## Milestone 4

This milestone involved the creation of a manual RPS game. A random integer between 0-2, which pertains to the different choices in the game - 0 = rock - 1 = paper - 2 = scissors

Based on the classic rules of RPS, the get_winner function then works out the winner. The game logic was the most challenging part of this milestone. I found that depending on the result of subtracting one player's choice from the other, a winner is produced:

```python
if comp_choice - user_choice == -1 or comp_choice - user_choice == 2:
      return 1 #user
    elif comp_choice - user_choice == -2 or comp_choice - user_choice == 1:
      return 2 #computer
    else:
      return 0 #draw
```

## Milestone 1

- Answer some of these questions in the next few bullet points. What have you built? What technologies have you used? Why have you used those?

- Example: The FastAPI framework allows for fast and easy construction of APIs and is combined with pydantic, which is used to assert the data types of all incoming data to allow for easier processing later on. The server is ran locally using uvicorn, a library for ASGI server implementation.

```python
"""Insert your code here"""
```

> Insert an image/screenshot of what you have built so far here.

## Milestone 2

- Does what you have built in this milestone connect to the previous one? If so explain how. What technologies are used? Why have you used them? Have you run any commands in the terminal? If so insert them using backticks (To get syntax highlighting for code snippets add the language after the first backticks).

- Example below:

```bash
/bin/kafka-topics.sh --list --zookeeper 127.0.0.1:2181
```

- The above command is used to check whether the topic has been created successfully, once confirmed the API script is edited to send data to the created kafka topic. The docker container has an attached volume which allows editing of files to persist on the container. The result of this is below:

```python
"""Insert your code here"""
```

> Insert screenshot of what you have built working.

## Milestone n

- Continue this process for every milestone, making sure to display clear understanding of each task and the concepts behind them as well as understanding of the technologies used.

- Also don't forget to include code snippets and screenshots of the system you are building, it gives proof as well as it being an easy way to evidence your experience!

## Conclusions

- Maybe write a conclusion to the project, what you understood about it and also how you would improve it or take it further.

- Read through your documentation, do you understand everything you've written? Is everything clear and cohesive?
