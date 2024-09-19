class Funcionario {
    constructor(nome, idade, cargo) {
        this.nome = nome;
        this.idade = idade;
        this.cargo = cargo;
    }

    seApresentar() {
        return `Olá, meu nome é ${this.nome}, tenho ${this.idade} anos e sou ${this.cargo}.`;
    }

    trabalhar() {
        return `${this.nome} está trabalhando.`;
    }
}

class Gerente extends Funcionario {
    constructor(nome, idade, cargo, departamento) {
        super(nome, idade, cargo);
        this.departamento = departamento;
    }

    gerenciar() {
        return `${this.nome} está gerenciando o departamento de ${this.departamento}.`;
    }
}

class Desenvolvedor extends Funcionario {
    constructor(nome, idade, cargo, linguagem) {
        super(nome, idade, cargo);
        this.linguagem = linguagem;
    }

    programar() {
        return `${this.nome} está programando em ${this.linguagem}.`;
        console.log("");
    }
}

// Função erros
function exibirErro(mensagem) {
    const erroDiv = document.getElementById('erro');
    erroDiv.innerText = mensagem;
    erroDiv.style.color = 'red';
}

// Função para criar os funcionários
function criarFuncionarios() {
    try {
        const nomeGerente = document.getElementById('nomeGerente').value;
        const idadeGerente = parseInt(document.getElementById('idadeGerente').value);
        const cargoGerente = document.getElementById('cargoGerente').value;
        const departamento = document.getElementById('departamento').value;

        const nomeDev = document.getElementById('nomeDev').value;
        const idadeDev = parseInt(document.getElementById('idadeDev').value);
        const cargoDev = document.getElementById('cargoDev').value;
        const linguagem = document.getElementById('linguagem').value;

        // Validação
        if (!nomeGerente || isNaN(idadeGerente) || !cargoGerente || !departamento) {
            throw new Error("Todos os campos do gerente devem ser preenchidos corretamente.");
        }

        if (!nomeDev || isNaN(idadeDev) || !cargoDev || !linguagem) {
            throw new Error("Todos os campos do desenvolvedor devem ser preenchidos corretamente.");
        }

        // instâncias
        const gerente = new Gerente(nomeGerente, idadeGerente, cargoGerente, departamento);
        const desenvolvedor = new Desenvolvedor(nomeDev, idadeDev, cargoDev, linguagem);

        // Exibição das informações
        document.getElementById('resultado').innerHTML = `
            <p>${gerente.seApresentar()}</p>
            <p>${gerente.gerenciar()}</p>
            <p>${desenvolvedor.seApresentar()}</p>
            <p>${desenvolvedor.programar()}</p>
        `;
    } catch (error) {
        exibirErro(error.message);
    }
}