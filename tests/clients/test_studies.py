import pytest

from berserk import Client


class TestStudies:
    @pytest.mark.vcr
    def test_export_by_username(self):
        pgns = list(Client().studies.export_by_username("neio"))
        assert len(pgns) == 1
        assert '[StudyName "neio\'s Study"]' in pgns[0]
