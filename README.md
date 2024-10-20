# python_challenge
Python Challenge for Module 3


I attempted the PyBank challenge first, using detailed notes and examples from class. This code was approached segment by segment, at first attempting to put all dates and profits & losses in one dictionary to find the max and min and use the length function to find the total # of months. I also approached first by using multiple For Loops, as well as printing each output separately/ one at a time). This caused a few problems, which probed me to re-evaluate:
    1. The dictionary method would have allowed me to easily print out date and amount, but made it harder to determine the max and min
    2. Though this is a small dataset, multiple for loops could cause time lags on larger datasets 
    3. When using the length function in #1, I only got 85 months (vs. the actual total of 86)
    4. Though printing out each output as I went through each segment provided the correct output, it was inefficient as I had to retype everything when writing to the output file.
    
Because of these limitations with the original code, I worked with a tutor as well as the class skeleton to properly and efficiently get the correct outputs.

In my original attempt, I took a different approach of calculating the average change by incorporating a DEF function, and decided to keep this in my second attempt. 

I was able to apply my learnings from the PyBank challenge to the PyPoll challenge, using tickers to add votes to each candidate as it went through the For loop, using a DEF function to calculate percentage of votes, and writing the output for both Terminal and CSV in one segment.

Learning resources: In class personal notes, online forums (Stack overflow to answer questions on DEF functions), tutoring sessions and the PyBank/PyPoll skeletons to track errors and de-bug.
