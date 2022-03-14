# Exercises HackerRank
In this reposotory you will find some exercises's HackerRank but first I invite you to try resolve them. 
Good luck!!

## Exercises:
### 1. Pile of socks:
  There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks       with matching colors there are.

  Example:
  n = 7
  ar = [1,2,1,2,1,3,2]

  There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is 2.

### 2. Steps Of AHiker
  An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly steps steps, for every step it was noted if it was an uphill, U, or   a downhill, D step. Hikes always start and end at sea level, and each step up or down represents a 1 unit change in altitude. We define the following terms:

  A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
  A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
  Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

  Example

  steps = 8 path = [UDDDUDUU]


  The hiker first enters a valley 2 units deep. Then they climb out and up onto a mountain 2 units high. Finally, the hiker returns to sea level and ends the hike.

  Function Description

  Complete the countingValleys function in the editor below.

  countingValleys has the following parameter(s):

  int steps: the number of steps on the hike
  string path: a string describing the path
  Returns

  int: the number of valleys traversed
