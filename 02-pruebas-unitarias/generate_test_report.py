#!/usr/bin/env python3
"""Ejecuta pytest, genera junit XML y lo convierte a JSON en evidencias/"""
import subprocess
import os
import xml.etree.ElementTree as ET
import json
import sys

ROOT = os.path.dirname(__file__)
EVID = os.path.join(ROOT, 'evidencias')
if not os.path.exists(EVID):
    os.makedirs(EVID)

XML_PATH = os.path.join(EVID, 'junit_report.xml')
JSON_PATH = os.path.join(EVID, 'test_report.json')
PYTEST_ARGS = [
    sys.executable, '-m', 'pytest', 'src/test/python/test_auth.py', '-q', '--tb=short', f'--junitxml={XML_PATH}'
]

print('Running:', ' '.join(PYTEST_ARGS))
res = subprocess.run(PYTEST_ARGS, cwd=ROOT, capture_output=True, text=True)
print(res.stdout)
print(res.stderr, file=sys.stderr)

# Parse junit xml if created
if not os.path.exists(XML_PATH):
    print('XML report not found at', XML_PATH)
    sys.exit(1)

root = ET.parse(XML_PATH).getroot()
report = {
    'tests': int(root.attrib.get('tests', 0)),
    'errors': int(root.attrib.get('errors', 0)),
    'failures': int(root.attrib.get('failures', 0)),
    'skipped': int(root.attrib.get('skipped', 0)),
    'time': float(root.attrib.get('time', 0.0)),
    'cases': []
}

for case in root.iter('testcase'):
    name = case.attrib.get('name')
    classname = case.attrib.get('classname')
    time = float(case.attrib.get('time', 0.0))
    status = 'passed'
    message = ''
    details = ''
    if case.find('failure') is not None:
        status = 'failure'
        message = case.find('failure').attrib.get('message', '')
        details = case.find('failure').text or ''
    elif case.find('error') is not None:
        status = 'error'
        message = case.find('error').attrib.get('message', '')
        details = case.find('error').text or ''
    elif case.find('skipped') is not None:
        status = 'skipped'
        message = case.find('skipped').attrib.get('message', '')
        details = case.find('skipped').text or ''

    report['cases'].append({
        'name': name,
        'classname': classname,
        'time': time,
        'status': status,
        'message': message,
        'details': details
    })

with open(JSON_PATH, 'w', encoding='utf-8') as f:
    json.dump(report, f, indent=2, ensure_ascii=False)

print('JSON report written to', JSON_PATH)
