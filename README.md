# AutomaticKahootBot
Kahoot Bot that searches for the answers itself.

**Pros:**
 - Searches for the answers itself (when provided with a link).
 - Plays itself.
 - Can join kahoot at any point and get answers correctly immediatly.
 - Has a realistic mode where answer times are randomized.
 
**Cons:**
 - Can be tricked by randomizing questions and answers or by using question types like true or false, type answer, puzzle, poll or slide.
 - Can't join if there is 2 step join (pattern confirm), if name is already in use or if are picked by spinning the wheel.


# Usage:
```
from KahootBot import KahootBot
kahoot_bot = KahootBot()
kahoot_bot.play(kahoot_nickname="Bob The Bot", kahoot_pin="12345", kahoot_url="https://create.kahoot.it/details/captain-marvels-universe/5668edff-c2bb-4193-b09f-ff9637685a50", is_realistic=True)
```


# What is kahoot?
https://kahoot.com/what-is-kahoot/
