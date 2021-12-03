#!/bin/zsh

cd "$(dirname "$0")"

source ./homeassistant.sh

homeassistant_switch switch.dori_pc_relay turn_on
