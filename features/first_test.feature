#Укажем что это за фича
Feature: Checking search
#Укажем имя сценария (в одной фиче может быть несколько)
Scenario: Open browser Firefox and start search
  Given browser Firefox
  Then website "https://ya.ru"
  Then enter text Yandex "kek"
Scenario: Open browser Firefox and start search
  Given browser Firefox
  Then website "https://google.ru"
  Then enter text Google "kek"
Scenario: Open browser Chrome and start search
  Given browser Chrome
  Then website "https://ya.ru"
  Then enter text Yandex "kek"
Scenario: Open browser Chrome and start search
  Given browser Chrome
  Then website "https://google.ru"
  Then enter text Google "kek"