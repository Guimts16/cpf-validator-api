from flask import Flask, request

app = Flask(__name__)


def cpf_ok(cpf):
    cpf = cpf.strip().replace(".", "").replace("-", "")

    if len(cpf) != 11 or any(c not in "0123456789" for c in cpf):
        return False

    d = [int(c) for c in cpf]

    if len(set(d)) == 1:
        return False

    for i in range(9, 11):
        s = sum(d[j] * (i + 1 - j) for j in range(i))
        r = (s * 10) % 11

        if r == 10:
            r = 0

        if r != d[i]:
            return False

    return True


@app.post("/validar-cpf")
def validar_cpf():
    dados = request.get_json(silent=True)

    if not isinstance(dados, dict) or not isinstance(dados.get("cpf"), str):
        return {"erro": "Envie o campo 'cpf' como texto em um JSON."}, 400

    return {"valido": cpf_ok(dados["cpf"])}