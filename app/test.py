from docx import Document

# Load your existing Word document
doc = Document( r"D:\almanac_2026\almanac-2026\Alabama\Congressional Districts\2026 - Cong. Districts – AL.docx")

# Unicode character for an unchecked box and checked box
unchecked_box = '\u2610'  # ☐
checked_box = '\u2611'  # ☑

# List of keywords to identify the items where you want checkboxes
keywords = ["AUTHOR", "EDITORIAL BOARD REVIEW", "AUTHOR 2ND SUBMISSION", 
            "EDITORIAL BOARD 2ND REVIEW", "COPY EDITOR", "CBIS"]

# Iterate through each paragraph and add an unchecked checkbox if it contains any keywordt
for paragraph in doc.paragraphs:
    for keyword in keywords:
        if keyword in paragraph.text:
            # Add unchecked box at the beginning of the paragraph
            paragraph.text = f"{checked_box} {paragraph.text}"
            break

# Save the modified document
doc.save('modified_document.docx')
