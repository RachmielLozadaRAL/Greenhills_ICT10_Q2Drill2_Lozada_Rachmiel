# Seatwork 1
from pyscript import display, document

def student_guild(e):
    document.getElementById('output').innerHTML = ' '
    student_name = document.getElementById('student_name').value
    math_members = ['Canuday', 'Chua', 'Lozada', 'Padua', 'Paulino', 'Villante', 'canuday', 'chua', 'lozada', 'padua', 'paulino', 'villante']
    member_checker = student_name in math_members

    display_message = (f'Sorry, you are not smart enough. Study more.', f'Congratulations! {student_name}, you are now part of the OBMC Math club moderated by Mr. Ferma.')
    display(display_message[member_checker], target='output')