# Drill 2
from pyscript import display, document

# Confirmed members
grade_7 = {'Jayvee', 'Callin'}
grade_8 = {'Gabriel', 'Philbert'}
grade_9 = {'Iselda', 'Cornifer'}
grade_10 = {'Ogrim', 'Dante'}

new_members = set()

def update_display():
    # Combines all sets and updates the page output 
    updated_set = grade_7 | grade_8 | grade_9 | grade_10 | new_members
    members_formatted = ', '.join(updated_set)
    total_count = len(updated_set)

    document.getElementById("member_list_display").innerHTML = f"<p><b>Members:</b> {members_formatted}</p>"
    document.getElementById("total_count_display").innerHTML = f"<p><b>Total Members:</b> {total_count}</p>"

def add_member(event=None):
    global new_members

    # Get input values
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()
    
    full_name = f"{first_name} {last_name}".strip()
    
    # Set difference prevents adding empty string if inputs were blank
    confirmed_set = {full_name} - {""}
    new_members |= confirmed_set

    # Clear input text boxes
    document.getElementById("first_name").value = ""
    document.getElementById("last_name").value = ""

    # Refresh the member list display
    update_display()

# Display the initial member list and count when the page loads
update_display()