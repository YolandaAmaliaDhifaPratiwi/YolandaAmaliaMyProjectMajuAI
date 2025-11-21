# backend/agent_tools.py


def execute_function_safe(name, args):
# Whitelist mapping
    if name == 'run_code_snippet':
        code = args.get('code','')
# Do NOT execute arbitrary code in production. Here we simulate execution.
    return {'status':'ok','output':'(simulated) executed code snippet. Output: ...'}
    if name == 'get_course_section':
        section = args.get('section','')
    return {'status':'ok','content':f'(simulated) content for {section}'}
    return {'error':'unknown function'}
