
from pybricks.tools import hub_menu

# Make a menu to choose a letter. You can also use numbers.
selected = hub_menu("1", "2", "3", "4", "5")

# Based on the selection, run a program.
if selected == "1":
    import ThingaMaBobber
elif selected == "2":
    import thegrabythigy
elif selected == "3":
    import duboldouolingo9
elif selected == "4":
    import coralpusher
elif selected == "5":
    import BoBbObBoater