import os
import sys
import json
import logging
sys.path.append(os.environ.get('EFS_MOUNT_PATH'))
import tensorflow as tf

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def predict(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps({
            'tf_version': tf.__version__
        })
    }
