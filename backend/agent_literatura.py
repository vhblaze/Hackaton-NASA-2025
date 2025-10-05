#!/usr/bin/env python3
"""
Agent Especialista em Literatura (Research Analyst)
Mineração de textos científicos
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from typing import Dict, Any, List, Optional
import os
import json

class AgentLiteratura:
    """
    Agent Especialista em Literatura - Mineração de textos científicos
    
    Responsabilidades:
    - Análise de abstracts, conclusões, resultados
    - Identificação de lacunas de conhecimento
    - Mapeamento de consenso/desacordo científico
    - Extração de hipóteses e conclusões
    """
    
    def __init__(self):
        self.github_csv_url = "https://raw.githubusercontent.com/jgalazka/SB_publications/main/SB_publication_PMC.csv"
        self.nslsl_search_url = "https://extapps.ksc.nasa.gov/NSLSL/Search#"
        self.publications_df = self._load_github_publications()

    def _load_github_publications(self) -> pd.DataFrame:
        """
        Carrega o CSV de publicações do GitHub.
        """
        try:
            df = pd.read_csv(self.github_csv_url)
            print("CSV de publicações do GitHub carregado com sucesso.")
            return df
        except Exception as e:
            print(f"Erro ao carregar CSV do GitHub: {e}")
            return pd.DataFrame(columns=["Title", "Link"])

    def buscar_nslsl_simulado(self, termo_busca: str) -> List[Dict[str, str]]:
        """
        Simula a busca na NSLSL. Em um ambiente real, isso envolveria web scraping ou API.
        Aqui, retornamos resultados baseados em palavras-chave.
        """
        print(f"Simulando busca na NSLSL para: {termo_busca}")
        resultados_simulados = []
        termo_lower = termo_busca.lower()

        # Simular resultados relevantes
        if "marte" in termo_lower or "marciana" in termo_lower:
            resultados_simulados.append({
                "titulo": "Exploração de Marte: Desafios e Oportunidades",
                "link": "https://example.com/marte_exploracao",
                "abstract": "Este artigo discute os principais desafios e oportunidades na exploração humana e robótica de Marte, incluindo radiação e recursos. Conclui-se que a colaboração internacional é crucial. Hipótese: Novas tecnologias de propulsão reduzirão o tempo de viagem."
            })
        if "microgravidade" in termo_lower:
            resultados_simulados.append({
                "titulo": "Efeitos da Microgravidade em Sistemas Biológicos",
                "link": "https://example.com/microgravidade_biologia",
                "abstract": "Uma revisão abrangente sobre como a microgravidade afeta a fisiologia humana e de outros organismos em missões espaciais. Conclui-se que a perda óssea é um problema significativo. Hipótese: Exercícios contínuos podem mitigar os efeitos."
            })
        if "radiação" in termo_lower:
            resultados_simulados.append({
                "titulo": "Proteção contra Radiação em Viagens Espaciais",
                "link": "https://example.com/radiacao_espacial",
                "abstract": "Estratégias e tecnologias para mitigar os riscos da radiação cósmica em missões de longa duração. Conclui-se que blindagens ativas são promissoras. Hipótese: Materiais leves podem oferecer proteção adequada."
            })
        if "biologia espacial" in termo_lower or "life sciences" in termo_lower:
            resultados_simulados.append({
                "titulo": "Avanços em Biologia Espacial",
                "link": "https://example.com/biologia_espacial",
                "abstract": "Recentes descobertas e direções futuras na pesquisa de biologia espacial. Conclui-se que a pesquisa em genômica é fundamental. Hipótese: Organismos extremófilos podem sobreviver em Marte."
            })
        
        # Filtrar publicações do GitHub que contenham o termo de busca no título
        if not self.publications_df.empty:
            github_matches = self.publications_df[self.publications_df["Title"].str.lower().str.contains(termo_lower, na=False)]
            for index, row in github_matches.iterrows():
                # Adicionar um abstract simulado para as publicações do GitHub
                simulated_abstract = "Abstract simulado para a publicação: {}. Este artigo aborda aspectos de biologia espacial e seus impactos. Conclui-se que mais estudos são necessários. Hipótese: Dados de microgravidade são cruciais.".format(row["Title"])
                resultados_simulados.append({
                    "titulo": row["Title"],
                    "link": row["Link"],
                    "abstract": simulated_abstract
                })

        return resultados_simulados

    def analisar_literatura(self, resultados_busca: List[Dict[str, str]]) -> Dict[str, Any]:
        """
        Analisa os resultados da busca, extraindo informações chave.
        """
        print("Analisando literatura...")
        analise = {
            "total_artigos_encontrados": len(resultados_busca),
            "temas_principais": {},
            "lacunas_potenciais": [],
            "conclusoes_extraidas": [],
            "hipoteses_mencionadas": []
        }

        for artigo in resultados_busca:
            abstract = artigo.get("abstract", "").lower()
            titulo = artigo.get("titulo", "").lower()

            # Identificar temas principais (exemplo simples)
            if "marte" in abstract or "marte" in titulo:
                analise["temas_principais"]["exploracao_marte"] = analise["temas_principais"].get("exploracao_marte", 0) + 1
            if "microgravidade" in abstract or "microgravidade" in titulo:
                analise["temas_principais"]["microgravidade"] = analise["temas_principais"].get("microgravidade", 0) + 1
            if "radiação" in abstract or "radiação" in titulo:
                analise["temas_principais"]["radiacao_espacial"] = analise["temas_principais"].get("radiacao_espacial", 0) + 1
            if "biologia" in abstract or "biologia" in titulo or "life sciences" in abstract or "life sciences" in titulo:
                analise["temas_principais"]["biologia_espacial"] = analise["temas_principais"].get("biologia_espacial", 0) + 1

            # Extrair conclusões e hipóteses (simulado com regex)
            conclusoes = re.findall(r"conclui-se que([^.]+)", abstract)
            for conc in conclusoes:
                analise["conclusoes_extraidas"].append("Em '{}': {}. ".format(artigo['titulo'], conc.strip().capitalize()))
            
            hipoteses = re.findall(r"hipótese:([^.]+)", abstract)
            for hip in hipoteses:
                analise["hipoteses_mencionadas"].append("Em '{}': {}. ".format(artigo['titulo'], hip.strip().capitalize()))

        # Identificar lacunas potenciais (simulado)
        if not analise["temas_principais"].get("microgravidade"):
            analise["lacunas_potenciais"].append("Mais pesquisa necessária sobre os efeitos da microgravidade em longo prazo.")
        if not analise["temas_principais"].get("radiacao_espacial"):
            analise["lacunas_potenciais"].append("Faltam estudos sobre novas formas de proteção contra radiação.")
        if not analise["temas_principais"].get("exploracao_marte"):
            analise["lacunas_potenciais"].append("Aprofundar estudos sobre a viabilidade de habitats em Marte.")

        print("Análise de literatura concluída.")
        return analise

    def processar_consulta_literatura(self, consulta_texto: str) -> Dict[str, Any]:
        """
        Processa uma consulta relacionada à literatura científica.
        
        Args:
            consulta_texto: A consulta do usuário.
            
        Returns:
            Dicionário com os resultados da análise da literatura.
        """
        print(f"Processando consulta de literatura: {consulta_texto}")
        
        # 1. Buscar na NSLSL (simulado) e no GitHub
        resultados_busca = self.buscar_nslsl_simulado(consulta_texto)
        
        # 2. Analisar os resultados
        analise_literatura = self.analisar_literatura(resultados_busca)
        
        return {
            "status": "sucesso",
            "consulta_original": consulta_texto,
            "resultados_busca": resultados_busca,
            "analise_literatura": analise_literatura,
            "mensagem": "Análise de literatura concluída com sucesso."
        }

# Exemplo de uso (para teste local)
if __name__ == "__main__":
    agent_literatura = AgentLiteratura()
    
    print("\n--- Testando com consulta sobre microgravidade ---")
    consulta_teste_micro = "Quais são os principais artigos sobre microgravidade?"
    resultado_micro = agent_literatura.processar_consulta_literatura(consulta_teste_micro)
    print(json.dumps(resultado_micro, indent=2))

    print("\n--- Testando com consulta sobre exploração de Marte ---")
    consulta_teste_marte = "Artigos recentes sobre exploração de Marte e radiação"
    resultado_marte = agent_literatura.processar_consulta_literatura(consulta_teste_marte)
    print(json.dumps(resultado_marte, indent=2))

    print("\n--- Testando com consulta genérica ---")
    consulta_teste_generica = "Me fale sobre biologia espacial"
    resultado_generica = agent_literatura.processar_consulta_literatura(consulta_teste_generica)
    print(json.dumps(resultado_generica, indent=2))

