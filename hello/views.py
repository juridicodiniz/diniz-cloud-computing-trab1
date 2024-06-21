from django.http import HttpResponse

def home(request):     
    html = f'''
    <html>
    <head>
   <meta charset="utf-8">
   
    <title>DEV | Fernando Diniz | Serra </title>
    <meta name="description"
        content="Atuação em diversas atividades no ramo da TI, como: Projetar, desenvolver, testar, implantar e manter sistemas computacionais de informação; Avaliar, selecionar, especificar e utilizar metodologias, tecnologias e ferramentas da engenharia de software, linguagens de programação e bancos de dados; Coordenar equipes de produção de softwares; Realizar vistorias e perícias em sistemas."/>

	<meta name="Advogado" content="O Escritório Jurídico Diniz presta serviços de Consultoria e Planejamento, especializados nas áreas Previdenciária, Empresárial e Digital" />
	<meta name="Previdenciario" content="Dr.Fernando Diniz, Advogado especialista em Diretio Previdenciário" />
	<meta name="Empresarial" content="Dr.Fernando Diniz, Advogado especialista em Diretio Empresarial" />
	<meta name="Juridico Diniz" content="Escritório Jurídico com especialistas em Direito Previdenciário, Empresárial e Digital" />
	<meta name="LGPD" content="Dr.Fernando Diniz, Advogado especialista na Lei Geral de Proteção de Dados" />
	
	<meta property="og:image" content="https://juridicodiniz.com/images/diniz_oculos_azul.png">
    
  </head>
        <body>
            <h2>Cloud Computing & Site Reliability Engineering</h2>
            <h3>By Fernando Bonitão Diniz</h3>
            
        </body>
    </html>
    '''
    return HttpResponse(html)