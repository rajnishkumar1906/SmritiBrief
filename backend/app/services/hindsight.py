from hindsight_client import Hindsight
from app.core.config import settings

class HindsightManager:
    def __init__(self):
        if not settings.HINDSIGHT_API_KEY:
            raise ValueError("HINDSIGHT_API_KEY not found in settings")
        
        self.client = Hindsight(
            base_url="https://api.hindsight.vectorize.io",
            api_key=settings.HINDSIGHT_API_KEY
        )

    def retain(self, bank_id: str, content: str):
        """Store meeting notes or observations"""
        return self.client.retain(bank_id=bank_id, content=content)

    def recall(self, bank_id: str, query: str, top_k: int = 3):
        """Search for relevant past context"""
        return self.client.recall(bank_id=bank_id, query=query, top_k=top_k)

    def reflect(self, bank_id: str, query: str):
        """Generate high-level insights or leverage reports"""
        return self.client.reflect(bank_id=bank_id, query=query)

hindsight_service = HindsightManager()
