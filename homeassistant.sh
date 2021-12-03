#!/bin/zsh
source $HOME/.config/homeassistant.sh

homeassistant_switch() {
    ENTITY="$1"
    CONTROL="$2"
    curl -X POST -H "Authorization: Bearer $HOMEASSISTANT_TOKEN" -H 'Content-Type: application/json' -d "{\"entity_id\": \"$ENTITY\"}" "$HOMEASSISTANT_URL/api/services/switch/$CONTROL"
}
