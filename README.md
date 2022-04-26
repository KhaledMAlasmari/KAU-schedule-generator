# KAU schedule generator

This is a script that generates all possible schedules with no conflicts. You may ask, why not generate the best schedule possible? Well, that's subjective, _and It's definitely not that hard hahaha....._
## Installation

Use [pip](https://pip.pypa.io/en/stable/) to install the requirements

```bash
pip install -r requirements.txt
```

## Usage
Add the sections links for each course separately in a list then pass them to the function parse_info
```python 
course1 = parse_info(sections_204)
course2 = parse_info(sections_211)
course3 = parse_info(sections_212)
# you could add more if you want
```
Now you should have Course objects to use the generator on!
```python
schedules = get_all_possible_schedules(course1, course2, course3)
```

## Todo
- Improve the efficiency. _Somehow?_
- Convert this into a web app