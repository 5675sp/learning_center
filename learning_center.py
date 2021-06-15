from h2o_wave import site, main, app, Q, ui
import session
from logout import logout_method
from datetime import timedelta
from tzlocal import get_localzone
import pytz
from datetime import datetime

global current
current = 0

async def lab_instruction(q: Q, url: str):

    q.page['tutorial_content'] = ui.frame_card(
       box='1 2 -1 -1',
       title='',
       path=url
    )

    await q.page.save()

async def dropdown(q: Q):

    list_of_tutorials = [
        'Tutorial 1A: Automatic Machine Learning Introduction with Driverless AI', 
        'Tutorial 1B: Machine Learning Experiment Scoring and Analysis Tutorial - Financial Focus', 
        'Tutorial 1C: Machine Learning Interpretability Tutorial',
        'Tutorial 2A: Time Series Recipe Tutorial - Retail Sales Forecasting',
        'Tutorial 2B: Natural Language Processing Tutorial - Sentiment Analysis',
        'Tutorial 3A: Get Started with Open Source Custom Recipes Tutorial',
        'Tutorial 3B: Build Your Own Custom Recipe Tutorial',
        'Tutorial 4A: Scoring Pipeline Deployment Introduction',
        'Tutorial 4B: Scoring Pipeline Deployment Templates',
        'Tutorial 4C: Scoring Pipeline Deployment in Java Runtime',
        'Tutorial 4D: Scoring Pipeline Deployment in C++ Runtime',
        'Tutorial 4E: Scoring Pipeline Deployment in Python Runtime',
        'Tutorial 5A: Disparate Impact Analysis Tutorial',
        'Tutorial 5B: Risk Assessment Tools in the World of AI, the Social Sciences, and Humanities'
        ]



    versions = [
        '1.9.1',
        '1.9.0',
        '1.8.7.1',
        '1.8.4.1',
        '1.8.0',
        '1.7.0',
        '1.6.0',
        '1.4.2'

    ]
    q.page['header'] = ui.header_card(
        box='1 1 1 1',
        title='H2O.ai',
        subtitle='Tutorials',
        nav=[
            ui.nav_group(
                label='Tutorial Versions',
                items=[ui.nav_item(name=f'#{e}', label=e) for e in versions]
            ),
            ui.nav_group(
                label='Sergio Perez (admin)',
                items=[ui.nav_item(name='logout', label='logout')]
            )
        ],
    )

    q.page['dropdown'] = ui.form_card(
        box='2 1 4 1',
        items=[
            ui.text(''),
            ui.dropdown(name='dropdown', label='', value ='0', placeholder = 'Tutorial 1A: Automatic Machine Learning Introduction with Driverless AI',choices=[
                        ui.choice(name=f'{i}', label=list_of_tutorials[i]) for i in range(len(list_of_tutorials))
                    ])
        ]
    )

    await q.page.save()


async def buttons(q: Q, bool_start: bool, bool_end: bool):
    q.page['buttons'] = ui.form_card(
        box='6 1 3 1',
        items=[
            ui.text(''),
            ui.buttons(items = [
                ui.button(name='select',label='Select', primary=True, disabled=False),
                ui.button(name='path',label='Path', primary=True, disabled=False),
                #ui.button(name='logout',label='Logout', primary=True, disabled=False),
                ui.button(name='start',label='Start', primary=True, disabled=bool_start),
                ui.button(name='end',label='End', primary=True, disabled=bool_end)
            ], justify='center')
        ]
    )
    await q.page.save()


def create_lab_instance():
    session_holder = session.get_session()
    create_api_start_lab = "https://aquarium.h2o.ai/api/startLab"
    data = {"labId": "24"}
    session_holder.post(create_api_start_lab, data=data, verify=False)
    print('lab instance was created')


def get_lab_instance_metrics():
    session_holder = session.get_session()
    url_api_lab_number = f'https://aquarium.h2o.ai/api/lab/24'
    req = session_holder.get(url_api_lab_number, verify=False)
    jsonRes = req.json()
    print('----------------------------------------------')
    print(jsonRes)
    print('----------------------------------------------')
    return jsonRes



async def lab_instance_metrics(q: Q):

    jsonRes = get_lab_instance_metrics()

    print(jsonRes)

 
    q.page['metrics'] = ui.form_card(
        box='9 1 -1 1',
        items=[
            ui.text(''),
            ui.separator(label='Lab Instance Metrics Will Appear Here')
            ]
    )

    await q.page.save()

    if jsonRes['state'] == 'running':
        print('ONE')
        await buttons(q, True, False)
        await update_lab_instance_metrics(q, False)


async def update_lab_instance_metrics(q: Q, exist: bool):

    if exist:
        create_lab_instance()
    
    while True:
        print('TWO')
        jsonRes = get_lab_instance_metrics()

        if jsonRes['state'] != 'running':

            state = jsonRes['state']
            q.page['metrics'].items = [
                ui.text(''),
                ui.progress(label=f'Please wait, starting the lab may take several minutes [{state}]', caption='')
            ]

        elif jsonRes['state'] == 'running': 

            state = jsonRes['state']
            labId = jsonRes['labId']
            outputs = jsonRes['outputs']
            description = outputs[0]['description']
            value = outputs[0]['value']
            time = timestamp_to_hours_minutes_format(jsonRes['runningStartTime'],jsonRes['durationMinutes'])
            url = f'''**{description}:** <a href="{value}" target="_blank">{value}</a>'''
            q.page['metrics'].items = [
                ui.inline(items=[
                    ui.message_bar(type='success', text=f'Success | Time: {time}'),
                    ui.text(url),
                ])
                #ui.message_bar(type='success', text=f'Success | Time: {time} | Lab instance ID: {str(labId)} | Lab instance state: {state}')
            ]

        print('INSIDE THE WHILE TRUE')
        await q.page.save()
        await q.sleep(20)

def end_lab_instance():
    session_holder = session.get_session()
    url_api_end_lab = "https://aquarium.h2o.ai/api/endLab"
    data = {"labId": "24"}
    session_holder.post(url_api_end_lab, data=data, verify=False)
    print('LAB INSTANCE ENDED')


async def update_end_lab_instance_metrics(q: Q):

    q.page['metrics'].items = [
                ui.text(''),
                ui.separator(label='Lab Instance Metrics Will Appear Here')
            ]

    await q.page.save()


def timestamp_to_hours_minutes_format(running_start_time: int, running_duration_minutes: int):  

    if running_start_time == 0:
        return 'starting'

    zone = str(get_localzone())

    x= datetime.fromtimestamp(running_start_time/1000, pytz.timezone(zone))

    year = int(x.strftime("%Y"))
    month = int(x.strftime("%m"))
    day = int(x.strftime("%d"))
    hour = int(x.strftime("%H"))
    minute = int(x.strftime("%M"))
    second = int(x.strftime("%S"))

    date_1 = datetime(year,month,day,hour,minute,second)

    year = int(x.strftime("%Y"))
    month = int(x.strftime("%m"))
    day = int(x.strftime("%d"))
    hour = int(x.strftime("%H"))
    minute = int(x.strftime("%M"))
    second = int(x.strftime("%S"))

    appropriate_zone = pytz.timezone(zone)
    x = datetime.now(appropriate_zone)

    year = int(x.strftime("%Y"))
    month = int(x.strftime("%m"))
    day = int(x.strftime("%d"))
    hour = int(x.strftime("%H"))
    minute = int(x.strftime("%M"))
    second = int(x.strftime("%S"))

    date_2 = datetime(year,month,day,hour,minute,second)

    total_seconds = date_2 - date_1

    total_minutes = int(total_seconds / timedelta(minutes=1))
    
    total_seconds = (running_duration_minutes-total_minutes) * 60
   
    seconds = total_seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d hour(s), %02d minute(s)" % (hour, minutes)


async def delete_cards(q: Q):
    names = [
        'tutorial_content',
        'dropdown',
        'learning_path',
        'buttons',
        'metrics'
    ]

    for name in names:
        del q.page[f'{name}']

    await q.page.save()
    
@app('/learning_center')
async def serve(q: Q):
    
    if not q.client.initialized:
        q.client.initialized = True
        q.page['path'] = ui.meta_card(box='')
        await session.login_options(q)
        
    if q.args.loginbutton:

        session.start_session(q.args.email, q.args.password)
        valid = session.get_valid()

        if valid:
            del q.page['login']
            del q.page['logo']
            await lab_instruction(q, 'https://5675sp.github.io/tutorials/1.9.0/automatic-ml-intro-with-driverless-ai')
            await dropdown(q)
            await buttons(q, False, True)
            await lab_instance_metrics(q)
    
        else: 
            await session.login_failed(q)

    if q.args.option_one_openid:
        await session.login(q)

    if q.args.option_two_create_account:
        await session.creat_account(q)

    if q.args.back_from_login_page:
        await session.login_options(q)

    if q.args.back_from_create_account_page:
        await session.login_options(q)

    if q.args.start:
        await buttons(q, True, False)
        await update_lab_instance_metrics(q, True)

    if q.args.end:
        end_lab_instance()
        await buttons(q, False, True)
        await update_end_lab_instance_metrics(q)

    if q.args.logout:
        await delete_cards(q)
        logout_method()
        await session.login_options(q)
        

    if q.args.path:
        content = '![Learning Path](https://s3.amazonaws.com/data.h2o.ai/DAI-Tutorials/Aquarium/sergio-perez-dai-1-gpu/V191/dai-learning-path-191-v1.png)'
        q.page['path'].dialog = ui.dialog(title='', items=[
            ui.text(content),
            ui.buttons([ui.button(name='close',label='Close', primary=True, disabled=False)], justify='center')
        ], closable=False, width='1500px')
        await q.page.save()

    if q.args.close:
        q.page['path'].dialog = None
        await q.page.save()
     
    if q.args.select:

        value = q.args.dropdown

        if value == None:
            global current
            value = current 
        else:
            value = int(value)
            current = value

        if value == 0:
            q.page['tutorial_content'].path = 'https://5675sp.github.io/tutorials/1.9.0/automatic-ml-intro-with-driverless-ai'
        elif value == 1:
            q.page['tutorial_content'].path = 'https://5675sp.github.io/tutorials/1.9.0/machine-learning-experiment-scoring-and-analysis-tutorial-financial-focus'
        elif value == 2:
            q.page['tutorial_content'].path = 'https://5675sp.github.io/tutorials/1.9.0/machine-learning-interpretability-tutorial'
        elif value == 3:
            q.page['tutorial_content'].path = 'https://5675sp.github.io/tutorials/1.9.0/time-series-recipe-tutorial-retail-sales-forecasting'
        elif value == 4:
            q.page['tutorial_content'].path = 'https://5675sp.github.io/tutorials/1.9.0/natural-language-processing-tutorial-sentiment-analysis'
        elif value == 5:
            q.page['tutorial_content'].path = 'https://5675sp.github.io/tutorials/1.9.0/get-started-with-open-source-custom-recipes-tutorial'
        elif value == 6:
            q.page['tutorial_content'].path = 'https://5675sp.github.io/tutorials/1.9.0/build-your-own-custom-recipe-tutorial'
        elif value == 7:
            q.page['tutorial_content'].path = 'https://5675sp.github.io/tutorials/1.9.0/scoring-pipeline-deployment-introduction'
        elif value == 8:
            q.page['tutorial_content'].path = 'https://5675sp.github.io/tutorials/1.9.0/scoring-pipeline-deployment-templates'
        elif value == 9:
            q.page['tutorial_content'].path = 'https://5675sp.github.io/tutorials/1.9.0/scoring-pipeline-deployment-in-java-runtime'
        elif value == 10:
            q.page['tutorial_content'].path = 'https://5675sp.github.io/tutorials/1.9.0/scoring-pipeline-deployment-in-c++-runtime'
        elif value == 11:
            q.page['tutorial_content'].path = 'https://5675sp.github.io/tutorials/1.9.0/scoring-pipeline-deployment-in-python-runtime'
        elif value == 15:
            q.page['tutorial_content'].path = 'https://5675sp.github.io/tutorials/1.9.0/disparate-impact-analysis-tutorial'
        elif value == 16:
            q.page['tutorial_content'].path = 'https://5675sp.github.io/tutorials/1.9.0/risk-assessment-tools-in-the-world-of-ai-the-social-sciences-and-humanities'
     
        await q.page.save()

    























 


       
   
    






    

    


    
   
        



  
    
    


