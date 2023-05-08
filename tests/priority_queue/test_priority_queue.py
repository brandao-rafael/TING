from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    """Aqui irá sua implementação"""
    priority_queue = PriorityQueue()
    priority_queue.enqueue({"qtd_linhas": 9})
    priority_queue.enqueue({"qtd_linhas": 4})
    priority_queue.enqueue({"qtd_linhas": 2})
    priority_queue.enqueue({"qtd_linhas": 5})
    priority_queue.enqueue({"qtd_linhas": 7})
    priority_queue.enqueue({"qtd_linhas": 11})
    priority_queue.enqueue({"qtd_linhas": 3})

    assert len(priority_queue) == 7
    assert priority_queue.search(0) == {"qtd_linhas": 4}

    priority_queue.dequeue()
    assert priority_queue.search(0) == {"qtd_linhas": 2}
    assert priority_queue.search(5) == {"qtd_linhas": 11}

    priority_queue.dequeue()
    assert priority_queue.search(0) == {"qtd_linhas": 3}
    assert priority_queue.search(4) == {"qtd_linhas": 11}

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(5)
