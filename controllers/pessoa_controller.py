from flask import Blueprint, jsonify, request
from exceptions.file_exception import NoFilePartError, NoSelectedFileError
from exceptions.service_exception import ErroLeituraImagemError, PessoaJaCadastradaError, PessoaNaoEncontradaError, RostoNaoEncontradoError
from services.reconhecimento_service import ReconhecimentoService
from helpers.file_helper import FileHelper

pessoa_controller = Blueprint('controller', __name__)

diretorio = 'imagens_cadastradas'
reconhecimento_service= ReconhecimentoService()

@pessoa_controller.route('/', methods=['GET'])
def hello():
    return 'Inicio'

@pessoa_controller.route('/cadastrar', methods=['POST'])
def cadastrar():
    try:
        file = FileHelper.validar_arquivo_requisicao(request)
        client_id = request.form['client_id']
        identificacao = request.form['identificacao']
        
        if not client_id or not identificacao:
            return jsonify({"error": "Campos 'client_id' e 'identificacao' são obrigatórios."}), 422

        imagem = FileHelper.salvar_imagem_repositorio(diretorio, identificacao, file)
        resultado = reconhecimento_service.cadastrar_pessoa_com_reconhecimento(client_id=client_id, identificacao=identificacao, url_imagem=imagem)
        FileHelper.remover_imagem(imagem)
        return jsonify(resultado.__dict__), 200
    except  NoFilePartError as e:
        return jsonify({"error": str(e)}), 422
    except  NoSelectedFileError as e:
        return jsonify({"error": str(e)}), 422
    except RostoNaoEncontradoError as e:
        return jsonify({"error": str(e)}), 422  
    except PessoaJaCadastradaError as e:
        return  jsonify({"error": str(e)}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500
        
@pessoa_controller.route('/atualizar', methods=['PUT'])
def atualizar():
    try:
        file = FileHelper.validar_arquivo_requisicao(request)
        client_id = request.form['client_id']
        identificacao = request.form['identificacao']
        
        if not client_id or not identificacao :
            return jsonify({"error": "Campos 'client_id' e 'identificacao' são obrigatórios."}), 422
        
        imagem = FileHelper.salvar_imagem_repositorio(diretorio, identificacao, file)
        resultado = reconhecimento_service.atualizar_cadastro(client_id=client_id, identificacao=identificacao, url_imagem=imagem)
        FileHelper.remover_imagem(imagem)
        return jsonify(resultado.__dict__), 200
   
    except NoFilePartError as e:
        return jsonify({"error": str(e)}), 422
    except NoSelectedFileError as e:
        return jsonify({"error": str(e)}), 422
    except RostoNaoEncontradoError as e:
        return jsonify({"error": str(e)}), 422
    except PessoaNaoEncontradaError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@pessoa_controller.route('/autenticar', methods=['POST'])
def autenticar():
    try:    
        file = FileHelper.validar_arquivo_requisicao(request)
        client_id = request.form['client_id']
        identificacao = request.form['identificacao']
        
        if not client_id or not identificacao:
            return jsonify({"error": "Campos 'client_id' e 'identificacao' são obrigatórios."}), 422
        
        resultado = reconhecimento_service.autenticar_pessoa(identificacao=identificacao, url_imagem= file, client_id=client_id)
    
        return jsonify(resultado.__dict__), 200
   
    except  NoFilePartError as e:
        return jsonify({"error": str(e)}), 422
    except  NoSelectedFileError as e:
        return jsonify({"error": str(e)}), 422
    except ErroLeituraImagemError as e:
        return jsonify({"error": str(e)}), 500
    except PessoaNaoEncontradaError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

        
