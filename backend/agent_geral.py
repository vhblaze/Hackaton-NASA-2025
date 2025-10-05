#!/usr/bin/env python3
"""
Agent Geral (Search Master)
Coordenador e interface principal do sistema multi-agente
"""

import json
import re
import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum

# Importar os agentes especializados
from agent_csv import AgentCSV, NumpyEncoder
from agent_literatura import AgentLiteratura
from agent_missoes import AgentMissoes

class AgentType(Enum):
    CSV = "csv"
    LITERATURA = "literatura"
    MISSOES = "missoes"

@dataclass
class ConsultaUsuario:
    """Representa uma consulta do usuário"""
    texto: str
    timestamp: str
    id_consulta: str

@dataclass
class ResultadoAgente:
    """
    Representa o resultado de um agente especializado
    O campo 'dados' pode conter um dicionário com os resultados da análise,
    incluindo caminhos para visualizações geradas.
    """
    agente_tipo: AgentType
    dados: Dict[str, Any]
    sucesso: bool
    mensagem: str

class AgentGeral:
    """
    Agent Geral - Coordenador principal do sistema multi-agente
    
    Responsabilidades:
    - Receber consultas do usuário em linguagem natural
    - Rotear para os agentes especializados
    - Combinar e sintetizar resultados
    - Interface de painel dinâmico
    """
    
    def __init__(self):
        self.historico_consultas: List[ConsultaUsuario] = []
        self.agentes_disponiveis = {
            AgentType.CSV: "Agent Especialista em CSV (Data Analyst)",
            AgentType.LITERATURA: "Agent Especialista em Literatura (Research Analyst)",
            AgentType.MISSOES: "Agent Especialista em Missões (Mission Planner)"
        }
        # Instanciar agentes especializados
        self.agent_csv = AgentCSV()
        self.agent_literatura = AgentLiteratura()
        self.agent_missoes = AgentMissoes()
        
    def analisar_intencao(self, consulta: str) -> List[AgentType]:
        """
        Analisa a intenção do usuário e determina quais agentes devem ser acionados
        
        Args:
            consulta: Texto da consulta do usuário
            
        Returns:
            Lista de tipos de agentes que devem processar a consulta
        """
        consulta_lower = consulta.lower()
        agentes_necessarios = []
        
        # Palavras-chave para Agent CSV (Data Analyst)
        palavras_csv = [
            'dados', 'csv', 'estatística', 'análise', 'gráfico', 'tabela',
            'tendência', 'padrão', 'números', 'dataset', 'planilha',
            'visualização', 'correlação', 'média', 'distribuição'
        ]
        
        # Palavras-chave para Agent Literatura (Research Analyst)
        palavras_literatura = [
            'artigo', 'pesquisa', 'literatura', 'paper', 'estudo',
            'publicação', 'abstract', 'conclusão', 'hipótese',
            'consenso', 'lacuna', 'conhecimento', 'científico',
            'revista', 'autor', 'citação'
        ]
        
        # Palavras-chave para Agent Missões (Mission Planner)
        palavras_missoes = [
            'missão', 'planejamento', 'risco', 'oportunidade',
            'investimento', 'tecnologia', 'lunar', 'marciano',
            'espacial', 'nasa', 'exploração', 'foguete',
            'satélite', 'astronauta', 'rover'
        ]
        
        # Verificar presença de palavras-chave
        if any(palavra in consulta_lower for palavra in palavras_csv):
            agentes_necessarios.append(AgentType.CSV)
            
        if any(palavra in consulta_lower for palavra in palavras_literatura):
            agentes_necessarios.append(AgentType.LITERATURA)
            
        if any(palavra in consulta_lower for palavra in palavras_missoes):
            agentes_necessarios.append(AgentType.MISSOES)
        
        # Se nenhum agente específico foi identificado, usar todos
        if not agentes_necessarios:
            agentes_necessarios = list(AgentType)
            
        return agentes_necessarios
    
    def rotear_consulta(self, consulta: ConsultaUsuario) -> Dict[AgentType, str]:
        """
        Roteia a consulta para os agentes apropriados
        
        Args:
            consulta: Objeto ConsultaUsuario
            
        Returns:
            Dicionário mapeando tipos de agentes para suas consultas específicas
        """
        agentes_necessarios = self.analisar_intencao(consulta.texto)
        roteamento = {}
        
        for agente_tipo in agentes_necessarios:
            # Adaptar a consulta para cada agente específico
            consulta_adaptada = self._adaptar_consulta_para_agente(
                consulta.texto, agente_tipo
            )
            roteamento[agente_tipo] = consulta_adaptada
            
        return roteamento
    
    def _adaptar_consulta_para_agente(self, consulta: str, agente_tipo: AgentType) -> str:
        """
        Adapta a consulta original para o contexto específico de cada agente
        
        Args:
            consulta: Consulta original do usuário
            agente_tipo: Tipo do agente que receberá a consulta
            
        Returns:
            Consulta adaptada para o agente específico
        """
        prefixos = {
            AgentType.CSV: "Analise os dados CSV relacionados a: ",
            AgentType.LITERATURA: "Busque na literatura científica informações sobre: ",
            AgentType.MISSOES: "Forneça insights de planejamento de missões para: "
        }
        
        return prefixos[agente_tipo] + consulta
    
    def sintetizar_resultados(self, resultados: List[ResultadoAgente]) -> Dict[str, Any]:
        """
        Combina e sintetiza os resultados dos agentes especializados
        
        Args:
            resultados: Lista de resultados dos agentes
            
        Returns:
            Resultado sintetizado e formatado
        """
        sintese = {
            "resumo_executivo": "",
            "resultados_por_agente": {},
            "insights_combinados": [],
            "recomendacoes": [],
            "dados_suporte": {}
        }
        
        # Processar resultados de cada agente
        for resultado in resultados:
            if resultado.sucesso:
                sintese["resultados_por_agente"][resultado.agente_tipo.value] = {
                    "dados": resultado.dados,
                    "status": "sucesso"
                }
            else:
                sintese["resultados_por_agente"][resultado.agente_tipo.value] = {
                    "erro": resultado.mensagem,
                    "status": "erro"
                }
        
        # Gerar insights combinados
        sintese["insights_combinados"] = self._gerar_insights_combinados(resultados)
        
        # Gerar recomendações
        sintese["recomendacoes"] = self._gerar_recomendacoes(resultados)
        
        # Criar resumo executivo
        sintese["resumo_executivo"] = self._criar_resumo_executivo(resultados)
        
        return sintese
    
    def _gerar_insights_combinados(self, resultados: List[ResultadoAgente]) -> List[str]:
        """
        Gera insights combinando informações de múltiplos agentes.
        Esta é uma simulação e deve ser aprimorada com lógica real de combinação.
        """
        insights = []
        
        # Lógica para combinar insights (simulada)
        agentes_com_sucesso = [r for r in resultados if r.sucesso]
        
        if any(r.agente_tipo == AgentType.CSV for r in agentes_com_sucesso):
            insights.append("Padrões e tendências identificados em dados estruturados.")
        if any(r.agente_tipo == AgentType.LITERATURA for r in agentes_com_sucesso):
            insights.append("Lacunas de conhecimento e consenso científico mapeados.")
        if any(r.agente_tipo == AgentType.MISSOES for r in agentes_com_sucesso):
            insights.append("Oportunidades e riscos para missões espaciais avaliados.")

        if len(agentes_com_sucesso) > 1:
            insights.append("Análise multi-dimensional realizada com sucesso.")
            insights.append("Correlações potenciais entre diferentes tipos de dados observadas.")
        
        return insights
    
    def _gerar_recomendacoes(self, resultados: List[ResultadoAgente]) -> List[str]:
        """
        Gera recomendações baseadas nos resultados combinados.
        Esta é uma simulação e deve ser aprimorada com lógica real de recomendação.
        """
        recomendacoes = []
        
        for resultado in resultados:
            if resultado.sucesso:
                if resultado.agente_tipo == AgentType.MISSOES:
                    recomendacoes.append("Considerar investimento em tecnologias promissoras para exploração espacial.")
                elif resultado.agente_tipo == AgentType.CSV:
                    recomendacoes.append("Aprofundar análise nos padrões identificados nos datasets da NASA.")
                elif resultado.agente_tipo == AgentType.LITERATURA:
                    recomendacoes.append("Explorar as lacunas de conhecimento identificadas na literatura científica.")
        
        if not recomendacoes and any(r.sucesso for r in resultados):
            recomendacoes.append("Nenhuma recomendação específica gerada, mas os dados estão disponíveis para análise mais aprofundada.")
        elif not recomendacoes:
            recomendacoes.append("Não foi possível gerar recomendações devido à falta de resultados dos agentes.")

        return recomendacoes
    
    def _criar_resumo_executivo(self, resultados: List[ResultadoAgente]) -> str:
        """
        Cria um resumo executivo dos resultados.
        """
        agentes_executados = len(resultados)
        agentes_sucesso = len([r for r in resultados if r.sucesso])
        
        resumo = f"Análise executada por {agentes_executados} agentes especializados. "
        resumo += f"{agentes_sucesso} agentes retornaram resultados com sucesso. "
        
        if agentes_sucesso == agentes_executados:
            resumo += "Análise completa realizada com êxito."
        elif agentes_sucesso > 0:
            resumo += "Análise parcial realizada com alguns resultados disponíveis."
        else:
            resumo += "Análise não pôde ser completada devido a erros nos agentes."
            
        return resumo
    
    def gerar_painel_dinamico(self, sintese: Dict[str, Any]) -> str:
        """
        Gera uma interface de painel dinâmico em formato HTML/Markdown.
        
        Args:
            sintese: Resultado sintetizado dos agentes
            
        Returns:
            HTML/Markdown formatado para exibição
        """
        painel = f'''
# 🚀 Painel de Análise Multi-Agente - NASA

## 📊 Resumo Executivo
{sintese["resumo_executivo"]}

## 🤖 Status dos Agentes

'''
        
        for agente, resultado in sintese["resultados_por_agente"].items():
            status_icon = "✅" if resultado["status"] == "sucesso" else "❌"
            painel += f"- **{agente.upper()}** {status_icon}\n"
            if "visualizacoes" in resultado["dados"] and resultado["dados"]["visualizacoes"]:
                painel += "  Visualizações geradas:\n"
                for viz_path in resultado["dados"]["visualizacoes"]:
                    painel += f"  - ![]({viz_path})\n"
            
            # Adicionar detalhes da análise de literatura, se disponível
            if agente == AgentType.LITERATURA.value and "analise_literatura" in resultado["dados"]:
                lit_analise = resultado["dados"]["analise_literatura"]
                painel += "  Análise de Literatura:\n"
                if lit_analise.get("temas_principais"):
                    painel += "    Temas Principais:\n"
                    for tema, count in lit_analise["temas_principais"].items():
                        painel += "      - {} ({} artigos)\n".format(tema.replace("_", " ").title(), count)
                if lit_analise.get("lacunas_potenciais"):
                    painel += "    Lacunas Potenciais:\n"
                    for lacuna in lit_analise["lacunas_potenciais"]:
                        painel += f"      - {lacuna}\n"
                if lit_analise.get("conclusoes_extraidas"):
                    painel += "    Conclusões Extraídas:\n"
                    for conc in lit_analise["conclusoes_extraidas"]:
                        painel += f"      - {conc}\n"
                if lit_analise.get("hipoteses_mencionadas"):
                    painel += "    Hipóteses Mencionadas:\n"
                    for hip in lit_analise["hipoteses_mencionadas"]:
                        painel += f"      - {hip}\n"
            
            # Adicionar detalhes da análise de missões, se disponível
            if agente == AgentType.MISSOES.value and "analise_riscos_oportunidades" in resultado["dados"]:
                missoes_analise = resultado["dados"]
                painel += "  Análise de Missões:\n"
                painel += "    Riscos:\n"
                for risco in missoes_analise["analise_riscos_oportunidades"]["riscos"]:
                    painel += f"      - {risco}\n"
                painel += "    Oportunidades:\n"
                for oportunidade in missoes_analise["analise_riscos_oportunidades"]["oportunidades"]:
                    painel += f"      - {oportunidade}\n"
                painel += "    Recomendações de Investimento:\n"
                for rec in missoes_analise["recomendacoes_investimento"]:
                    painel += f"      - {rec}\n"
                painel += "    Tecnologias Promissoras:\n"
                for tech in missoes_analise["tecnologias_promissoras"]:
                    painel += f"      - {tech}\n"
                painel += "    Plano de Missão (Fases):\n"
                for fase in missoes_analise["plano_missao"]["fases"]:
                    painel += f"      - {fase}\n"
                painel += "    Plano de Missão (Objetivos):\n"
                for obj in missoes_analise["plano_missao"]["objetivos"]:
                    painel += f"      - {obj}\n"
                painel += "    Plano de Missão (Recursos Necessários):\n"
                for rec_nec in missoes_analise["plano_missao"]["recursos_necessarios"]:
                    painel += f"      - {rec_nec}\n"

        painel += f'''

## 💡 Insights Combinados
'''
        
        for insight in sintese["insights_combinados"]:
            painel += f"- {insight}\n"
        
        painel += f'''

## 🎯 Recomendações
'''
        
        for recomendacao in sintese["recomendacoes"]:
            painel += f"- {recomendacao}\n"
        
        return painel
    
    def processar_consulta(self, texto_consulta: str) -> str:
        """
        Método principal para processar uma consulta do usuário
        
        Args:
            texto_consulta: Texto da consulta do usuário
            
        Returns:
            Resultado formatado da análise
        """
        
        # Criar objeto de consulta
        consulta = ConsultaUsuario(
            texto=texto_consulta,
            timestamp=datetime.datetime.now().isoformat(),
            id_consulta=f"consulta_{len(self.historico_consultas) + 1}"
        )
        
        # Adicionar ao histórico
        self.historico_consultas.append(consulta)
        
        # Rotear consulta
        roteamento = self.rotear_consulta(consulta)
        
        resultados_agentes = []
        github_csv_url = "https://raw.githubusercontent.com/jgalazka/SB_publications/main/SB_publication_PMC.csv"

        for agente_tipo, consulta_adaptada in roteamento.items():
            if agente_tipo == AgentType.CSV:
                print(f"Agent Geral: Acionando Agent CSV com consulta: {consulta_adaptada}")
                try:
                    # Para o Agent CSV, usaremos o CSV do GitHub como exemplo
                    csv_result = self.agent_csv.processar_consulta_csv(
                        consulta_texto=consulta_adaptada,
                        csv_url=github_csv_url
                    )
                    resultados_agentes.append(ResultadoAgente(
                        agente_tipo=AgentType.CSV,
                        dados=csv_result,
                        sucesso=True,
                        mensagem="Análise CSV concluída."
                    ))
                except Exception as e:
                    resultados_agentes.append(ResultadoAgente(
                        agente_tipo=AgentType.CSV,
                        dados={},
                        sucesso=False,
                        mensagem=f"Erro ao executar Agent CSV: {e}"
                    ))
            elif agente_tipo == AgentType.LITERATURA:
                print(f"Agent Geral: Acionando Agent Literatura com consulta: {consulta_adaptada}")
                try:
                    lit_result = self.agent_literatura.processar_consulta_literatura(consulta_adaptada)
                    resultados_agentes.append(ResultadoAgente(
                        agente_tipo=AgentType.LITERATURA,
                        dados=lit_result,
                        sucesso=True,
                        mensagem="Pesquisa de literatura concluída."
                    ))
                except Exception as e:
                    resultados_agentes.append(ResultadoAgente(
                        agente_tipo=AgentType.LITERATURA,
                        dados={},
                        sucesso=False,
                        mensagem=f"Erro ao executar Agent Literatura: {e}"
                    ))
            elif agente_tipo == AgentType.MISSOES:
                print(f"Agent Geral: Acionando Agent Missões com consulta: {consulta_adaptada}")
                try:
                    missoes_result = self.agent_missoes.processar_consulta_missoes(consulta_adaptada)
                    resultados_agentes.append(ResultadoAgente(
                        agente_tipo=AgentType.MISSOES,
                        dados=missoes_result,
                        sucesso=True,
                        mensagem="Planejamento de missões concluído."
                    ))
                except Exception as e:
                    resultados_agentes.append(ResultadoAgente(
                        agente_tipo=AgentType.MISSOES,
                        dados={},
                        sucesso=False,
                        mensagem=f"Erro ao executar Agent Missões: {e}"
                    ))
        
        # Sintetizar resultados
        sintese = self.sintetizar_resultados(resultados_agentes)
        
        # Gerar painel dinâmico
        painel = self.gerar_painel_dinamico(sintese)
        
        return painel

# Exemplo de uso
if __name__ == "__main__":
    agent = AgentGeral()
    
    # Teste com consulta exemplo
    consulta_teste = "Quero analisar dados de missões da NASA e encontrar artigos sobre exploração de Marte"
    resultado = agent.processar_consulta(consulta_teste)
    print(resultado)

    print("\n--- Teste com consulta apenas CSV ---")
    consulta_csv = "Analise os dados do CSV de publicações"
    resultado_csv = agent.processar_consulta(consulta_csv)
    print(resultado_csv)

    print("\n--- Teste com consulta apenas Literatura ---")
    consulta_lit = "Quais são os principais artigos sobre microgravidade?"
    resultado_lit = agent.processar_consulta(consulta_lit)
    print(resultado_lit)

    print("\n--- Teste com consulta apenas Missões ---")
    consulta_mis = "Quais os riscos de uma missão para Marte?"
    resultado_mis = agent.processar_consulta(consulta_mis)
    print(resultado_mis)

    print("\n--- Teste com consulta genérica ---")
    consulta_generica = "Me dê informações sobre a NASA"
    resultado_generica = agent.processar_consulta(consulta_generica)
    print(resultado_generica)

