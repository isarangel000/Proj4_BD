# 🕷 𝙲𝚘𝚏𝚛𝚎 𝚍𝚎 𝙳𝚘𝚌𝚎𝚜 𝙲𝚛𝚒𝚙𝚝𝚘𝚐𝚛𝚊𝚏𝚊𝚍𝚘 🦇

Aplicação em Python para armazenar doces coletados no Halloween utilizando **MongoDB** e **criptografia Fernet (AES Simétrico)**.  
O tipo de doce é salvo criptografado no banco e só pode ser lido com a chave secreta.

---

## ⤿ 𝚃𝚎𝚌𝚗𝚘𝚕𝚘𝚐𝚒𝚊𝚜
- Python  
- CustomTkinter (Interface Dark)  
- MongoDB + pymongo (Banco NoSQL)  
- cryptography.fernet (Criptografia Simétrica)

---

## ⤿ 𝙵𝚞𝚗𝚌𝚒𝚘𝚗𝚊𝚕𝚒𝚍𝚊𝚍𝚎𝚜
- Cadastrar doces (criptografando antes de salvar)  
- Listar doces (descriptografando automaticamente)  
- Excluir registros  
- Interface estilosa e intuitiva 🎃

---

## ⤿ 𝙴𝚜𝚝𝚛𝚞𝚝𝚞𝚛𝚊 𝚍𝚘 𝙳𝚘𝚌𝚞𝚖𝚎𝚗𝚝𝚘 (MongoDB)
```json
{
  "child": "Nome",
  "candy_type": "<criptografado>",
  "qty": 5,
  "timestamp": "data/hora"
}
