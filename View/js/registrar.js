const btn = document.getElementById('btn_repeat');
const nome = document.getElementById('nome');
const user_name = document.getElementById('user_name');
const senha = document.getElementById('senha');
const senha_repeat = document.getElementById('senha_repeat');

btn.addEventListener('click', async() => {

    url = 'http://127.0.0.1:5000/registrar_novo_investidor';

    user_data = {
        nome: String(nome.value),
        user_name:  String(user_name.value),
        senha:  String(senha.value)
    };

    fetchData = {
        method: 'POST',
        body: JSON.stringify(user_data),
        headers: { 'Content-Type' : 'application/json' }
    };

    if (senha.value == senha_repeat.value){
        let response = await fetch(url, fetchData)
        response = await response.json()

        if (response.mensagem == 'Usuário criado com sucesso'){
            alert(response.mensagem)
        }
        else if (response.mensagem == 'Usuário não foi criado'){
            alert(response.mensagem)
        }
    } else {
        alert('As senhas não são iguais')
        document.getElementById('senha').value = ''
        document.getElementById('senha_repeat').value = ''
    }

})