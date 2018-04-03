import uuid

print("##vso[task.logissue type=warning; code=42;]Red team is here")

timeline_id = uuid.uuid4()
print(f"##vso[task.logdetail id={str(timeline_id)};name=Red Team;type=build;order=1]Hi from Red")

print("##vso[task.addattachment type=myattachmenttype;name=myattachmentname;]vsts-logging.py")
