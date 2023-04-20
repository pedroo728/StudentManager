import requests
from .config import get_url, get_header, get_db

def _count_levels(id=0)->int:
    db = get_db()
    result = ''
    with db.get_session() as session:
        if (id != 0):
            result = session.execute(f"select count(*) from LevelType where id = {id} and status <> 0").all()
        else:
            result = session.execute("select count(*) from LevelType where status <> 0").all()
    return int(result[0][0])

def _get_url() -> str:
    return f'{get_url()}/level_types'

def test_get_all():
    # arrange
    url = _get_url()
    total = _count_levels()

    # act
    response = requests.get(url=url, headers=get_header(), timeout=600000)
    result_request = response.json()

    #assert
    assert response.status_code == 200
    assert len(result_request) == total

def test_get_exist():
    # arrange
    new_id = 1
    url = f'{_get_url()}/{new_id}'

    # act
    response = requests.get(url=url, headers=get_header(), timeout=600000)
    result_request = response.json()

    #assert
    assert response.status_code == 200
    assert result_request['id'] == new_id
    
def test_get_not_exist():
    # arrange
    id = -1
    url = f'{_get_url()}/{id}'

    # act
    response = requests.get(url=url, headers=get_header(), timeout=600000)

    #assert
    assert response.status_code == 404
