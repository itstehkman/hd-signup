import logging
import urllib

from config import Config
from membership import Membership
from project_handler import ProjectHandler
import plans


""" Handles allowing the user to select a plan. """
class SelectPlanHandler(ProjectHandler):
  """ hash: The hash of the member we are selecting a plan for. """
  def get(self, member_hash):
    # Get the plans to show.
    selectable, unavailable = plans.Plan.get_plans_to_show()

    # Put the urls to send people to when they select a plan in there also, in a
    # form that is easy for jinja to understand.
    base_url = "/account/%s" % (member_hash)
    selectable_paired = []
    for plan in selectable:
      item = {}
      item["url"] = "%s?%s" % (base_url, urllib.urlencode({"plan": plan.name}))
      item["plan"] = plan

      selectable_paired.append(item)

    self.response.out.write(self.render("templates/select_plan.html",
                            selectable=selectable_paired,
                            unavailable=unavailable))
