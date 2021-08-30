import datetime
import os
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
def my_scheduled_job():
  print('hello ,++++++++++++++++++++++++')
  logger.info( "cron job work")

