# Monty Hall problem

## Task 
Develop an API-service with single endpoint to check Monty Hall problem (https://en.wikipedia.org/wiki/Monty_Hall_problem)

## Requirements
1. Flask
2. Pytest

## Service
POST /play/
Request body: `{choose_option: str, attempts: int}`, where `choose_option` — one of: keep (player does not change choice), `change` (player changes choice).
Expected response: `{wins: int, loose: int}`, where `wins` – number of wins and  `loose` – number of loose. In result, `wins + loose = attempts`

## Tests
1. POST /play/, body: `{choose_option: "keep", attempts: 100000}` and check in percentage that average wins ~33%
2. POST /play/, body: `{choose_option: "change", attempts: 100000}` and check in percentage that average wins ~66%
