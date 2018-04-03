import http.client
import json
import os

conn = http.client.HTTPSConnection("public1.visualstudio.com")

payload = json.dumps({'name': 'RedTeam.3',
 'path': '\\RedTeam',
 'process': {'phases': [{'condition': 'succeeded()',
                         'jobAuthorizationScope': 'projectCollection',
                         'jobCancelTimeoutInMinutes': 1,
                         'name': 'Phase 1',
                         'refName': 'Phase_1',
                         'steps': [{'alwaysRun': False,
                                    'condition': 'succeeded()',
                                    'continueOnError': False,
                                    'displayName': 'PowerShell Script',
                                    'enabled': True,
                                    'environment': {},
                                    'inputs': {'arguments': '',
                                               'failOnStandardError': 'true',
                                               'inlineScript': '$ttl = '
                                                               '[int]$env:ttl\n'
                                                               'Write-Host '
                                                               '"TTL=$ttl"\n'
                                                               '\n'
                                                               'if ($ttl -gt '
                                                               '0) {\n'
                                                               '  $newTtl = '
                                                               '$ttl - 1\n'
                                                               '\n'
                                                               '  $url = '
                                                               '"https://public1.visualstudio.com/MyFirstProject/_apis/build/builds?api-version=4.1-preview"\n'
                                                               '$body = @{\n'
                                                               'definition = '
                                                               '@{\n'
                                                               'id = 7\n'
                                                               'type = '
                                                               '"build"\n'
                                                               '}\n'
                                                               'parameters = '
                                                               '"{`"ttl`":`"$newTtl`"}"\n'
                                                               '} | '
                                                               'ConvertTo-Json\n'
                                                               '$headers = @{ '
                                                               'Authorization '
                                                               '= "Bearer '
                                                               '$env:SYSTEM_ACCESSTOKEN"\n'
                                                               '"Content-Type" '
                                                               '= '
                                                               '"application/json" '
                                                               '}\n'
                                                               '  '
                                                               'Invoke-RestMethod '
                                                               '-Method "Post" '
                                                               '-Uri $url '
                                                               '-Body $body '
                                                               '-Headers '
                                                               '$headers\n'
                                                               '}',
                                               'scriptName': '',
                                               'scriptType': 'inlineScript',
                                               'workingFolder': ''},
                                    'task': {'definitionType': 'task',
                                             'id': 'e213ff0f-5d5c-4791-802d-52ea3e7be1f1',
                                             'versionSpec': '1.*'},
                                    'timeoutInMinutes': 0}],
                         'target': {'allowScriptsAuthAccessOption': True,
                                    'executionOptions': {'type': 0},
                                    'type': 1}}],
             'type': 1},
 'repository': {'checkoutSubmodules': False,
                'clean': 'false',
                'defaultBranch': 'master',
                'id': 'vtbassmatt/vsts-demo',
                'name': 'vtbassmatt/vsts-demo',
                'properties': {'apiUrl': 'https://api.github.com/repos/vtbassmatt/vsts-demo',
                               'branchesUrl': 'https://api.github.com/repos/vtbassmatt/vsts-demo/branches',
                               'checkoutNestedSubmodules': 'false',
                               'cleanOptions': '0',
                               'cloneUrl': 'https://github.com/vtbassmatt/vsts-demo.git',
                               'connectedServiceId': '8c5a5af1-58e0-45e8-ba85-125d53cd0208',
                               'defaultBranch': 'master',
                               'fetchDepth': '0',
                               'fullName': 'vtbassmatt/vsts-demo',
                               'gitLfsSupport': 'false',
                               'isPrivate': 'False',
                               'labelSources': '0',
                               'labelSourcesFormat': '$(build.buildNumber)',
                               'refsUrl': 'https://api.github.com/repos/vtbassmatt/vsts-demo/git/refs',
                               'reportBuildStatus': 'true',
                               'skipSyncSource': 'true'},
                'type': 'GitHub',
                'url': 'https://github.com/vtbassmatt/vsts-demo.git'}})

token = os.environ['SYSTEM_ACCESSTOKEN']

headers = {
    'Authorization': f"Bearer {token}",
    'content-type': "application/json"
    }

conn.request("POST", "/MyFirstProject/_apis/build/definitions?api-version=4.1-preview", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
