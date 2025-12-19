from pytest import mark
import logging

logger = logging.getLogger(__name__)

@mark.django_db
def test_create_task(api_client) -> None:

    """
    Test the create task API
    
    :param api_client:
    :return: None

    """

    payload = {
        "title": "Wash Clothes",
        "content" : "Wash clothes in the washing machine"
    }

    response_create = api_client.post("/api/tasks/",data=payload, format="json")
    task_id = response_create.data["task"]['id']
    logger.info(f"Created task with id: {task_id}")
    logger.info(f"Response : {response_create.data}")

    assert response_create.status_code == 201
    assert response_create.data["task"]["title"] == payload["title"]

    response_read = api_client.get(f"/api/tasks/{task_id}", format="json")
    logger.info(f"Read task with id: {task_id}")
    logger.info(f"Response: {response_read.data}")
    assert response_read.status_code == 200
    assert response_read.data["task"]["title"] == payload["title"]

@mark.django_db
def test_patch_task(api_client) -> None:

    """
    Test the update task API
    :param api_client:
    :return: None
    """

    payload = {
        "title":"Trim the Lawn",
        "content": "Trim the lawn with the lawnmower"
    }

    response_create = api_client.post("/api/tasks/",data=payload, format="json")
    task_id = response_create.data['task']['id']
    logger.info(f"Created task with id : {task_id}")
    logger.info(f"Response : {response_create.data}")

    assert response_create.status_code  == 201
    assert response_create.data["task"]["title"] == payload["title"]

    payload["title"] = "Cut the grass"
    response_update = api_client.patch(f"/api/tasks/{task_id}", data=payload,format="json")
    logger.info(f"Updated task with id: {task_id}")
    logger.info(f"Response: {response_update.data}")
    assert response_update.status_code == 200
    assert response_update.data['task']['title'] == payload['title']

    response_update = api_client.patch(f"/api/tasks/{task_id + '1'}", data=payload, format="json")
    logger.info(f" Updated task with id : {task_id + '1'}")
    logger.info(f"Response : {response_update.data}")
    assert response_update.status_code == 404

@mark.django_db  
def test_delete_task(api_client) -> None:  
    """  
    Test the delete task API  
    :param api_client:  
    :return: None  
    """  
    payload = {  
        "title": "Cook healthy food",  
        "content": "Cook healthy food for the family with high protein and low fat",  
    }  
   
    response_create = api_client.post("/api/tasks/", data=payload, format="json")  
    task_id = response_create.data["task"]["id"]  
    logger.info(f"Created task with id: {task_id}")  
    logger.info(f"Response: {response_create.data}")  
    assert response_create.status_code == 201  
    assert response_create.data["task"]["title"] == payload["title"]  

    response_delete = api_client.delete(f"/api/tasks/{task_id}", format="json")  
    assert response_delete.status_code == 204  
   
    response_read = api_client.get(f"/api/tasks/{task_id}", format="json")  
    assert response_read.status_code == 404  
   
    response_delete = api_client.delete(f"/api/tasks/{task_id + '1'}", format="json")  
    assert response_delete.status_code == 404




