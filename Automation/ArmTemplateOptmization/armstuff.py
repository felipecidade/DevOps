from armparser import ARMTemplateParser
from readmeFile import readmFile
import sys
def main(parameters):

    if paramenters[1] == '-h':
        print (

        )
    arm_template_path = "path/to/your/template.json"
    readme_path = "README.md"

    parser = ARMTemplateParser(arm_template_path)
    markdown_content = generate_markdown(parser)
    write_to_file(markdown_content, readme_path)
    print("README generated successfully.")

if __name__ == "__main__":
    parameters = sys.argv

    if len(parameters) < 2:
        main(parameters)
    else:
        print ('Invalid paramenters type -h for help.')
