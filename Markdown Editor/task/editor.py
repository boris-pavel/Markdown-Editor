formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line', 'ordered-list', 'unordered-list']
special_commands = ['!help', '!done']


def show_help():
    print('Available formatters: ', end='')
    for f in formatters:
        print(f, end=' ')
    print('')
    print('Special commands: ', end='')
    for c in special_commands:
        print(c, end=' ')
    print('')


def save_result(text):
    file = open('output.md', 'w', encoding='utf-8')
    file.write(text)
    file.close()
    exit()


def get_plain():
    return input('Text: ')


def make_bold():
    text = input('Text: ')
    return f'**{text}**'


def make_italic():
    text = input('Text: ')
    return f'*{text}*'


def make_header():
    while True:
        try:
            level = int(input('Level: '))
            if level < 1 or level > 6:
                raise ValueError
            text = input('Text: ')
            return f'{"#" * level} {text}\n'
        except ValueError:
            print('The level should be within the range of 1 to 6')
            continue


def make_link():
    label = input('Label: ')
    url = input('URL: ')
    return f'[{label}]({url})'


def make_inline_code():
    text = input('Text: ')
    return f'`{text}`'


def make_list(list_type):
    while True:
        rows = int(input('Number of rows: '))
        if rows > 0:
            break
        print('The number of rows should be greater than zero')
    elements = []
    text = ""
    for i in range(1, rows + 1):
        elements.append(input(f'Row #{i}: '))
    match list_type:
        case 'ordered':
            for i in range(0, len(elements)):
                text += f'{i + 1}. {elements[i]}\n'
        case 'unordered':
            for i in elements:
                text += f'* {i}\n'
    return text


def main():
    markdown = ""
    while True:
        user_input = input('Choose a formatter: ')
        if user_input in formatters:
            match user_input:
                case 'plain':
                    markdown += get_plain()
                case 'bold':
                    markdown += make_bold()
                case 'italic':
                    markdown += make_italic()
                case 'inline-code':
                    markdown += make_inline_code()
                case 'link':
                    markdown += make_link()
                case 'header':
                    if markdown != "":
                        markdown += '\n'
                    markdown += make_header()
                case 'new-line':
                    markdown += '\n'
                case 'ordered-list':
                    markdown += make_list('ordered')
                case 'unordered-list':
                    markdown += make_list('unordered')
            print(markdown)
            continue
        if user_input == '!help':
            show_help()
            continue
        if user_input == '!done':
            save_result(markdown)
        print('Unknown formatting type or command')


main()
