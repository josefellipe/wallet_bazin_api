const acoes_tbl = document.getElementById('acoes')
const input_range = document.getElementById('range')
const btn_buscar = document.getElementById('btn_buscar')


btn_buscar.addEventListener('click', async () => {

    acoes_tbl.innerHTML = ''

    const url = 'http://127.0.0.1:5000/consultar';

    let acoes = await fetch(url);
    acoes = await acoes.json();
    let range = input_range.value



    let n = 0
    while (n < range) {
        n += 1

        let acao = acoes[n]
        var empresa = document.createElement('tr');
        var numero = document.createElement('td');
        var ticket = document.createElement('td');
        var nome = document.createElement('td');
        var dy_0 = document.createElement('td');
        var dy_1 = document.createElement('td');
        var dy_2 = document.createElement('td');
        var dy_3 = document.createElement('td');
        var dy_4 = document.createElement('td');
        var btn_1 = document.createElement('td');



        numero.innerHTML = `${n}`;
        ticket.innerHTML = `${acao[1]}`;
        nome.innerHTML = `${acao[2]}`;
        dy_0.innerHTML = `${acao[4]}%`;
        dy_1.innerHTML = `${acao[5]}%`;
        dy_2.innerHTML = `${acao[6]}%`;
        dy_3.innerHTML = `${acao[7]}%`;
        dy_4.innerHTML = `${acao[8]}%`;
        var btns = `<div  class="disp">
                        <button class="btn btn-success" type="button">+</button> 
                        <a href="https://www.fundamentus.com.br/detalhes.php?papel=${acao[1]}" target="_blank">
                            <button class="btn btn-light" type="button">i</button>
                        </a>
                    </div>`;
        btn_1.innerHTML = btns



        empresa.appendChild(numero);
        empresa.appendChild(ticket);
        empresa.appendChild(nome);
        empresa.appendChild(dy_0);
        empresa.appendChild(dy_1);
        empresa.appendChild(dy_2);
        empresa.appendChild(dy_3);
        empresa.appendChild(dy_4);
        empresa.appendChild(btn_1);


        acoes_tbl.appendChild(empresa);
    }
})
