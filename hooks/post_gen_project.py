'''
hook to delete datafile if not needed
'''
import os

def generate_datafile():
    datafile = "{{ cookiecutter.project_name }}_data.yaml"
    if "{{ cookiecutter.use_datafile }}".lower() != 'true':
        os.remove(os.path.join(os.getcwd(), datafile))

if __name__ == '__main__':
    generate_datafile()