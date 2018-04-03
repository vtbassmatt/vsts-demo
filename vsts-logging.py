import os
import uuid

#print("##vso[task.logissue type=warning; code=42;]Red team is here")

timeline_root_id = uuid.uuid4()
print(f"##vso[task.logdetail id={str(timeline_root_id)};name=Red Team;type=build;order=1]Hi from Red")

for x in "Hi from Red Team":
  timeline_local_id = uuid.uuid4()
  print(f"##vso[task.logdetail id={str(timeline_local_id)};parentid={str(timeline_root_id)};name={x};type=build;order=1]RED")

#repopath = os.environ['BUILD_REPOSITORY_LOCALPATH']
#print(f"##vso[task.addattachment type=myattachmenttype;name=myattachmentname;]{repopath}/vsts-logging.py")
