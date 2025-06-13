"""
Descrição
    Uma empresa quer validar se os e-mails cadastrados pelos usuários estão no formato correto. Crie uma função que receba um e-mail e verifique se ele é válido, seguindo as regras:

📌 Regras para um e-mail válido:
    Deve conter o caractere "@" e um domínio, como gmail.com ou outlook.com.
    Não pode começar ou terminar com "@".
    Não pode conter espaços.

Entrada
    Uma string contendo o e-mail a ser validado.
Saída
    "E-mail válido" se o e-mail estiver no formato correto.
    "E-mail inválido" caso contrário.

Exemplos:
    Entrada	            Saída
    usuario@gmail.com	E-mail válido
    user@outlook.com	E-mail válido
    usuario gmail.com	E-mail inválido
"""
import re

class Email():
    def __init__(self, email: str):
        self.email: str = email
    
    def check_email(self, ) -> str:
        """
            Função para checar se um email é válido ou inválido

        Returns:
            str: Se o email for válido retorna "E-mail válido", caso contrário "E-mail inválido"
        """
        # Expressão regular onde verificar a estrutura do email que deve ser:
        # Conter um @
        # Antes do @ não pode haver nem @ e conter espaços
        # Depois do @ só pode sre domínio do gmail ou outlook
        valid = re.search(r"[^@\s]+@(gmail|outlook)\.com$", self.email) != None
        return "E-mail válido" if valid else "E-mail inválido"
    
# Entrada do usuário
email = input().strip()

print(Email(email).check_email())