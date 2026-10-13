"""Build one Physics topic with the approved readable panel layout."""
from physics_helpers import SUBJECT,TOPICS
from physics_maps import MAPS
from readable_subject_mindmaps import build as build_readable
import sys

def build(n):build_readable(SUBJECT,TOPICS,MAPS,n)
if __name__=='__main__':build(int(sys.argv[1]))
