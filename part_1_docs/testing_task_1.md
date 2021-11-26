### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    # uses the assignment operator rather than the 
    # equality comparison operator
    if card.value = 1:
      return True
    # else statement should be followed by a colon
    else
      return False
   
  # should use def to define the method, should have a comma 
  # between card1 and card2 in the parameter list
  # may need a condition for when the card values are equal
  dif highest_card(self, card1 card2):
  # body of the method is not indented
  if card1.value > card2.value:
    # card is not defined in method scope, should be card1
    return card
  else:
    return card2
  

# method should be indented, not defined in the class
# but takes self as first parameter
def cards_total(self, cards):
  # total should be initialized with a value, presumably 0
  total
  for card in cards:
    total += card.value
    # return statement is in the body of the for loop
    # will return the value of the first card in cards only
    return "You have a total of" + total
  
```
