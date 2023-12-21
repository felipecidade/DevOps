from armparser import armParser

class gerenerateMarkdow:
    def generate_markdown(template):
        md_content = "# README for ARM Template\n\n"

        # Overview (Needs manual editing)
        md_content += "## Overview\n\n"
        md_content += "This ARM template deploys the following resources. Please update this section with more details.\n\n"

        # Resources Table
        md_content += "## Resources\n\n"
        md_content += "| Resource Type | API Version |\n"
        md_content += "| --- | --- |\n"
        for resource in template.get('resources', []):
            md_content += f"| {resource['type']} | {resource['apiVersion']} |\n"

        # Parameters Table
        md_content += "\n## Parameters\n\n"
        md_content += "| Name | Type | Default Value | Description |\n"
        md_content += "| --- | --- | --- | --- |\n"
        for name, param in template.get('parameters', {}).items():
            default_value = param.get('defaultValue', 'None')
            description = param.get('metadata', {}).get('description', 'No description provided')
            md_content += f"| {name} | {param['type']} | {default_value} | {description} |\n"

        # Outputs Table
        md_content += "\n## Outputs\n\n"
        md_content += "| Name | Type | Description |\n"
        md_content += "| --- | --- | --- |\n"
        for name, output in template.get('outputs', {}).items():
            description = output.get('metadata', {}).get('description', 'No description provided')
            md_content += f"| {name} | {output['type']} | {description} |\n"

        return md_content

def write_to_file(content, filename):
    with open('readme.md', 'w') as file:
        file.write(content)