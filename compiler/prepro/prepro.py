import re

class PrePro:
    '''
    Responsável pelo pré processamento da cadeia. 
    Retirando comentários.
    '''
    @staticmethod
    def filter(code: str) -> str:
        code = re.sub(r"\s*//.*", "", code)

        if (len(code) == 1 and code == '\n'):
            # Linha apenas com apenas \n pós substituição
            return ''

        return code

    @staticmethod
    def pre_pro(lines_code: list[str]) -> str:
        code = ''
        for line in lines_code:
            code += PrePro().filter(line)

        return code
