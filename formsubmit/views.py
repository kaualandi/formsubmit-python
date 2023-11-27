from django.http import JsonResponse
from rest_framework.decorators import api_view
from .email_helpers import *
from django.core.mail import EmailMessage
from django.conf import settings
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

@api_view(['POST'])
def send_email(request, email_address):
    data = request.data
    print(email_address + '-----------------------------------')
    user_agent = request.META['HTTP_USER_AGENT']
    html = create_html_template(data, user_agent)
    
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = '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'

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    subject = "Você recebeu uma nova mensagem em " + data['name'] + "!"
    sender = {"name":"Noclaf Forms","email":"eu@kaualf.com"}
    email = [{"email": email_address}]
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=email, html_content=html, sender=sender, subject=subject)

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)

    return JsonResponse({'worked': True})
