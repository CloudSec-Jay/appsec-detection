import os
import sys 
import logging
from datetime import datetime
import subprocess

#Creating the log file for scrpit

LOG_FILE = 'var/ossec/logs/ansible-trigger.log'
logging.basicConfig(
  filename=LOG_FILE
  level=logging.INFO,
  format='%(asctime)s - %(levelname)s - %(message)s'
)


ANSIBLE_PLAYBOOK_DIR = 'opt/security-playbooks'
ANSIBLE_INVENTORY ='opt/security-playbooks/inventory/hosts'

PLAYBOOK_MAP = {
  # 'rule_number' : 'yaml-file'  
}

