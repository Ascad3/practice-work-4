def valid(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
    return not stack

def min_changes(s):
    open_count = close_count = 0
    changes = 0

    for char in s:
        if char == '(':
            open_count += 1
        elif char == ')':
            if open_count > 0:
                open_count -= 1
            else:
                close_count += 1

    changes = open_count + close_count
    return changes

# Пример использования функций
while True:
    print("Введите строку скобок"
          "\nДля завершения программы введите stop")
    string = input()
    if string == "stop":
        break
    if all(c in '()' for c in string):
        print("Последовательность правильная:", valid(string))
        print("Минимальное необходимое количество изменений:", min_changes(string))
    else:
        print("Введите корректную строку")
        continue
