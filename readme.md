# VerifyCPF

API em Python com Flask para validar o formato e os dígitos verificadores de um CPF.

## Requisitos

- Python 3
- pip

## Instalação

Na pasta do projeto, instale o Flask:

```bash
python -m pip install flask
```

## Executar

Com o código da API salvo em `app.py`, execute:

```bash
python -m flask --app app run
```

A API estará disponível em `http://127.0.0.1:5000`.

Se o arquivo tiver outro nome, substitua `app` pelo nome do arquivo sem a extensão `.py`.

## Validar um CPF

Envie uma requisição `POST` para `/validar-cpf`, com o cabeçalho `Content-Type: application/json` e o corpo:

```json
{
  "cpf": "529.982.247-25"
}
```

O CPF deve ser enviado como texto, com ou sem pontos e traço.

### Teste pelo PowerShell

```powershell
Invoke-RestMethod `
    -Uri "http://127.0.0.1:5000/validar-cpf" `
    -Method Post `
    -ContentType "application/json" `
    -Body '{"cpf":"529.982.247-25"}'
```

### Respostas

CPF válido — HTTP 200:

```json
{"valido": true}
```

CPF inválido — HTTP 200:

```json
{"valido": false}
```

Campo `cpf` ausente ou enviado em outro tipo — HTTP 400:

```json
{"erro": "Envie o campo 'cpf' como texto em um JSON."}
```

## Observações

A validação verifica o formato e os dígitos verificadores. Ela não consulta a existência ou a situação cadastral do CPF na Receita Federal.

O servidor iniciado pelo comando acima é destinado a testes locais.

