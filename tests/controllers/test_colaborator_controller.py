import requests
from .config import get_url, get_header, get_db
from src.domain.entities.colaborator import Colaborator

def _colaborator_data() -> dict:
    return {'cpf': '91834522798', 'email': 'sergiowgs9t@gmail.com', 'name':'Sergio29', 'cell_phone': '29964049400', 'colaborator_type_id': 1}

def _count_colaborators(id=0)->int:
    db = get_db()
    result = ''
    with db.get_session() as session:
        if (id != 0):
            result = session.execute(f"select count(*) from Colaborator where id = {id} and status <> 0").all()
        else:
            result = session.execute("select count(*) from Colaborator where status <> 0").all()
    return int(result[0][0])

def _clear_test(id)->None:
    url = f'{_get_url()}/{id}'
    requests.delete(url=url, headers=get_header(), timeout=600000)

def _get_url() -> str:
    return f'{get_url()}/colaborators'

def _create_colaborator() -> int:
    json_data = _colaborator_data()
    url = _get_url()
    response = requests.post(url=url, headers=get_header(), json=json_data, timeout=600000)
    result_request = response.json()
    return result_request['id']

def test_get_all():
    # arrange
    url = _get_url()
    total = _count_colaborators()

    # act
    response = requests.get(url=url, headers=get_header(), timeout=600000)
    result_request = response.json()

    #assert
    assert response.status_code == 200
    assert len(result_request) == total

def test_get_exist():
    # arrange
    new_id = _create_colaborator()
    url = f'{_get_url()}/{new_id}'

    # act
    response = requests.get(url=url, headers=get_header(), timeout=600000)
    result_request = response.json()

    #assert
    assert response.status_code == 200
    assert result_request['id'] == new_id

    _clear_test(new_id)

def test_get_not_exist():
    # arrange
    id = -1
    url = f'{_get_url()}/{id}'

    # act
    response = requests.get(url=url, headers=get_header(), timeout=600000)

    #assert
    assert response.status_code == 404

def test_insert_exist():
    # arrange
    json_data = _colaborator_data()
    url = _get_url()

    # act
    response = requests.post(url=url, headers=get_header(), json=json_data, timeout=600000)
    result_request = response.json()

    #assert
    assert response.status_code == 201
    assert result_request['id'] != ''
    assert result_request['cpf'] == json_data['cpf']

    _clear_test(result_request['id'])

def test_delete():
    # arrange
    new_id = _create_colaborator()
    url = _get_url()

    #act
    response = requests.delete(url=f"{url}/{new_id}", headers=get_header(), timeout=600000)

    #assert
    assert response.status_code == 204
    assert _count_colaborators(new_id) == 0
