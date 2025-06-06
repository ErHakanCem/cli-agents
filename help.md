# How to Use It
As long as the Ollama desktop application is running (or you have run ollama serve in a terminal), your script will now work completely offline.

The commands to use it are exactly the same as before:

Bash

# Generate a command using your local Code Llama model
shelly "find all python files modified in the last 24 hours" --copy

# Generate and execute (with confirmation)
shelly "list current network connections" -e
You have now successfully created a powerful, private, and offline AI agent for your command line!
 
# Download a Code-Generation Model
Next, open your terminal and download a model. For generating shell commands, a model that is "instruct" or "code" trained is best. codellama is a great choice.

Run this command in your terminal:
ollama run codellama:7b-instruct

- codellama:7b-instruct: This is a 7-billion parameter version of Code Llama, specifically tuned to follow instructions. It's a good balance of size and capability.
- The first time you run this, it will download the model (which can be several gigabytes). After that, it will load it instantly. You can close the chat that appears after the download is complete.
