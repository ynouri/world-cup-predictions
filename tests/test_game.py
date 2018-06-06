import pytest
from worldcup import Game


@pytest.fixture
def game_example():
    return Game('France', 'Peru')


def test_game_creation(game_example):
    assert (
        game_example
        and game_example.team_1 == 'France'
        and game_example.team_2 == 'Peru'
    )


def test_game_get_teams(game_example):
    t1, t2 = game_example.get_teams()
    assert (
        t1 == 'France'
        and t2 == 'Peru'
    )


def test_play(game_example):
    game_example.play()
    t1_score, t2_score = game_example.score
    assert t1_score >= 0 and t2_score >= 0


def test_get_points(game_example):
    # Draw
    game_example.score = (1, 1)
    draw = game_example.get_points()
    # Team 1 wins
    game_example.score = (3, 1)
    t1_win = game_example.get_points()
    # Team 2 wins
    game_example.score = (0, 2)
    t2_win = game_example.get_points()
    assert (
        draw == (1, 1)
        and t1_win == (2, 0)
        and t2_win == (0, 2)
    )