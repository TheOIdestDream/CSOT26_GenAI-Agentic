Created a class ChatBot , each bot will be independent with customizable model and base url
Made 4 methods
Method 1 - To initialize
Method 2 - call_model - Runs a single prompt and its output and stores it in the messages so that the chatbot remembers.Also displays total tokens used
Method 3 - summary - In case the messages history overflows N(Here I took N as 25) it summarizes it into a single message using the same call_model
                     Also used in case the user asks for a summary
Method 4 - run_model - Main method to start the model. Takes model as input and continously runs call_model until the user asks to "Exit"
                       Also calls the summary method in case user asks for a summary of the conversation
Mostly used the base framework given in build1 and build 2
Tried implementing streaming but missed a few details
