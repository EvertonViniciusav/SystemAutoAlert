document.addEventListener("DOMContentLoaded", function () {
    fetch('/api/usuarios')
        .then(response => {
            if (!response.ok) {
                throw new Error(`Erro na API: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            const tabelaUsuarios = document.getElementById('usuariosCadastrados');

            tabelaUsuarios.innerHTML = '';

            data.forEach(usuario => {
                const linha = document.createElement('tr');
                linha.innerHTML = `
                    <td>${usuario.id}</td>
                    <td>${usuario.nome}</td>
                    <td>${usuario.ativo ? 'Sim' : 'Não'}</td>
                    <td>${usuario.criado_at}</td>
                    <td>${usuario.alterado_at || 'Não alterado'}</td>
                `;
                tabelaUsuarios.appendChild(linha);
            });
        })
        .catch(error => {
            console.error('Erro ao carregar usuários:', error);
        });
});


