import json

class ARMTemplateParser:
    def __init__(self, template_path):
        self.template_path = template_path
        self.template = self._load_template()

    def _load_template(self):
        with open(self.template_path, 'r') as file:
            return json.load(file)

    def get_resources(self):
        return self.template.get('resources', [])

    def get_parameters(self):
        return self.template.get('parameters', {})

    def get_outputs(self):
        return self.template.get('outputs', {})

    def get_functions(self):
        return self.template.get('functions', {})
    
    def get_variables(self):
        return self.template.get('variables', {})