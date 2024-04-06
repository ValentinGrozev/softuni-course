from typing import List
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    VALID_TYPES_OF_INFLUENCER = {
        "PremiumInfluencer": PremiumInfluencer,
        "StandardInfluencer": StandardInfluencer
    }

    VALID_TYPES_OF_CAMPAIGN = {
        "HighBudgetCampaign": HighBudgetCampaign,
        "LowBudgetCampaign": LowBudgetCampaign
    }

    def __init__(self):
        self.influencers: List = []
        self.campaigns: List = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.VALID_TYPES_OF_INFLUENCER:
            return f"{influencer_type} is not an allowed influencer type."

        try:
            next(filter(lambda i: i.username == username, self.influencers))
            return f"{username} is already registered."
        except StopIteration:

            influencer = self.VALID_TYPES_OF_INFLUENCER[influencer_type](username, followers, engagement_rate)
            self.influencers.append(influencer)
            return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_TYPES_OF_CAMPAIGN:
            return f"{campaign_type} is not a valid campaign type."

        try:
            next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns))
            return f"Campaign ID {campaign_id} has already been created."
        except StopIteration:

            campaign = self.VALID_TYPES_OF_CAMPAIGN[campaign_type](campaign_id, brand, required_engagement)
            self.campaigns.append(campaign)
            return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        try:
            influencer = next(filter(lambda i: i.username == influencer_username, self.influencers))
        except StopIteration:
            return f"Influencer '{influencer_username}' not found."

        try:
            campaign = next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns))
        except StopIteration:
            return f"Campaign with ID {campaign_id} not found."

        if campaign.check_eligibility(influencer.engagement_rate) is not True:
            return (f"Influencer '{influencer_username}' does not meet the eligibility "
                    f"criteria for the campaign with ID {campaign_id}.")

        if influencer.calculate_payment(campaign) > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= influencer.calculate_payment(campaign)
            influencer.campaigns_participated.append(campaign)

            return (f"Influencer '{influencer_username}' has successfully"
                    f" participated in the campaign with ID {campaign_id}.")

    def calculate_total_reached_followers(self):
        campaign_information = {}

        for influencer in self.influencers:
            for campaign in influencer.campaigns_participated:
                if campaign not in campaign_information:
                    campaign_information[campaign] = 0
                campaign_information[campaign] += influencer.reached_followers(campaign.__class__.__name__)

        return campaign_information

    def influencer_campaign_report(self, username: str):
        influencer = next(filter(lambda i: i.username == username, self.influencers))

        if len(influencer.campaigns_participated) == 0:
            return f"{username} has not participated in any campaigns."

        return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        sorted_campaign = sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget))

        result = "$$ Campaign Statistics $$"

        campaign_info = self.calculate_total_reached_followers()

        for campaign in sorted_campaign:
            result += (f'\n  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)}, '
                       f'Total budget: ${campaign.budget:.2f}, Total reached '
                       f'followers: {campaign_info[campaign] if campaign in campaign_info else 0}')

        return result
