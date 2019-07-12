from jinja2 import Environment, FileSystemLoader
import os

# capture our current directory
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def generate_datafile():
    src_file = "../{{ cookiecutter.project_name }}/data/template_datafile.yaml"
    
    if "true" in "{{ cookiecutter.include_datafile }}".lower(): # yes, include the datafile
        filename = "{{ cookiecutter.datafile_name }}"
        dest_file = "../{{ cookiecutter.project_name }}/data/" + filename + ".yaml"
        os.rename(src_file, dest_file)
    else: # no, don't include the datafile
        os.remove(src_file)

if __name__ == '__main__':
    generate_datafile()