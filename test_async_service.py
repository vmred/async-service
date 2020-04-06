from async_service import AsyncService


class TestAsyncService:
    def test_one(self):
        async_service = AsyncService()
        async_service.verify_documents()
