to_do_notes = []

while True:
    note = input()
    if note == 'End':
        break
    to_do_notes.append(note)

sorted_notes = sorted(to_do_notes, key= lambda x: int(x.split('-')[0]))
print([note.split('-')[1] for note in sorted_notes])


