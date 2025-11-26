import os
import pathlib

from ze.src.models import ConfigGen


def test_envs_dir_create(monkeypatch, tmp_path):
    fake_file = tmp_path / "fake_project" / "src" / "config.py"
    fake_file.parent.mkdir(parents=True)
    fake_file.write_text("# fake file")

    monkeypatch.setattr("ze.src.models", str(fake_file))

    called_paths = []

    def fake_makedirs(path, exist_ok=True):
        called_paths.append(path)

    monkeypatch.setattr(os, "makedirs", fake_makedirs)

    cfg = ConfigGen()

    expected_root = (
        pathlib.Path(fake_file)
        .resolve()
        .parent.parent.parent.parent.parent.parent.parent
    )

    expected_envs = expected_root / "envs"

    assert cfg._ConfigGen__envs_dir == str(expected_envs)

    assert len(called_paths) == 1
    assert called_paths[0] == str(expected_envs)
