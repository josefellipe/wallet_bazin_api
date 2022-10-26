const btn = document.getElementById('btn_login')
    const name = document.getElementById('user_name')
    const senha = document.getElementById('senha')

    btn.addEventListener('click', async() => {

        const url = 'http://127.0.0.1:5000/login';

        let data_json = {
            login: String(name.value),
            senha: String(senha.value)
        };

        let fetchData = {
            method:'POST',
            body: JSON.stringify(data_json),
            headers: { 'Content-Type': 'application/json' }
        }

        let investidor = await fetch(url, fetchData)
        investidor = await investidor.json()

        console.log(investidor)

    })