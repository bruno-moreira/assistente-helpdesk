
import unittest
from assistente_virtual import *

CHAMANDO_OK = "audio_chamado/atender-chamado.wav"
CHAMANDO_JARVIS = "audio_chamado/assistente-diferente.wav"
CHAMANDO_ATENDER = "audio_chamado/atender-chamado.wav"
CHAMANDO_AGUARDAR = "audio_chamado/aguardando-chamado.wav"
CHAMANDO_ESPERAR = "audio_chamado/em-espera-chamado.wav"
CHAMANDO_FINALIZAR = "audio_chamado/finalizar-chamado.wav"
CHAMANDO_PARECER = "audio_chamado/parecer-do-chamado.wav"

class TesteNomeAssistente(unittest.TestCase):

    def setUp(self):
        self.iniciado, self.reconhecedor, self.palavras_de_parada, self.nome_do_assistente, self.acoes = iniciar()

    def testar_01_reconhecer_nome(self):
        tem_transcricao, transcricao = transcrever_arquivo_de_audio(self.reconhecedor,CHAMANDO_OK)

        self.assertTrue(tem_transcricao) # usar essas funções de assert para fazer os testes, NÃO usar if, usar as opções de teste mesmo. 

        tokens = obter_tokens(transcricao)
        self.assertIsNotNone(tokens)
        self.assertEqual(tokens[0], self.nome_do_assistente)

    def testar_02_nao_reconhecer_outro_nome(self):
        tem_transcricao, transcricao = transcrever_arquivo_de_audio(self.reconhecedor,CHAMANDO_JARVIS)

        self.assertTrue(tem_transcricao) 
        tokens = obter_tokens(transcricao)
        self.assertIsNotNone(tokens)
        self.assertNotEqual(tokens[0], self.nome_do_assistente)
    
    def testar_03_atender_chamado(self):
        tem_transcricao, transcricao = transcrever_arquivo_de_audio(self.reconhecedor,CHAMANDO_ATENDER)

        self.assertTrue(tem_transcricao) 

        tokens = obter_tokens(transcricao)
        
        self.assertEqual(tokens[0], self.nome_do_assistente)
        self.assertEqual(tokens[1], self.acoes[0]['nome'])
        self.assertEqual(tokens[2], self.acoes[0]['objetos'][0])
    
    def testar_04_chamado_em_espera(self):
        tem_transcricao, transcricao = transcrever_arquivo_de_audio(self.reconhecedor,CHAMANDO_ESPERAR)

        self.assertTrue(tem_transcricao) 

        tokens = obter_tokens(transcricao)
        
        self.assertEqual(tokens[0], self.nome_do_assistente)
        self.assertEqual(tokens[1], self.acoes[1]['nome'])
        self.assertEqual(tokens[2], self.acoes[1]['objetos'][0])
    
    def testar_05_chamado_aguardando_peça(self):
        tem_transcricao, transcricao = transcrever_arquivo_de_audio(self.reconhecedor,CHAMANDO_AGUARDAR)

        self.assertTrue(tem_transcricao) 

        tokens = obter_tokens(transcricao)
        
        self.assertEqual(tokens[0], self.nome_do_assistente)
        self.assertEqual(tokens[1], self.acoes[2]['nome'])
        self.assertEqual(tokens[2], self.acoes[2]['objetos'][0])
         
    def testar_06_finalizar_chamado(self):
        tem_transcricao, transcricao = transcrever_arquivo_de_audio(self.reconhecedor,CHAMANDO_FINALIZAR)

        self.assertTrue(tem_transcricao) 

        tokens = obter_tokens(transcricao)
        
        self.assertEqual(tokens[0], self.nome_do_assistente)
        self.assertEqual(tokens[1], self.acoes[3]['nome'])
        self.assertEqual(tokens[2], self.acoes[3]['objetos'][0])
    
    def testar_07_parecer_tecnico_chamado(self):
        tem_transcricao, transcricao = transcrever_arquivo_de_audio(self.reconhecedor,CHAMANDO_PARECER)

        self.assertTrue(tem_transcricao) 

        tokens = obter_tokens(transcricao)
        self.assertIsNotNone(tokens)
        self.assertEqual(tokens[0], self.nome_do_assistente)
        self.assertEqual(tokens[1], self.acoes[4]['nome'])
        self.assertEqual(tokens[2], self.acoes[4]['objetos'][0])
    
        

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteNomeAssistente))

    executador = unittest.TextTestRunner()
    executador.run(testes)
