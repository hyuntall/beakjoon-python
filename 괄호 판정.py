def validate_brace_pair(value):
    stack = []
    for idx in range(len(value)):
        if value[idx] == '{':
            stack.append(value[idx])
        else:
            if len(stack) > 0:
                stack.pop()
    if len(stack) > 0:
        print('유효하지 않은 중괄호 쌍입니다.')
    else:
        print('유효한 중괄호 쌍입니다.')

validate_brace_pair("{{}}{}")
validate_brace_pair("{{}")
validate_brace_pair("{{{}}}")
validate_brace_pair("}{{{}}}{")