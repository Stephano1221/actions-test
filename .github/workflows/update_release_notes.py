import sys
import textwrap
 
version_number = sys.argv[1]
release_date = sys.argv[2]
wiki_link = sys.argv[3]
 
vnext = "## v.next"
release_note = textwrap.dedent(f"""\
    {vnext}
    
    ## v{version_number} - {release_date}
    - Full details can be found in the [release notes]({wiki_link})\
""")
 
path = "./RELEASENOTES.md"
file = open(path)
release_notes = file.read()
file.close()
 
release_notes = release_notes.replace(vnext, release_note, 1)
 
file = open(path, "w")
file.write(release_notes)
file.close()
