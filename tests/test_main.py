import os
from pathlib import Path
import pytest
import shutil
from src.main import create_basic_structure, create_intermediate_structure, create_advanced_structure, create_extended_structure

@pytest.fixture
def output_path(tmpdir):
    path = Path(tmpdir.mkdir("project"))
    yield path
    shutil.rmtree(str(path))

def test_create_basic_structure(output_path: Path):
    create_basic_structure(str(output_path))
    assert (output_path / "src").is_dir()
    assert (output_path / "tests").is_dir()
    assert (output_path / "src" / "main.py").is_file()
    assert (output_path / "tests" / "test_main.py").is_file()
    assert (output_path / "README.md").is_file()


def test_create_intermediate_structure(output_path: Path):
    create_intermediate_structure(str(output_path))
    assert (output_path / "src").is_dir()
    assert (output_path / "tests").is_dir()
    assert (output_path / "src" / "main.py").is_file()
    assert (output_path / "tests" / "test_main.py").is_file()
    assert (output_path / "src" / "utils").is_dir()
    assert (output_path / "src" / "utils" / "helpers.py").is_file()
    assert (output_path / "tests" / "test_helpers.py").is_file()
    assert (output_path / "README.md").is_file()

def test_create_advanced_structure(output_path: Path):
    create_advanced_structure(str(output_path))
    assert (output_path / "src").is_dir()
    assert (output_path / "tests").is_dir()
    assert (output_path / "src" / "main.py").is_file()
    assert (output_path / "tests" / "test_main.py").is_file()
    assert (output_path / "src" / "utils").is_dir()
    assert (output_path / "src" / "utils" / "helpers.py").is_file()
    assert (output_path / "tests" / "test_helpers.py").is_file()
    assert (output_path / "src" / "services").is_dir()
    assert (output_path / "src" / "services" / "service.py").is_file()
    assert (output_path / "tests" / "test_service.py").is_file()
    assert (output_path / "README.md").is_file()

def test_create_extended_structure(output_path: Path):
    create_extended_structure(str(output_path))
    assert (output_path / "src").is_dir()
    assert (output_path / "tests").is_dir()
    assert (output_path / "src" / "main.py").is_file()
    assert (output_path / "tests" / "test_main.py").is_file()
    assert (output_path / "src" / "utils").is_dir()
    assert (output_path / "src" / "utils" / "helpers.py").is_file()
    assert (output_path / "tests" / "test_helpers.py").is_file()
    assert (output_path / "src" / "services").is_dir()
    assert (output_path / "src" / "services" / "service.py").is_file()
    assert (output_path / "tests" / "test_service.py").is_file()
    assert (output_path / "assets").is_dir()
    assert (output_path / "data").is_dir()
    assert (output_path / "assets" / "images").is_dir()
    assert (output_path / "data" / "input").is_dir()
    assert (output_path / "data" / "intermediate").is_dir()
    assert (output_path / "data" / "output").is_dir()
    assert (output_path / "README.md").is_file()