CREATE TABLE IF NOT EXISTS pessoas (
  identificacao INTEGER,
  client_id INTEGER NOT NULL,
  data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP,
  data_atualizacao DATETIME,
  url_imagem TEXT NOT NULL,
  face_encoding BLOB,

  PRIMARY KEY (identificacao, client_id)
);

CREATE TABLE IF NOT EXISTS sistema_externo (
  client_id INTEGER PRIMARY KEY,
  nome TEXT NOT NULL,
  data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
);