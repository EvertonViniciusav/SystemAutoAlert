CREATE TABLE empresas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    documento VARCHAR(18) NOT NULL,  -- CPF ou CNPJ
    tipo_documento ENUM('CPF', 'CNPJ') NOT NULL,  -- Para diferenciar
    razao_social VARCHAR(255) NOT NULL,
    cep VARCHAR(10),
    rua VARCHAR(255),
    numero VARCHAR(20),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    estado VARCHAR(2),
    pais VARCHAR(100),
    numero_contato VARCHAR(20),
    numero_notificacao VARCHAR(20),
    email VARCHAR(255),
    observacao TEXT,
    criacao_empresa DATETIME DEFAULT CURRENT_TIMESTAMP,
    alteracao_empresa DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
