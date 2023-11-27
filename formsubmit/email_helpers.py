from django.conf import settings
import datetime

def open_and_return():
  with open(settings.BASE_DIR_OS + '/formsubmit/template.html') as file:
    data = file.read()
  return data

def create_html_template(data, user_agent):
  template = open_and_return()
  infors = create_html_lines(data['infors'])
  now = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
  
  return template.format(user_agent, data['subject'], now, infors)


def create_html_lines(data):
    html_lines = [
        f'''<tr><td><div style="color: #101010; font-size: 17px">
        <b>{x['label']}</b>:</b><br /><div style="padding: 5px 0;">{x['value']}</div>
        </div></td></tr>''' for x in data
    ]

    html = '''<tr><td height="12"></td></tr>
    <tr><td height="2px" style="border-radius: 4px; background: #0002;"></td></tr>
    <tr><td height="12"></td></tr>'''.join(html_lines)

    return html