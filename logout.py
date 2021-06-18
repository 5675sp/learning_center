import session

def logout_method():

    session_holder = session.get_session()
    url_logout = "https://aquarium.h2o.ai/api/logout"
    session_holder.get(url_logout, verify=False)
    print('user has been logout')

