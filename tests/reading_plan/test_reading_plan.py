import pytest
from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
from tech_news.database import find_news


mock_db = [
    {
        "title": "Alguma coisa",
        "reading_time": 5,
    },
    {
        "title": "Deixa Acontecer",
        "reading_time": 25,
    },
    {
        "title": "Notícia legal",
        "reading_time": 3,
    },
    {
        "title": "Notícia longa 2",
        "reading_time": 10,
    },
]


def test_reading_plan_group_news(mocker):
    result = mocker.patch(find_news)
    result.return_value = mock_db
    result_function = ReadingPlanService.group_news_for_available_time(10)
    assert len(result_function["readable"]) == 2
    assert len(result_function["unreadable"]) == 1
    assert result_function["readable"][0]["unfilled_time"] == 2
    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(0)
