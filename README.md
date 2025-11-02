
````markdown
# 🕷 𝙲𝚘𝚏𝚛𝚎 𝚍𝚎 𝙳𝚘𝚌𝚎𝚜 𝙲𝚛𝚒𝚙𝚝𝚘𝚐𝚛𝚊𝚏𝚊𝚍𝚘 🦇

Aplicação em Python para armazenar doces coletados no Halloween usando **MongoDB** e **criptografia Fernet (AES simétrico)**.  
O tipo de doce é salvo criptografado no banco e só pode ser lido com a chave correta.

## ⤿ 𝚃𝚎𝚌𝚗𝚘𝚕𝚘𝚐𝚒𝚊𝚜
- Python
- CustomTkinter (interface)
- MongoDB + pymongo (banco de dados)
- cryptography.fernet (criptografia)

## ⤿ 𝙵𝚞𝚗𝚌𝚒𝚘𝚗𝚊𝚕𝚒𝚍𝚊𝚍𝚎𝚜
- Cadastrar doce (dados são criptografados antes de salvar)
- Listar doces (descriptografando automaticamente)
- Excluir registro
- Interface dark estilosa

## ⤿ 𝙴𝚜𝚝𝚛𝚞𝚝𝚞𝚛𝚊 𝚍𝚘𝚜 𝚍𝚊𝚍𝚘𝚜
```json
{
  "child": "Nome",
  "candy_type": "<criptografado>",
  "qty": 5,
  "timestamp": "data/hora"
}
````

##  𝙲𝚘𝚖𝚘 𝚎𝚡𝚎𝚌𝚞𝚝𝚊𝚛

```bash
pip install customtkinter pymongo cryptography
python nome_do_arquivo.py
```

```

