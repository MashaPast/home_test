import pytest
from pytest_check import check


@pytest.mark.parametrize('expected_popularity_value',
                         [10 ** 7,
                          1.5 * 10 ** 7,
                          5 * 10 ** 7,
                          10 ** 8,
                          5 * 10 ** 8,
                          10 ** 9,
                          1.5 * 10 ** 9])
def test_popularity(browser, expected_popularity_value, get_table_data):
    for row in get_table_data.rows:
        with check:
            assert row.popularity > int(expected_popularity_value), f"{row.website_name} (Frontend:{row.frontend}" \
                                                                    f"|Backend:{row.backend}) has {row.popularity} " \
                                                                    f"unique visitors per month. (Expected more than " \
                                                                    f"{expected_popularity_value})"
