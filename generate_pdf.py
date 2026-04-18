from fpdf import FPDF
import datetime
import os

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Igor Oliveira Mateus', 0, 1, 'C')
        self.set_font('Arial', '', 10)
        self.cell(0, 5, 'Email: igor.mateus@estudante.iftm.edu.br | Telefone: (34) 99774-5734', 0, 1, 'C')
        self.cell(0, 5, 'LinkedIn: linkedin.com/in/igor-oliveira-978714230 | GitHub: github.com/IgorCoding123', 0, 1, 'C')
        self.set_font('Arial', 'B', 10)
        self.set_text_color(0, 0, 255)
        self.cell(0, 5, 'Portfolio: https://portfolio-igor-coding.netlify.app/', 0, 1, 'C')
        self.set_text_color(0, 0, 0)
        self.ln(5)

    def section_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(240, 240, 240)
        self.cell(0, 8, f'  {title}', 0, 1, 'L', 1)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 5, body)
        self.ln(2)

    def project_item(self, title, desc, tech):
        self.set_font('Arial', 'B', 10)
        self.cell(0, 5, title, 0, 1, 'L')
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 5, desc)
        self.set_font('Arial', 'I', 9)
        self.cell(0, 5, f'Tecnologias: {tech}', 0, 1, 'L')
        self.ln(3)

pdf = PDF()
pdf.add_page()

# Objetivo
pdf.section_title('Objetivo')
pdf.chapter_body('Atuar no desenvolvimento de aplicações backend e fullstack, com forte embasamento em Java e Spring Boot, além de especialização em processos de automação, web scraping e análise de dados com Python.')

# Formação Acadêmica
pdf.section_title('Formação Acadêmica')
pdf.chapter_body('Análise e Desenvolvimento de Sistemas - IFTM (Uberaba - Campus Tecnológico)\nCursando')

# Conhecimentos Técnicos (Atualizado)
pdf.section_title('Conhecimentos Técnicos')
skills = [
    'Java & Backend: Core, POO, Spring Boot 3, Spring Security, JWT, JPA/Hibernate, APIs RESTful.',
    'Python & Data: Automação, Pandas, NumPy, YFinance, Matplotlib, Seaborn, Insights de Negócio.',
    'Web Scraping & Automação: Selenium (Stealth), Playwright, Scroll Dinâmico, Extração de Sites SPA.',
    'Big Data & SQL: PostgreSQL, MySQL, DuckDB (processamento de datasets 5GB+), modelagem e otimização.',
    'Frontend: Angular 17+ (TypeScript, Componentização, RXJS, Integração via HTTP).',
    'Linguagem C: Estrutura de Dados avançada, Algoritmos de Pesquisa/Ordenação e Complexidade.',
    'Testes & QA: Testes Unitários com JUnit 5, Mockito e depuração de aplicações.',
    'Ferramentas & DevOps: Git/GitHub, Maven, Docker, Postman, Netlify (CI/CD), Node.js/npm.'
]

for skill in skills:
    pdf.set_font('Arial', '', 10)
    pdf.cell(5)
    pdf.multi_cell(0, 5, f'{chr(149)} {skill}')
    pdf.ln(1)

# Principais Projetos
pdf.ln(2)
pdf.section_title('Destaques de Projetos Portfólio')

pdf.project_item(
    'Gestão Rural - Pecuária (FullStack)',
    'Plataforma completa para controle de rebanhos e finanças com autenticação JWT e arquitetura modular.',
    'Angular 17, Spring Boot 3, MySQL, Spring Security.'
)

pdf.project_item(
    'Funil de Conversão E-commerce (Big Data)',
    'Análise de comportamento de milhões de usuários em dataset de 5GB+ utilizando SQL de alta performance.',
    'Python, DuckDB, Plotly, SQL.'
)

pdf.project_item(
    'Buscador Global de Preços & Automação de Leads',
    'Sistemas de extração de dados e automação de mensagens para prospecção em escala e comparação de preços.',
    'Python, Selenium Stealth, Playwright, Pandas, Rich.'
)

pdf.project_item(
    'Análise de Vendas Superstore (BI)',
    'Dashboard interativo para identificação de sazonalidade e geração de insights recomendados para o negócio.',
    'Python, Pandas, Chart.js, HTML/CSS.'
)

# Idiomas
pdf.section_title('Idiomas')
pdf.chapter_body('Inglês: Leitura, Escrita e Fala - Médio/Avançado.')

# Rodapé
pdf.ln(5)
pdf.set_font('Arial', 'I', 8)
pdf.cell(0, 10, f'Atualizado em: {datetime.datetime.now().strftime("%d/%m/%Y")}', 0, 0, 'R')

output_path = 'Curriculo_Igor_Oliveira.pdf'
pdf.output(output_path)
print(f'PDF gerado com sucesso: {output_path}')
