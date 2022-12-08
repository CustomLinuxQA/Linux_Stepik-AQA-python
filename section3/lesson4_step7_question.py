import pytest


@pytest.fixture(scope="class")
def prepare_faces():
    print("first", "\n")
    yield
    print("end", "\n")


@pytest.fixture()
def very_important_fixture():
    print("second", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print("autouse", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        print(1)
    def test_second_smiling_faces(self, prepare_faces):
        print(1)