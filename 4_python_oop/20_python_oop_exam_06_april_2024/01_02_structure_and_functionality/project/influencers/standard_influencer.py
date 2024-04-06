from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class StandardInfluencer(BaseInfluencer):
    PAYMENT_PERCENTAGE = 0.45

    def calculate_payment(self, campaign: BaseCampaign):
        payment = float(campaign.budget * self.PAYMENT_PERCENTAGE)
        return payment

    def reached_followers(self, campaign_type: str):
        if campaign_type == "HighBudgetCampaign":
            return int((self.followers * self.engagement_rate) * 1.2)
        if campaign_type == "LowBudgetCampaign":
            return int((self.followers * self.engagement_rate) * 0.9)
