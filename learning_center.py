from h2o_wave import site, main, app, Q, ui
import session
from datetime import timedelta
from tzlocal import get_localzone
import pytz
from datetime import datetime

#global current_tutorial
current_tutorial = 0
nav_item_selected = 0
content = '![Learning Path](https://s3.amazonaws.com/data.h2o.ai/DAI-Tutorials/Aquarium/sergio-perez-dai-1-gpu/V191/dai-learning-path-191-v1.png)'
lab = '1' #lab 1 in Aquarium is title: Driverless AI Test Drive (1.9.1 Experimental) (1 GPU)

tutorials_list = [
    [
    'https://5675sp.github.io/tutorials/1.9.1/automatic-ml-intro-with-driverless-ai',
    'https://5675sp.github.io/tutorials/1.9.1/machine-learning-experiment-scoring-and-analysis-financial-focus',
    'https://5675sp.github.io/tutorials/1.9.1/machine-learning-interpretability',
    'https://5675sp.github.io/tutorials/1.9.1/time-series-recipe-retail-sales-forecasting',
    'https://5675sp.github.io/tutorials/1.9.1/natural-language-processing-sentiment-analysis',
    'https://5675sp.github.io/tutorials/1.9.1/image-processing-in-driverless-ai',
    'https://5675sp.github.io/tutorials/1.9.1/get-started-with-open-source-custom-recipes',
    'https://5675sp.github.io/tutorials/1.9.1/build-your-own-custom-recipe',
    'https://5675sp.github.io/tutorials/1.9.1/scoring-pipeline-deployment-introduction',
    'https://5675sp.github.io/tutorials/1.9.1/scoring-pipeline-deployment-templates',
    'https://5675sp.github.io/tutorials/1.9.1/scoring-pipeline-deployment-in-java-runtime',
    'https://5675sp.github.io/tutorials/1.9.1/scoring-pipeline-deployment-in-c++-runtime',
    'https://5675sp.github.io/tutorials/1.9.1/scoring-pipeline-deployment-in-python-runtime',
    'https://5675sp.github.io/tutorials/1.9.1/disparate-impact-analysis',
    'https://5675sp.github.io/tutorials/1.9.1/risk-assessment-tools-in-the-world-of-ai-the-social-sciences-and-humanities'
    ],
    [
    'https://5675sp.github.io/tutorials/1.9.0/automatic-ml-intro-with-driverless-ai',
    'https://5675sp.github.io/tutorials/1.9.0/machine-learning-experiment-scoring-and-analysis-tutorial-financial-focus',
    'https://5675sp.github.io/tutorials/1.9.0/machine-learning-interpretability-tutorial',
    'https://5675sp.github.io/tutorials/1.9.0/time-series-recipe-tutorial-retail-sales-forecasting',
    'https://5675sp.github.io/tutorials/1.9.0/natural-language-processing-tutorial-sentiment-analysis',
    'https://5675sp.github.io/tutorials/1.9.0/get-started-with-open-source-custom-recipes-tutorial',
    'https://5675sp.github.io/tutorials/1.9.0/build-your-own-custom-recipe-tutorial',
    'https://5675sp.github.io/tutorials/1.9.0/scoring-pipeline-deployment-introduction',
    'https://5675sp.github.io/tutorials/1.9.0/scoring-pipeline-deployment-templates',
    'https://5675sp.github.io/tutorials/1.9.0/scoring-pipeline-deployment-in-java-runtime',
    'https://5675sp.github.io/tutorials/1.9.0/scoring-pipeline-deployment-in-c++-runtime',
    'https://5675sp.github.io/tutorials/1.9.0/scoring-pipeline-deployment-in-python-runtime',
    'https://5675sp.github.io/tutorials/1.9.0/disparate-impact-analysis-tutorial',
    'https://5675sp.github.io/tutorials/1.9.0/risk-assessment-tools-in-the-world-of-ai-the-social-sciences-and-humanities'
    ],
    [
    'https://5675sp.github.io/tutorials/1.8.7.1/automatic-ml-intro-test-drive-tutorial',
    'https://5675sp.github.io/tutorials/1.8.7.1/machine-learning-experiment-scoring-and-analysis-tutorial-financial-focus',
    'https://5675sp.github.io/tutorials/1.8.7.1/machine-learning-interpretability-tutorial',
    'https://5675sp.github.io/tutorials/1.8.7.1/time-series-recipe-tutorial-retail-sales-forecasting',
    'https://5675sp.github.io/tutorials/1.8.7.1/natural-language-processing-tutorial-sentiment-analysis',
    'https://5675sp.github.io/tutorials/1.8.7.1/get-started-with-open-source-custom-recipes-tutorial',
    'https://5675sp.github.io/tutorials/1.8.7.1/build-your-own-custom-recipe-tutorial',
    'https://5675sp.github.io/tutorials/1.8.7.1/scoring-pipeline-deployment-introduction'
    ]
]


list_of_tutorials = [

    [
    'Tutorial 1A: Automatic Machine Learning Introduction with Driverless AI', 
    'Tutorial 1B: Machine Learning Experiment Scoring and Analysis - Financial Focus', 
    'Tutorial 1C: Machine Learning Interpretability',
    'Tutorial 2A: Time Series Recipe - Retail Sales Forecasting',
    'Tutorial 2B: Natural Language Processing - Sentiment Analysis',
    'Tutorial 2C: Image Processing in Driverless AI',
    'Tutorial 3A: Get Started with Open Source Custom Recipes',
    'Tutorial 3B: Build Your Own Custom Recipe',
    'Tutorial 4A: Scoring Pipeline Deployment Introduction',
    'Tutorial 4B: Scoring Pipeline Deployment Templates',
    'Tutorial 4C: Scoring Pipeline Deployment in Java Runtime',
    'Tutorial 4D: Scoring Pipeline Deployment in C++ Runtime',
    'Tutorial 4E: Scoring Pipeline Deployment in Python Runtime',
    'Tutorial 5A: Disparate Impact Analysis',
    'Tutorial 5B: Risk Assessment Tools in the World of AI, the Social Sciences, and Humanities'
    ],
    [
    'Tutorial 1A: Automatic Machine Learning Introduction with Driverless AI', 
    'Tutorial 1B: Machine Learning Experiment Scoring and Analysis - Financial Focus', 
    'Tutorial 1C: Machine Learning Interpretability',
    'Tutorial 2A: Time Series Recipe - Retail Sales Forecasting',
    'Tutorial 2B: Natural Language Processing - Sentiment Analysis',
    'Tutorial 3A: Get Started with Open Source Custom Recipes',
    'Tutorial 3B: Build Your Own Custom Recipe',
    'Tutorial 4A: Scoring Pipeline Deployment Introduction',
    'Tutorial 4B: Scoring Pipeline Deployment Templates',
    'Tutorial 4C: Scoring Pipeline Deployment in Java Runtime',
    'Tutorial 4D: Scoring Pipeline Deployment in C++ Runtime',
    'Tutorial 4E: Scoring Pipeline Deployment in Python Runtime',
    'Tutorial 5A: Disparate Impact Analysis',
    'Tutorial 5B: Risk Assessment Tools in the World of AI, the Social Sciences, and Humanities'
    ],
    [
    'Tutorial 1A: Automatic Machine Learning Introduction with Driverless AI', 
    'Tutorial 1B: Machine Learning Experiment Scoring and Analysis - Financial Focus', 
    'Tutorial 1C: Machine Learning Interpretability',
    'Tutorial 2A: Time Series Recipe - Retail Sales Forecasting',
    'Tutorial 2B: Natural Language Processing - Sentiment Analysis',
    'Tutorial 3A: Get Started with Open Source Custom Recipes',
    'Tutorial 3B: Build Your Own Custom Recipe',
    'Tutorial 4A: Scoring Pipeline Deployment Introduction'
    ]
]


async def lab_instruction(q: Q, url: str):

    q.page['tutorial_content'] = ui.frame_card(
       box='1 2 -1 -1',
       title='',
       path=url
    )

    await q.page.save()

async def dropdown(q: Q):

    jsonRes = session.top_bar()
    
    name = jsonRes['userName']
    role = jsonRes['userRole']

    versions = [
        '1.9.1',
        '1.9.0',
        '1.8.7.1'
    ]

    name_of_nav_items = [
        '_0',
        '_1',
        '_2'
    ]
     
    q.page['header'] = ui.header_card(
        box='1 1 1 1',
        title='L + A',
        subtitle='V: 1.9.1',
        nav=[
            ui.nav_group(
                label='Tutorial Versions',
                items=[ui.nav_item(name=f'{name_of_nav_items[i]}', label=versions[i]) for i in range(len(versions))]
            ),
            ui.nav_group(
                label=f'{name} ({role})',
                items=[ui.nav_item(name='logout', label='logout')]
            )
        ],
    )

    q.page['dropdown'] = ui.form_card(
        box='2 1 4 1',
        items=[
            ui.text(''),
            ui.dropdown(name='dropdown', label='', value ='0', placeholder = list_of_tutorials[nav_item_selected][0],choices=[
                        ui.choice(name=f'{i}', label=list_of_tutorials[nav_item_selected][i]) for i in range(len(list_of_tutorials[nav_item_selected]))
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
                ui.button(name='start',label='Start', primary=True, disabled=bool_start),
                ui.button(name='end',label='End', primary=True, disabled=bool_end)
            ], justify='center')
        ]
    )
    await q.page.save()

async def modified_buttons(q: Q, start: bool, end: bool):
    q.page['buttons'].items[1].buttons.items[2].button.disabled = start
    q.page['buttons'].items[1].buttons.items[3].button.disabled = end 
    await q.page.save()

def create_lab_instance():
    session_holder = session.get_session()
    create_api_start_lab = "https://aquarium.h2o.ai/api/startLab"
    data = {"labId": f"{lab}"}
    session_holder.post(create_api_start_lab, data=data, verify=False)

def get_lab_instance_metrics():
    session_holder = session.get_session()
    url_api_lab_number = f'https://aquarium.h2o.ai/api/lab/{lab}'
    req = session_holder.get(url_api_lab_number, verify=False)
    jsonRes = req.json()
    return jsonRes

async def update_lab_instance_metrics(q: Q, initiate: bool):
 
    if initiate:
        q.page['metrics'] = ui.form_card(
            box='9 1 -1 1',
            items= []
        )

    global exit
    exit = False

    while True:
        if exit: 
            break;

        jsonRes = get_lab_instance_metrics()

        if jsonRes['state'] == '' :
            q.page['metrics'].items = [
                ui.text(''),
                ui.separator(label='Lab Instance Metrics Will Appear Here')
            ]
            await modified_buttons(q, False, True)
            break;

        if jsonRes['state'] != 'running':
            if jsonRes['cloudState'] == 'ROLLBACK_IN_PROGRESS':
                q.page['metrics'].items = [
                    ui.message_bar(type='error', text=f'Lab failed to start properly. Please try ending and restarting the lab. If this condition persists, please notify your Aquarium administrator.')
                ]
                await q.page.save()
                break;
            else: 
                state = jsonRes['state']
                q.page['metrics'].items = [
                    ui.progress(label=f'Please wait, starting the lab may take several minutes [{state}]', caption='')
                ]
                await modified_buttons(q, True, False)

        elif jsonRes['state'] == 'running': 
            outputs = jsonRes['outputs']
            description = outputs[0]['description']
            value = outputs[0]['value']
            time = timestamp_to_hours_minutes_format(jsonRes['runningStartTime'],jsonRes['durationMinutes'])
            url = f'''**{description}:** <a href="{value}" target="_blank">{value}</a>'''
            q.page['metrics'].items = [
                ui.inline(items=[
                    ui.message_bar(type='success', text=f'Time: {time}'),
                    ui.text(url),
                ])
            ]
            await modified_buttons(q, True, False)

        await q.page.save()
        await q.sleep(20)

def end_lab_instance():
    session_holder = session.get_session()
    url_api_end_lab = "https://aquarium.h2o.ai/api/endLab"
    data = {"labId": f"{lab}"}
    session_holder.post(url_api_end_lab, data=data, verify=False)

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
        'metrics',
        'header'
    ]

    for name in names:
        del q.page[f'{name}']
    
    await q.page.save()
    
@app('/learning_center')
async def serve(q: Q):
    
    global nav_item_selected

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
            await lab_instruction(q, tutorials_list[nav_item_selected][0])
            await dropdown(q)
            await buttons(q, False, True)
            await update_lab_instance_metrics(q, True)
    
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
        create_lab_instance()
        await update_lab_instance_metrics(q, False)

    if q.args.end:
        end_lab_instance()
        await update_lab_instance_metrics(q, False)
            
    global exit
    global lab 
    if q.args.logout:
        exit = True
        lab = '1'
        await delete_cards(q)
        session.logout_method()
        await session.login_options(q)
    
    global content
    if q.args.path:
        q.page['path'].dialog = ui.dialog(title='', items=[
            ui.text(content = content),
            ui.buttons([ui.button(name='close',label='Close', primary=True, disabled=False)], justify='center')
        ], closable=False, width='1500px')
        await q.page.save()

    if q.args.close:
        q.page['path'].dialog = None
        await q.page.save()

    if q.args.select:

        value = q.args.dropdown

        if value == None:
            global current_tutorial
            value = current_tutorial
        else:
            value = int(value)
            current_tutorial = value

        q.page['tutorial_content'].path = tutorials_list[nav_item_selected][value]
        print(nav_item_selected)
        print(value)
     
        await q.page.save()
    
    if q.args._0:
        nav_item_selected = 0
        q.page['tutorial_content'].path = tutorials_list[nav_item_selected][0]
        q.page['dropdown'].items[1].dropdown.choices = [
                        ui.choice(name=f'{i}', label=list_of_tutorials[nav_item_selected][i]) for i in range(len(list_of_tutorials[nav_item_selected]))
                    ]
        q.page['header'].subtitle = 'V: 1.9.1'
        content = '![Learning Path](https://s3.amazonaws.com/data.h2o.ai/DAI-Tutorials/Aquarium/sergio-perez-dai-1-gpu/V191/dai-learning-path-191-v1.png)'
        lab = '1'
        exit = True
        await update_lab_instance_metrics(q, False)
   
    if q.args._1:
        nav_item_selected = 1
        q.page['tutorial_content'].path = tutorials_list[nav_item_selected][0]
        q.page['dropdown'].items[1].dropdown.choices = [
                        ui.choice(name=f'{i}', label=list_of_tutorials[nav_item_selected][i]) for i in range(len(list_of_tutorials[nav_item_selected]))
                    ]
        q.page['header'].subtitle = 'V: 1.9.0'
        content = '![Learning Path](https://s3.amazonaws.com/data.h2o.ai/DAI-Tutorials/Aquarium/sergio-perez-dai-1-gpu/V190/dai-learning-path-190-v7.png)'
        lab = '3'
        exit = True
        await update_lab_instance_metrics(q, False)
     
    if q.args._2:
        nav_item_selected = 2
        q.page['tutorial_content'].path = tutorials_list[nav_item_selected][0]
        q.page['dropdown'].items[1].dropdown.choices = [
                        ui.choice(name=f'{i}', label=list_of_tutorials[nav_item_selected][i]) for i in range(len(list_of_tutorials[nav_item_selected]))
                    ]
        q.page['header'].subtitle = 'V: 1.8.7.1'
        content = '![Learning Path](https://s3.amazonaws.com/data.h2o.ai/DAI-Tutorials/Aquarium/ana-castro-dai-1-gpu/v5/dai-learning-path-1871.png)'
        lab = '1'
        exit = True
        await update_lab_instance_metrics(q, False)

       
    
   
    






    

    


    
   
        



  
    
    


