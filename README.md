# Hetrogeneous Auto Dungeon Master Lambda Handler

[![Test and Format](https://github.com/jeremylt/autoDM/actions/workflows/test.yml/badge.svg)](https://github.com/jeremylt/autoDM/actions/workflows/test.yml)
[![Deploy Docs](https://github.com/jeremylt/autoDM/actions/workflows/doc.yml/badge.svg)](https://github.com/jeremylt/autoDM/actions/workflows/doc.yml)

## Overview

This repository provides the lambda handler code for an auto DM for Dungeons and Dragons 5e via Alexa skill or web interface.

The user can request a monster, NPC, encounter, or plot arc by challenge rating, environment, or both.
Monsters come from the Monster Manual, Volo's Guide to Monsters, and Mordenkainen's Tome of Foes.
Plot arc ideas and multi-monster challenge rating calculations come from the Dungeon Master's Guide.

## Technology

The Auto DM is hosted as a Lambda function on AWS.
The Alexa skill is hosted by Amazon.
The web interface uses an Amazon API Gateway and the demo web version is hosted on GitHub Pages.

## Documentation

Sphinx documentation can be found [here](https://jeremylt.github.io/autoDM/).

## Demo

The Alexa skill can be accessed [here](https://www.amazon.com/Jeremy-L-Thompson-Auto-Master/dp/B07QFVN96G/ref=sr_1_1?keywords=auto+game+master&qid=1555011836&s=digital-skills&sr=1-1-catcorr).

A demo web version can be accessed [here](https://jeremylt.github.io/autoDMWebsite/).
