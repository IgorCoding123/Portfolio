from fpdf import FPDF
import datetime

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
        self.ln(10)

    def section_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(2)

    def chapter_body(self, body):
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 5, body)
        self.ln(5)

pdf = PDF()
pdf.add_page()

# Objetivo
pdf.section_title('Objetivo')
pdf.chapter_body('Atuar no desenvolvimento e manutenção de aplicações backend ou fullstack, com foco em Java, Spring Boot e APIs REST, evoluindo tecnicamente em ambientes ágeis.')

# Formação Acadêmica
pdf.section_title('Formação Acadêmica')
pdf.chapter_body('Análise e Desenvolvimento de Sistemas - IFTM (Uberaba - Campus Tecnológico)\nCursando')

# Conhecimentos Técnicos (Atualizado)
pdf.section_title('Conhecimentos Técnicos')
skills = [
    'Linguagem C: Algoritmos, lógica de programação, estruturas de controle, estruturas de dados básicas, modularização e funções.',
    'Estrutura de Dados: Vetores, listas encadeadas (simples, duplas e circulares), pilhas, filas, árvores (binárias, AVL, múltiplas) e grafos.',
    'Pesquisa e Ordenação: Algoritmos de busca, ordenação e análise de complexidade.',
    'Banco de Dados: SQL (PostgreSQL, MySQL), modelagem de dados, consultas, joins e relacionamentos.',
    'Java: Sintaxe, controle de fluxo, POO (herança, polimorfismo, abstração), coleções, enums e APIs padrão.',
    'Spring Framework: Spring Boot 3, Spring MVC, desenvolvimento de APIs REST, Spring Data JPA, Spring Security, persistência, transações e boas práticas.',
    'Segurança e Autenticação: Implementação de JWT (JSON Web Tokens) e controle de acesso.',
    'Testes Automatizados: JUnit 5 e Mockito para testes unitários e mocks de dependências.',
    'Frontend: Angular 17+ (componentização, services, HTTP, routing e integração com APIs REST).',
    'Integração FullStack: CORS, serialização JSON e padrões de arquitetura modernos.',
    'DevOps e Deployment: Netlify (CI/CD), Docker, Render, e automação de deploys.',
    'Ferramentas: Git/GitHub, Maven, Postman, STS, VS Code, Node.js/npm.'
]

for skill in skills:
    pdf.set_font('Arial', '', 10)
    pdf.cell(5)
    pdf.multi_cell(0, 5, f'chr(149) {skill}'.replace('chr(149)', chr(149)))
    pdf.ln(1)

# Idiomas
pdf.ln(5)
pdf.section_title('Idiomas')
pdf.chapter_body('Inglês: Leitura, Escrita e Fala - Médio/Avançado.')

# Data de atualização no rodapé ou fim
pdf.ln(5)
pdf.set_font('Arial', 'I', 8)
pdf.cell(0, 10, f'Atualizado em: {datetime.datetime.now().strftime("%d/%m/%Y")}', 0, 0, 'R')

pdf.output('C:/Users/eduar/OneDrive/Desktop/Portfolio/Curriculo_Igor_Oliveira.pdf')
