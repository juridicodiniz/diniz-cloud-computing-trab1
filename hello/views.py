from django.http import HttpResponse

def home(request):     
    html = f'''
    <html>
        <body>
            <h2>Cloud Computing & Site Reliability Engineering</h2>
            <h3>By Fernando Mendes Diniz</h3>
            
        </body>
    </html>
    '''
    return HttpResponse(html)