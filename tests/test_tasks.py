from src.app import create_task

def test_create_task():
    task = create_task("Teste", "Alta")
    assert task["title"] == "Teste"
    assert task["priority"] == "Alta"
