# 📧 Validador de E-mail

Este projeto consiste em uma aplicação simples em Python que **valida o formato de um e-mail** com base em regras pré-definidas. A verificação é feita utilizando **expressões regulares**, garantindo que o e-mail esteja em um padrão aceito por um sistema fictício da empresa.

---

## ✅ Regras de Validação

Para um e-mail ser considerado **válido**, ele deve:

1. Conter o caractere `@`.
2. Não começar ou terminar com `@`.
3. Não conter espaços.
4. Conter um domínio **@gmail.com** ou **@outlook.com**.

---

## 💡 Exemplo de Funcionamento

| Entrada                | Saída          |
|------------------------|----------------|
| `usuario@gmail.com`    | E-mail válido  |
| `user@outlook.com`     | E-mail válido  |
| `usuario gmail.com`    | E-mail inválido|
| `@gmail.com`           | E-mail inválido|
| `usuario@exemplo.com`  | E-mail inválido|

---

## 📦 Estrutura do Código

### Classe `Email`

```python
class Email():
    def __init__(self, email: str):
        self.email = email

    def check_email(self) -> str:
        # Valida se o e-mail está em formato aceito
        return "E-mail válido" if <condição> else "E-mail inválido"
```

A validação é feita com uma **expressão regular** que verifica:

- Parte antes do `@` não deve conter `@` ou espaços.
- Parte depois do `@` deve ser `gmail.com` ou `outlook.com`.

---

## ▶️ Como Usar

1. Crie um arquivo Python, por exemplo `validador_email.py`, com o código fornecido.
2. Execute no terminal:

```bash
python validador_email.py
```

3. Digite um e-mail quando solicitado.
4. O resultado será:

```
E-mail válido
```
ou
```
E-mail inválido
```

---

## ⚠️ Possíveis Erros

| Situação | Erro/Comportamento |
|----------|---------------------|
| E-mail sem `@` | E-mail inválido |
| Domínio inválido | E-mail inválido |
| Espaços no e-mail | E-mail inválido |
| Domínios não permitidos | E-mail inválido |

---

## ✏️ Sugestões de Melhorias

- Permitir múltiplos domínios (ex: `hotmail.com`, `yahoo.com`).
- Adicionar testes unitários.
- Criar interface de usuário (CLI ou Web).
- Implementar uma lista de domínios confiáveis externos.

---

## 📄 Licença

Este projeto é de uso livre para fins educacionais ou corporativos internos.