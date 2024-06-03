import pytest
from Api.workpackage.testsfonc.api_workpackage import Apiworkpackage






@pytest.fixture
def api_workpackage():
    return Apiworkpackage()


def test_postwork_valid_data(api_workpackage):
    
    
    # api_changerequest  = Apichangerequest()
    
    data = {
      "id": 0,
      "lockVersion": 0,
      "description": "string",
      "subject": "string",
      "scheduleManually": True,
      "startDate": "2024-05-22T07:36:17.578Z",
      "dueDate": "2024-05-22T07:36:17.578Z",
      "date": "2024-05-22T07:36:17.578Z",
      "derivedStartDate": "2024-05-22T07:36:17.578Z",
      "derivedDueDate": "2024-05-22T07:36:17.578Z",
      "duration": "string",
      "estimatedTime": "string",
      "derivedEstimatedTime": "string",
      "ignoreNonWorkingDays": True,
      "percentageDone": 0,
      "type": "phase",
      "projectId": 0,
      "parentId": 0,
      "assignee": {
        "firstName": "string",
        "lastName": "string",
        "cuid": "mhdl5011",
        "email": "rebecca.touomno@orange.com",
        "id": 0
      },
      "weight": 0,
      "visibleInTimeline": True,
      "visibleInPPT": True
}
    
    response = api_workpackage.post_workpackage(data)
    assert response.status_code == 201





def test_postwork_invalid_token(api_workpackage):
   
    
   
    data = { 
    "id": 0,
    "lockVersion": 0,
    "description": "string",
    "subject": "string",
    "scheduleManually": True,
    "startDate": "2024-05-22T07:36:17.578Z",
    "dueDate": "2024-05-22T07:36:17.578Z",
    "date": "2024-05-22T07:36:17.578Z",
    "derivedStartDate": "2024-05-22T07:36:17.578Z",
    "derivedDueDate": "2024-05-22T07:36:17.578Z",
    "duration": "string",
    "estimatedTime": "string",
    "derivedEstimatedTime": "string",
    "ignoreNonWorkingDays": True,
    "percentageDone": 0,
    "type": "string",
    "projectId": 0,
    "parentId": 0,
    "assignee": {
      "firstName": "string",
      "lastName": "string",
       "cuid": "mhdl5011",
        "email": "rebecca.touomno@orange.com",
      "id": 0
    },
    "weight": 0,
    "visibleInTimeline": True,
    "visibleInPPT": True
    }

    api_workpackage.headers['Authorization'] = 'Bearer token_invalid'
    response = api_workpackage.post_workpackage(data)
    assert response.status_code == 401





def test_postwork_no_token(api_workpackage):
   
    
   
    data = { 
            "id": 0,
      "lockVersion": 0,
      "description": "string",
      "subject": "string",
      "scheduleManually": True,
      "startDate": "2024-05-22T07:36:17.578Z",
      "dueDate": "2024-05-22T07:36:17.578Z",
      "date": "2024-05-22T07:36:17.578Z",
      "derivedStartDate": "2024-05-22T07:36:17.578Z",
      "derivedDueDate": "2024-05-22T07:36:17.578Z",
      "duration": "string",
      "estimatedTime": "string",
      "derivedEstimatedTime": "string",
      "ignoreNonWorkingDays": True,
      "percentageDone": 0,
      "type": "string",
      "projectId": 0,
      "parentId": 0,
      "assignee": {
        "firstName": "string",
        "lastName": "string",
        "cuid": "mhdl5011",
        "email": "rebecca.touomno@orange.com",
        "id": 0
      },
      "weight": 0,
      "visibleInTimeline": True,
      "visibleInPPT": True
    }

    api_workpackage.headers['Authorization'] = ''
    response = api_workpackage.post_workpackage(data)
    assert response.status_code == 401

 
 
 
def test_postwork_value_error_on_field_subject(api_workpackage):
    
    data = { 
       "id": 0,
      "lockVersion": 0,
      "description": "string",
      "subject": 2,
      "scheduleManually": True,
      "startDate": "2024-05-22T07:36:17.578Z",
      "dueDate": "2024-05-22T07:36:17.578Z",
      "date": "2024-05-22T07:36:17.578Z",
      "derivedStartDate": "2024-05-22T07:36:17.578Z",
      "derivedDueDate": "2024-05-22T07:36:17.578Z",
      "duration": "string",
      "estimatedTime": "string",
      "derivedEstimatedTime": "string",
      "ignoreNonWorkingDays": True,
      "percentageDone": 0,
      "type": "string",
      "projectId": 0,
      "parentId": 0,
      "assignee": {
        "firstName": "string",
        "lastName": "string",
         "cuid": "mhdl5011",
        "email": "rebecca.touomno@orange.com",
        "id": 0
      },
      "weight": 0,
      "visibleInTimeline": True,
      "visibleInPPT": True
    }
    
    response = api_workpackage.post_workpackage(data)
    assert response.status_code == 400       
    
    


def test_postwork_value_error_on_type_field(api_workpackage):
    
    
    data = { 
        "id": 0,
        "lockVersion": 0,
        "description": "string",
        "subject": "string",
        "scheduleManually": True,
        "startDate": "2024-05-22T07:36:17.578Z",
        "dueDate": "2024-05-22T07:36:17.578Z",
        "date": "2024-05-22T07:36:17.578Z",
        "derivedStartDate": "2024-05-22T07:36:17.578Z",
        "derivedDueDate": "2024-05-22T07:36:17.578Z",
        "duration": "string",
        "estimatedTime": "string",
        "derivedEstimatedTime": "string",
        "ignoreNonWorkingDays": True,
        "percentageDone": 0,
        "type": "string",
        "projectId": 0,
        "parentId": 0,
        "assignee": {
          "firstName": "string",
          "lastName": "string",
          "cuid": "mhdl5011",
        "email": "rebecca.touomno@orange.com",
          "id": 0
        },
        "weight": 0,
        "visibleInTimeline": True,
        "visibleInPPT": True
    }
    api_workpackage.idpostworkpackage = 'ChangeRequestId=4dca7c5f-c145-48ef-8bf6-84b6d473bdfa'
    response = api_workpackage.post_workpackage(data)
    assert response.status_code == 500
    
 
 
    
def test_postwork_no_value_on_type_field(api_workpackage):
    
    
   
    data = { 
       "id": 0,
        "lockVersion": 0,
        "description": "string",
        "subject": "string",
        "scheduleManually": True,
        "startDate": "2024-05-22T07:36:17.578Z",
        "dueDate": "2024-05-22T07:36:17.578Z",
        "date": "2024-05-22T07:36:17.578Z",
        "derivedStartDate": "2024-05-22T07:36:17.578Z",
        "derivedDueDate": "2024-05-22T07:36:17.578Z",
        "duration": "string",
        "estimatedTime": "string",
        "derivedEstimatedTime": "string",
        "ignoreNonWorkingDays": True,
        "percentageDone": 0,
        "type": "",
        "projectId": 0,
        "parentId": 0,
        "assignee": {
          "firstName": "string",
          "lastName": "string",
          "cuid": "mhdl5011",
          "email": "rebecca.touomno@orange.com",
          "id": 0
        },
        "weight": 0,
        "visibleInTimeline": True,
        "visibleInPPT": True
    }
    api_workpackage.idpostworkpackage = 'ChangeRequestId=af17ceef-6884-4cf6-a94e-4d8cb6a21098'
    response = api_workpackage.post_workpackage(data)
    assert response.status_code == 500
        
    
    
    
def test_postwork__value_id_alreased_used(api_workpackage):
    
    
   
    data = { 
       "id": 0,
        "lockVersion": 0,
        "description": "string",
        "subject": "string",
        "scheduleManually": True,
        "startDate": "2024-05-22T07:36:17.578Z",
        "dueDate": "2024-05-22T07:36:17.578Z",
        "date": "2024-05-22T07:36:17.578Z",
        "derivedStartDate": "2024-05-22T07:36:17.578Z",
        "derivedDueDate": "2024-05-22T07:36:17.578Z",
        "duration": "string",
        "estimatedTime": "string",
        "derivedEstimatedTime": "string",
        "ignoreNonWorkingDays": True,
        "percentageDone": 0,
        "type": "string",
        "projectId": 0,
        "parentId": 0,
        "assignee": {
          "firstName": "string",
          "lastName": "string",
          "cuid": "mhdl5011",
          "email": "rebecca.touomno@orange.com",
          "id": 0
        },
        "weight": 0,
        "visibleInTimeline": True,
        "visibleInPPT": True
    }
    api_workpackage.idpostworkpackage = 'ChangeRequestId=8b5b3c90-45ce-4dc1-a26c-75d361643af7'
    response = api_workpackage.post_workpackage(data)
    assert response.status_code == 403
        
        
    
def test_postwork_wrong_value_on_field_id(api_workpackage):
 
    data = { 
         "id": 0,
        "lockVersion": 0,
        "description": "string",
        "subject": "string",
        "scheduleManually": True,
        "startDate": "2024-05-22T07:36:17.578Z",
        "dueDate": "2024-05-22T07:36:17.578Z",
        "date": "2024-05-22T07:36:17.578Z",
        "derivedStartDate": "2024-05-22T07:36:17.578Z",
        "derivedDueDate": "2024-05-22T07:36:17.578Z",
        "duration": "string",
        "estimatedTime": "string",
        "derivedEstimatedTime": "string",
        "ignoreNonWorkingDays": True,
        "percentageDone": 0,
        "type": "phase",
        "projectId": 0,
        "parentId": 0,
        "assignee": {
          "firstName": "string",
          "lastName": "string",
          "cuid": "string",
          "email": "string",
          "id": 0
        },
        "weight": 0,
        "visibleInTimeline": True,
        "visibleInPPT": True
    }
    api_workpackage.idpostworkpackage = 'ChangeRequestId=14c02d22-a789-4c9b-ba27-f133378e6ff6'
    response = api_workpackage.post_workpackage(data)
    assert response.status_code == 404




def test_postworkpackage_wrong_data_type_on_field_id(api_workpackage):
   
    data = { 
         "id": 0,
        "lockVersion": 0,
        "description": "string",
        "subject": "string",
        "scheduleManually": True,
        "startDate": "2024-05-22T07:36:17.578Z",
        "dueDate": "2024-05-22T07:36:17.578Z",
        "date": "2024-05-22T07:36:17.578Z",
        "derivedStartDate": "2024-05-22T07:36:17.578Z",
        "derivedDueDate": "2024-05-22T07:36:17.578Z",
        "duration": "string",
        "estimatedTime": "string",
        "derivedEstimatedTime": "string",
        "ignoreNonWorkingDays": True,
        "percentageDone": 0,
        "type": "phase",
        "projectId": 0,
        "parentId": 0,
        "assignee": {
          "firstName": "string",
          "lastName": "string",
          "cuid": "string",
          "email": "string",
          "id": 0
        },
        "weight": 0,
        "visibleInTimeline": True,
        "visibleInPPT": True
    }
    api_workpackage.idpostworkpackage = 'ChangeRequestId=11a34b52-e03b'
    response = api_workpackage.post_workpackage(data)
    assert response.status_code == 400





def test_postworkpackage_no_value_on_field_id(api_workpackage):
   
    data = { 
        "id": 0,
        "lockVersion": 0,
        "description": "string",
        "subject": "string",
        "scheduleManually": True,
        "startDate": "2024-05-22T07:36:17.578Z",
        "dueDate": "2024-05-22T07:36:17.578Z",
        "date": "2024-05-22T07:36:17.578Z",
        "derivedStartDate": "2024-05-22T07:36:17.578Z",
        "derivedDueDate": "2024-05-22T07:36:17.578Z",
        "duration": "string",
        "estimatedTime": "string",
        "derivedEstimatedTime": "string",
        "ignoreNonWorkingDays": True,
        "percentageDone": 0,
        "type": "phase",
        "projectId": 0,
        "parentId": 0,
        "assignee": {
          "firstName": "string",
          "lastName": "string",
          "cuid": "string",
          "email": "string",
          "id": 0
        },
        "weight": 0,
        "visibleInTimeline": True,
        "visibleInPPT": True
    }
    api_workpackage.idpostworkpackage = 'ChangeRequestId='
    response = api_workpackage.post_workpackage(data)
    assert response.status_code == 400
    