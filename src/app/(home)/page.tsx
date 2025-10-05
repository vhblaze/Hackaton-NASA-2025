import Footer from "@/components/LPSComponents/footer";
import Header from "@/components/LPSComponents/header";
import ServiceCard from "@/components/LPSComponents/serviceCard";
import Tabs from "@/components/LPSComponents/tabs";
import Image from "next/image";

export default function Home() {
  const dashboardOne = "/dashBoard";
  return (
    <main className="min-h-screen">
      <Header />

      {/* Hero Section */}
      <section
        id="inicio"
        className="relative h-screen flex items-center justify-center"
        style={{
          backgroundImage: "url('/image21.png')",
          backgroundSize: "cover",
          backgroundPosition: "center",
        }}
      >
        {/* Overlay */}
        <div className="absolute inset-0 bg-black/50"></div>

        {/* Content */}
        <div className="relative z-10 text-center px-6 max-w-4xl">
          <h1 className="text-5xl md:text-6xl lg:text-7xl font-bold text-white mb-6 leading-tight">
            Redefinindo suas
            <br />
            pesquisas com
            <br />
            <span className="text-gray-300">Tecnologias SACY</span>
          </h1>
          <p className="text-gray-300 text-lg md:text-xl mb-8 max-w-2xl mx-auto">
            Avançamos com tecnologias de ponta para transformar a maneira como
            você busca e processa informações, oferecendo soluções inteligentes
            que conectam dados e geram conhecimento de forma ágil e precisa.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <button className="bg-white text-black px-8 py-3 rounded-full font-semibold hover:bg-gray-200 transition-colors">
              Começar
            </button>
            <button className="border border-white text-white px-8 py-3 rounded-full font-semibold hover:bg-white hover:text-black transition-colors">
              Saber Mais →
            </button>
          </div>
        </div>

        {/* Scroll Indicator */}
        <div className="absolute bottom-8 left-1/2 transform -translate-x-1/2 animate-bounce">
          <svg
            className="w-6 h-6 text-white"
            fill="none"
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth="2"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path d="M19 14l-7 7m0 0l-7-7m7 7V3"></path>
          </svg>
        </div>
      </section>

      {/* Services Section */}
      <section
        id="servicos"
        className="py-20 px-6 bg-gradient-to-b from-black to-gray-900"
      >
        <div className="container mx-auto">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            <ServiceCard
              icon={
                <svg
                  className="w-12 h-12"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"
                  />
                </svg>
              }
              title="Gestão de Conhecimento"
              description="Organize, armazene e compartilhe informações de forma estruturada e acessível."
            />
            <ServiceCard
              icon={
                <svg
                  className="w-12 h-12"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"
                  />
                </svg>
              }
              title="IA Generativa"
              description="Gere conteúdo inteligente e personalizado com algoritmos avançados de IA."
            />
            <ServiceCard
              icon={
                <svg
                  className="w-12 h-12"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                  />
                </svg>
              }
              title="Precisão de Busca"
              description="Encontre exatamente o que procura com nossa tecnologia de busca de alta precisão."
            />
            <ServiceCard
              icon={
                <svg
                  className="w-12 h-12"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M13 10V3L4 14h7v7l9-11h-7z"
                  />
                </svg>
              }
              title="Missões Profundas"
              description="Explore tópicos complexos com análises detalhadas e insights profundos."
            />
          </div>
        </div>
      </section>

      {/* About Research Section */}
      <section id="sobre" className="py-20 px-6 bg-gray-900">
        <div className="container mx-auto">
          <h2 className="text-4xl md:text-5xl font-bold text-white text-center mb-12">
            Sobre as Pesquisas
          </h2>
          <Tabs />
        </div>
      </section>

      <Footer />
    </main>
  );
}
