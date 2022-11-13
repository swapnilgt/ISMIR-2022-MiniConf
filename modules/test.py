import tutorials
import sys

# TODO Move the utils code to the same repo once everything is setup.
sys.path.append("..")
sys.path.append(".")

from utils import slack as slackUtils
from utils import zoom as zoomUtils
from modules.tutorials import Tutorials
from modules.papers import Papers
from modules.zoom_creator import ZoomCreator

# Uncomment below for zoom creation
# zoomCreator =  ZoomCreator("../../ISMIR-2022-Miniconf-Data/sitedata/events.csv")
# zoomCreator.setupZoomCalls(zoomUtils)

# Uncommnet below for tutorials slack setup
# tutObj = Tutorials("../../ISMIR-2022-Miniconf-Data/sitedata/events.csv", "../../ISMIR-2022-Miniconf-Data/sitedata/townscript.csv")
# tutObj.setupSlackChannels(slackUtils)

##########################

# Uncommnet below for papers slack setup
paperObj = Papers("../../ISMIR-2022-Miniconf-Data/sitedata/papers.csv")
paperObj.setupSlackChannels(slackUtils)