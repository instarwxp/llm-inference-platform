from locust import HttpUser, task, between

class GatewayUser(HttpUser):
    wait_time = between(1, 2)

    @task(3)
    def health_check(self):
        self.client.get("/health")

    @task(2)
    def list_models(self):
        self.client.get("/api/models")

    @task(1)
    def chat(self):
        self.client.post("/api/chat", json={
            "model": "llama3.2",
            "message": "Say hello in one word."
        })
