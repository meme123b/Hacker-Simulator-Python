from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.history import FileHistory

# 自定义补全器
class MyCustomCompleter(Completer):
    def get_completions(self, document, complete_event):
        # 定义可能的补全选项
        options = ['exit', 'dc', 'disconnect', 'clear', 'SSHCrack', 'FTPSprint', 'SMTP_Mail_Server', 'WEB_Server_Wrom', 'Secure_Sockets_Layer', 'SQL_Output']

        # 获取当前输入的文本，并转换为小写
        text_before_cursor = document.text_before_cursor.lower()

        # 遍历所有可能的补全选项
        for option in options:
            # 将选项也转换为小写进行比较
            if option.lower().startswith(text_before_cursor):
                yield Completion(option, start_position=-len(text_before_cursor))

def Input_Toolkit(ts=''):
    # 使用 prompt_toolkit 提示用户输入，并使用自定义补全器
    # 同时启用历史命令记录
    try:
        history = FileHistory('.command_history')
        return prompt(ts, completer=MyCustomCompleter(), history=history).lower()
    except KeyboardInterrupt:
        exit()

if __name__ == '__main__':
    # 测试
    while True:
        user_input = Input_Toolkit('Enter a command: ')
        print(f'You entered: {user_input}')
